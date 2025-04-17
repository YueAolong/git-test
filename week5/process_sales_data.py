import pandas as pd
import numpy as np
from tqdm import tqdm
import os

def load_excel_file(file_path):
    """加载Excel文件并进行数据验证"""
    try:
        # 读取Excel文件
        df = pd.read_excel(file_path)
        
        # 数据验证：跳过金额为负数的行
        invalid_rows = df[df['销售额'] < 0]
        if not invalid_rows.empty:
            print(f"警告：在{os.path.basename(file_path)}中发现{len(invalid_rows)}行负数销售额，已跳过")
            df = df[df['销售额'] >= 0]
        
        # 添加城市列
        city_name = os.path.basename(file_path).split('_')[1].split('.')[0]
        df['城市'] = city_name
        
        return df
    except Exception as e:
        print(f"读取文件{file_path}时出错: {e}")
        return None

def process_sales_data():
    """处理销售数据并生成汇总结果"""
    # 检查文件是否存在
    beijing_file = 'sales_北京.xlsx'
    shanghai_file = 'sales_上海.xlsx'
    
    if not os.path.exists(beijing_file) or not os.path.exists(shanghai_file):
        print("错误：找不到所需的Excel文件，请确保sales_北京.xlsx和sales_上海.xlsx在当前目录中")
        return
    
    print("开始处理销售数据...")
    
    # 加载数据
    print("正在加载北京销售数据...")
    beijing_data = load_excel_file(beijing_file)
    if beijing_data is None:
        return
    
    print("正在加载上海销售数据...")
    shanghai_data = load_excel_file(shanghai_file)
    if shanghai_data is None:
        return
    
    # 合并数据
    print("正在合并数据...")
    combined_data = pd.concat([beijing_data, shanghai_data], ignore_index=True)
    
    # 按产品类别和城市计算总销售额
    print("正在计算汇总数据...")
    summary_data = combined_data.groupby(['产品类别', '城市'])['销售额'].sum().reset_index()
    
    # 创建数据透视表
    pivot_data = summary_data.pivot(index='产品类别', columns='城市', values='销售额').reset_index()
    
    # 计算总计
    pivot_data['总计'] = pivot_data['北京'] + pivot_data['上海']
    
    # 格式化销售额（保留两位小数）
    for col in ['北京', '上海', '总计']:
        pivot_data[col] = pivot_data[col].round(2)
    
    # 保存结果
    print("正在保存结果...")
    with pd.ExcelWriter('sales_汇总.xlsx', engine='openpyxl') as writer:
        pivot_data.to_excel(writer, sheet_name='分析结果', index=False)
        
        # 添加原始数据表
        combined_data.to_excel(writer, sheet_name='原始数据', index=False)
    
    print("处理完成！结果已保存到 sales_汇总.xlsx")
    
    # 显示结果预览
    print("\n汇总结果预览：")
    print(pivot_data)

if __name__ == "__main__":
    process_sales_data() 