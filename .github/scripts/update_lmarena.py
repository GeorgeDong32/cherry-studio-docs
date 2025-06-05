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
    with open(file_path, 'rb') as f:
        return hashlib.md5(f.read()).hexdigest()

def update_leaderboard_data():
    """
    从 fboulnois/llm-leaderboard-csv 项目下载排行榜数据，
    处理后生成 Markdown 文件。
    """
    # 最新 CSV 文件的下载 URL
    # 建议定期检查 https://github.com/fboulnois/llm-leaderboard-csv/releases 确保 URL 最新
    csv_url = 'https://github.com/fboulnois/llm-leaderboard-csv/releases/latest/download/lmsys_chatbot_arena_leaderboard.csv'
    
    # 输出 Markdown 文件的路径
    # 请确保此路径与您的 GitHub Actions 工作流中的 `output_file_path` 一致
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
        # 请注意：这里的列名必须与CSV文件中的实际列名完全匹配
        # 如果CSV文件结构发生变化，您可能需要更新这些列名
        required_columns = [
            'arena_rank_ub',    # Upper Bound 排名
            'arena_rank_sc',    # Style-controlled 排名
            'model_name',       # 模型名称
            'arena_elo',        # 竞技场分数
            'elo_ci',           # 置信区间
            'votes',            # 投票数
            'organization'      # 组织机构
        ]

        # 过滤出存在的列，避免因为CSV缺少列而报错
        available_columns = [col for col in required_columns if col in df.columns]
        if len(available_columns) != len(required_columns):
            logging.warning(f'Not all required columns found in CSV. Missing: {set(required_columns) - set(available_columns)}')
            # 如果缺少关键列，可以选择退出或继续（这里选择继续，但可能生成不完整数据）
            df = df[available_columns]
        else:
            df = df[required_columns]

        # 重命名列以便在 Markdown 中显示
        df.columns = [
            '排名(UB)',
            '排名(StyleCtrl)',
            '模型名',
            '分数',
            '置信区间',
            '票数',
            '服务商'
        ]
        
        # 格式化数值列
        df['分数'] = df['分数'].round(2)
        df['置信区间'] = df['置信区间'].round(2) # ELO 置信区间通常也是小数
        df['票数'] = df['票数'].apply(lambda x: f'{x:,}') # 添加千位分隔符

        # 获取当前 UTC 时间作为更新时间
        update_time = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC')

        # 生成 Markdown 内容
        markdown_content = f'''# LLM Arena 排行榜

> 数据更新时间: {update_time}

{df.to_markdown(index=False)}

## 说明

- 排名(UB)：基于 Bradley-Terry 模型的上界排名
- 排名(StyleCtrl)：考虑对话风格的样式控制排名
- 分数：基于模型性能的竞技场得分 (Elo 分数)
- 置信区间：模型表现的置信区间 (+/- ELO 值)
- 票数：模型收到的总投票数

## 数据来源

- 本数据由 [fboulnois/llm-leaderboard-csv](https://github.com/fboulnois/llm-leaderboard-csv) 项目自动生成并提供，该项目从 [lmarena.ai](https://lmarena.ai/) 获取并处理数据。
'''
        
        # 确保输出目录存在
        os.makedirs(os.path.dirname(output_file_path), exist_ok=True)
        
        # 比较内容，如果不同才写入
        # 使用哈希值比较，更稳健
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
    # 如果脚本成功更新了文件，则返回True，否则返回False
    # GitHub Actions 可以通过此 exit code 判断是否需要执行后续的 commit 步骤
    if update_leaderboard_data():
        exit(0) # 成功更新
    else:
        exit(1) # 未更新或发生错误
