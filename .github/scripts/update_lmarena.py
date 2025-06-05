# scripts/update_lmarena_leaderboard.py

import requests
import pandas as pd
import os
from datetime import datetime
import hashlib
import logging

# 配置日志记录
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def get_file_hash(file_path):
    """
    计算文件的MD5哈希值
    """
    if not os.path.exists(file_path):
        return None
    try:
        with open(file_path, 'rb') as f:
            return hashlib.md5(f.read()).hexdigest()
    except Exception as e:
        logging.error(f"Error calculating hash for {file_path}: {e}")
        return None

def update_leaderboard_data():
    """
    从 fboulnois/llm-leaderboard-csv 项目下载排行榜数据，
    处理后生成 Markdown 文件。
    """
    # 最新 CSV 文件的下载 URL
    # 根据您提供的 lmsys.csv 文件名进行修正
    csv_url = 'https://github.com/fboulnois/llm-leaderboard-csv/releases/latest/download/lmsys.csv'
    
    # 输出 Markdown 文件的路径
    output_file_path = 'other/model_rank/lmarena.md'

    logging.info(f'Attempting to download CSV from: {csv_url}')
    try:
        response = requests.get(csv_url)
        response.raise_for_status() # 如果请求失败，抛出异常

        # 将CSV内容读入Pandas DataFrame
        from io import StringIO
        df = pd.read_csv(StringIO(response.text))
        logging.info(f'Successfully downloaded CSV with {len(df)} rows.')

        # 检查并选择需要的列，并重命名
        # 这里的列名已根据您提供的 lmsys.csv 文件头进行调整
        required_columns = [
            'rank',            # Upper Bound 排名
            'rank_stylectrl',  # Style-controlled 排名
            'model',           # 模型名称
            'arena_score',     # 竞技场分数
            '95_pct_ci',       # 95% 置信区间
            'votes',           # 投票数
            'organization',    # 组织机构
            'license',         # 许可协议
            'knowledge_cutoff',# 知识截止日期
            'url'              # 链接
        ]

        # 过滤出存在的列，避免因为CSV缺少列而报错
        available_columns = [col for col in required_columns if col in df.columns]
        if len(available_columns) != len(required_columns):
            logging.warning(f'Not all required columns found in CSV. Missing: {set(required_columns) - set(available_columns)}')
            df_selected = df[available_columns]
        else:
            df_selected = df[required_columns]

        # 重命名列以便在 Markdown 中显示
        df_selected.columns = [
            '排名(UB)',
            '排名(StyleCtrl)',
            '模型名',
            '分数',
            '置信区间(95%)',
            '票数',
            '服务商',
            '许可协议',
            '知识截止日期',
            '链接'
        ]
        
        # 格式化数值列
        df_selected['分数'] = df_selected['分数'].round(2)
        # '置信区间(95%)' 列（原 '95_pct_ci'）已经是字符串，不需要再次格式化或四舍五入
        df_selected['票数'] = df_selected['票数'].apply(lambda x: f'{x:,}') # 添加千位分隔符

        # 获取当前 UTC 时间作为更新时间
        update_time = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC')

        # 生成 Markdown 内容
        markdown_content = f'''# LLM Arena 排行榜

这是一个基于 Chatbot Arena (lmarena.ai) 数据的排行榜，通过自动化流程生成。

> 数据更新时间: {update_time}

{df_selected.to_markdown(index=False)}

## 说明

- **排名(UB)**：基于 Bradley-Terry 模型的排名，其中'上界' (Upper Bound) 通常指在统计学上对模型表现的乐观估计，帮助理解模型的潜在竞争力。
- **排名(StyleCtrl)**：在计算排名时，会尝试控制或消除不同模型在对话风格上的潜在影响，以更纯粹地评估其核心能力。这有助于减少因模型回复风格（如冗长、简洁）带来的偏好偏差。
- **模型名**：大型语言模型 (LLM) 的名称。
- **分数**：模型在竞技场中通过用户投票获得的 Elo 评分。Elo 评分是一种相对排名系统，分数越高表示模型表现越好。该分数是动态变化的，反映了模型在当前竞争环境中的相对实力。
- **置信区间(95%)**：表示模型 Elo 评分的95%置信区间（例如：`+X/-Y`）。这个区间越小，表示模型的评分越稳定和可靠；反之，区间越大可能意味着数据量不足或模型表现波动较大。它提供了对评分准确性的量化评估。
- **票数**：该模型在竞技场中收到的总投票数量。投票数越多，通常意味着其评分的统计可靠性越高。
- **服务商**：提供该模型的组织或公司。
- **许可协议**：模型的许可协议类型，例如专有 (Proprietary)、Apache 2.0、MIT 等。
- **知识截止日期**：模型训练数据的知识截止日期，表示模型对该日期之后事件的了解程度。
- **链接**：指向模型相关信息或试用页面的链接。

## 数据来源与更新频率

本数据由 [fboulnois/llm-leaderboard-csv](https://github.com/fboulnois/llm-leaderboard-csv) 项目自动生成并提供，该项目从 [lmarena.ai](https://lmarena.ai/) 获取并处理数据。此排行榜由 GitHub Actions **每隔6小时**自动更新一次（具体频率取决于您的工作流配置）。

## 免责声明

请注意，本报告仅作为参考。排行榜数据是动态变化的，并基于特定时间段内用户在 Chatbot Arena 上的偏好投票。数据的完整性和准确性取决于上游数据源及 `fboulnois/llm-leaderboard-csv` 项目的更新和处理。不同模型可能采用不同的许可协议，使用时请参考模型提供商的说明。
'''
        
        # 确保输出目录存在
        os.makedirs(os.path.dirname(output_file_path), exist_ok=True)
        
        # 比较内容，如果不同才写入
        current_hash = get_file_hash(output_file_path)
        new_hash = hashlib.md5(markdown_content.encode('utf-8')).hexdigest()

        if current_hash == new_hash:
            logging.info('No changes detected. Skipping file write.')
            return False # 表示没有文件内容变化，不需要提交
        else:
            with open(output_file_path, 'w', encoding='utf-8') as f:
                f.write(markdown_content)
            logging.info(f'Successfully updated {output_file_path}')
            return True # 表示文件内容已更新，需要提交

    except requests.exceptions.RequestException as e:
        logging.error(f'Error downloading CSV: {e}')
        return False
    except Exception as e:
        logging.error(f'An unexpected error occurred: {e}')
        return False

if __name__ == "__main__":
    if update_leaderboard_data():
        exit(0) # 成功更新
    else:
        exit(1) # 未更新或发生错误
