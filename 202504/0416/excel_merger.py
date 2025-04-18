#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Excel工作表合并工具
功能：
1. 通过弹窗选择Excel文件
2. 读取所有工作表
3. 合并为一个DataFrame
4. 保存为新的Excel文件
"""

import pandas as pd
import os
import tkinter as tk
from tkinter import filedialog, messagebox
from typing import Optional, List, Dict, Any


def select_file() -> Optional[str]:
    """
    通过文件对话框选择Excel文件
    
    返回:
        Optional[str]: 选择的文件路径，如果用户取消则返回None
    """
    # 创建Tkinter根窗口
    root = tk.Tk()
    root.withdraw()  # 隐藏主窗口
    
    # 打开文件选择对话框
    file_path = filedialog.askopenfilename(
        title="选择Excel文件",
        filetypes=[("Excel文件", "*.xlsx *.xls"), ("所有文件", "*.*")]
    )
    
    return file_path if file_path else None


def select_save_file() -> Optional[str]:
    """
    通过文件对话框选择保存位置
    
    返回:
        Optional[str]: 选择的保存路径，如果用户取消则返回None
    """
    # 创建Tkinter根窗口
    root = tk.Tk()
    root.withdraw()  # 隐藏主窗口
    
    # 打开文件保存对话框
    file_path = filedialog.asksaveasfilename(
        title="选择保存位置",
        defaultextension=".xlsx",
        filetypes=[("Excel文件", "*.xlsx"), ("所有文件", "*.*")]
    )
    
    return file_path if file_path else None


def read_excel_sheets(file_path: str) -> Dict[str, pd.DataFrame]:
    """
    读取Excel文件中的所有工作表
    
    参数:
        file_path (str): Excel文件路径
        
    返回:
        Dict[str, pd.DataFrame]: 工作表名称和对应的DataFrame字典
    """
    # 读取所有工作表
    excel_file = pd.ExcelFile(file_path)
    sheet_names = excel_file.sheet_names
    
    print(f"\n发现 {len(sheet_names)} 个工作表:")
    for i, name in enumerate(sheet_names, 1):
        print(f"  {i}. {name}")
    
    # 读取每个工作表
    sheets_data = {}
    for sheet_name in sheet_names:
        df = pd.read_excel(file_path, sheet_name=sheet_name)
        sheets_data[sheet_name] = df
        print(f"\n工作表 '{sheet_name}' 的信息:")
        print(f"  行数: {df.shape[0]}")
        print(f"  列数: {df.shape[1]}")
        print(f"  列名: {', '.join(df.columns)}")
    
    return sheets_data


def merge_dataframes(sheets_data: Dict[str, pd.DataFrame]) -> pd.DataFrame:
    """
    合并所有DataFrame
    
    参数:
        sheets_data (Dict[str, pd.DataFrame]): 工作表数据字典
        
    返回:
        pd.DataFrame: 合并后的DataFrame
    """
    # 获取所有DataFrame
    dataframes = list(sheets_data.values())
    
    # 检查是否所有DataFrame具有相同的列
    first_df = dataframes[0]
    all_same_columns = all(df.columns.equals(first_df.columns) for df in dataframes[1:])
    
    if all_same_columns:
        print("\n所有工作表具有相同的列结构，直接合并...")
        # 添加工作表名称列
        for sheet_name, df in sheets_data.items():
            df['工作表'] = sheet_name
        
        # 合并所有DataFrame
        merged_df = pd.concat(dataframes, ignore_index=True)
    else:
        print("\n工作表具有不同的列结构，尝试合并共同列...")
        # 找出所有共同的列
        common_columns = set.intersection(*[set(df.columns) for df in dataframes])
        print(f"共同列: {', '.join(common_columns)}")
        
        # 添加工作表名称列
        for sheet_name, df in sheets_data.items():
            df['工作表'] = sheet_name
        
        # 只保留共同列进行合并
        dataframes = [df[list(common_columns) + ['工作表']] for df in dataframes]
        merged_df = pd.concat(dataframes, ignore_index=True)
    
    return merged_df


def save_merged_data(merged_df: pd.DataFrame, save_path: str) -> None:
    """
    保存合并后的数据
    
    参数:
        merged_df (pd.DataFrame): 合并后的DataFrame
        save_path (str): 保存路径
    """
    # 保存为Excel文件
    merged_df.to_excel(save_path, index=False)
    print(f"\n合并后的数据已保存至: {save_path}")
    print(f"总行数: {merged_df.shape[0]}")
    print(f"总列数: {merged_df.shape[1]}")


def main():
    """主函数"""
    print("===== Excel工作表合并工具 =====")
    
    # 选择输入文件
    input_file = select_file()
    if not input_file:
        print("未选择文件，程序退出")
        return
    
    # 检查文件是否存在
    if not os.path.exists(input_file):
        messagebox.showerror("错误", f"文件 '{input_file}' 不存在")
        print(f"错误: 文件 '{input_file}' 不存在")
        return
    
    try:
        # 读取所有工作表
        sheets_data = read_excel_sheets(input_file)
        
        # 合并DataFrame
        merged_df = merge_dataframes(sheets_data)
        
        # 选择保存位置
        save_path = select_save_file()
        if not save_path:
            print("未选择保存位置，程序退出")
            return
        
        # 保存合并后的数据
        save_merged_data(merged_df, save_path)
        
        print("\n处理完成!")
        
    except Exception as e:
        messagebox.showerror("错误", f"处理过程中出现错误: {str(e)}")
        print(f"错误: {str(e)}")


if __name__ == "__main__":
    main() 