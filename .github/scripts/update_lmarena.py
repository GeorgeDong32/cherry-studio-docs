import os
import requests
import pandas as pd
from datetime import datetime
import logging
import hashlib

# 配置日志记录
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def get_content_hash(content):
    """
    计算内容的哈希值
    """
    return hashlib.md5(content.encode('utf-8')).hexdigest()

def read_existing_content(file_path):
    """
    读取现有文件内容
    """
    try:
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as f:
                return f.read()
        return None
    except Exception as e:
        logging.error(f"Error reading existing file: {e}")
        return None

def fetch_data():
    """
    从 LLM Arena API 获取排名数据
    """
    api_url = "https://w89ie3.laf.dev/rank_search"
    api_key = os.environ.get('LMARENA_KEY')
    
    if not api_key:
        logging.error("API key not found in environment variables")
        return None, []
    
    headers = {
        'Authorization': api_key,
        'User-Agent': 'GitHub-Action-Bot'
    }
    
    try:
        logging.info("Fetching data from API...")
        response = requests.get(api_url, headers=headers, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        if data['success'] and 'data' in data and 'records' in data['data']:
            update_time = data.get('update_time', '')
            records = data['data']['records']
            logging.info(f"Successfully fetched {len(records)} records")
            return update_time, records
        else:
            logging.error(f"Invalid data format in API response: {data}")
            return None, []
            
    except requests.exceptions.Timeout:
        logging.error("API request timed out")
        return None, []
    except requests.exceptions.RequestException as e:
        logging.error(f"Request failed: {e}")
        return None, []
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        return None, []

def create_markdown_content(records, update_time):
    """
    生成Markdown格式的内容
    """
    try:
        if not records:
            logging.error("No records to process")
            return None

        columns = [
            'rank_ub',    # Upper Bound 排名
            'rank_sc',    # Style-controlled 排名
            'model',      # 模型名称
            'arena_score',# 竞技场分数
            'ci',         # 置信区间
            'votes',      # 投票数
            'org'         # 组织机构
        ]
        
        df = pd.DataFrame(records)[columns]
        
        # 格式化数值列
        df['arena_score'] = df['arena_score'].round(2)
        df['votes'] = df['votes'].apply(lambda x: f"{x:,}")
        
        df.columns = [
            '排名(UB)',
            '排名(StyleCtrl)',
            '模型名',
            '分数',
            '置信区间',
            '票数',
            '服务商'
        ]
        
        table = df.to_markdown(index=False)
        
        content = f"""# LLM Arena 排行榜

> 排名更新时间: {update_time}

{table}

## 说明

- 排名(UB)：基于 Bradley-Terry 模型的上界排名
- 排名(StyleCtrl)：考虑对话风格的样式控制排名
- 置信区间：模型表现的置信区间
- 分数：基于模型性能的竞技场得分

## 数据来源

- 数据来自 [lmarena.ai](https://lmarena.ai/)


"""
        return content
        
    except Exception as e:
        logging.error(f"Error creating markdown content: {e}")
        return None

def update_file():
    """
    主函数：获取数据并更新文件
    """
    file_path = "other/model_rank/lmarena.md"
    
    try:
        # 获取数据
        update_time, records = fetch_data()
        if not records:
            logging.error("No data to update")
            return False
        
        # 生成新内容
        new_content = create_markdown_content(records, update_time)
        if not new_content:
            logging.error("Failed to generate content")
            return False
        
        # 读取现有内容
        existing_content = read_existing_content(file_path)
        
        # 比较内容（忽略时间戳差异）
        if existing_content:
            old_hash = get_content_hash(''.join(existing_content.split('\n')[:-2]))
            new_hash = get_content_hash(''.join(new_content.split('\n')[:-2]))
            
            if old_hash == new_hash:
                logging.info("Content unchanged, skipping update")
                return True
        
        # 写入文件
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)
            
        logging.info(f"Successfully updated {file_path}")
        return True
        
    except Exception as e:
        logging.error(f"Error in update process: {e}")
        return False

if __name__ == "__main__":
    try:
        success = update_file()
        if not success:
            raise Exception("Update process failed")
    except Exception as e:
        logging.error(f"Script failed: {e}")
        raise
