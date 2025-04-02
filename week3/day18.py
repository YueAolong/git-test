# import os
#
# # 查找当前目录下的 .txt 文件
# for filename in os.listdir('.'):
#     if filename.endswith('.txt'):
#         print('找到文本文件：', filename)
#
# # 检查 photos 目录是否存在
# photos_dir = 'photos'
# if not os.path.exists(photos_dir):
#     print(f"错误：目录 '{photos_dir}' 不存在")
# else:
#     # 获取 .jpg 文件，并按名称排序
#     jpg_files = sorted([f for f in os.listdir(photos_dir) if f.endswith('.jpg')])
#
#     counter = 1
#     for filename in jpg_files:
#         new_name = f'vacation_{counter}.jpg'
#         old_path = os.path.join(photos_dir, filename)
#         new_path = os.path.join(photos_dir, new_name)
#
#         # 避免文件名冲突
#         if os.path.exists(new_path):
#             print(f"警告：文件 {new_name} 已存在，跳过重命名 {filename}")
#         else:
#             os.rename(old_path, new_path)
#             print(f"已重命名：{filename} -> {new_name}")
#
#         counter += 1
#
#     print('重命名完成')
# import smtplib
# from email.mime.text import MIMEText
#
# sender = '2399364892@qq.com'
# receiver = 'lingxuan0309@qq.com'
# password = 'ootyqhxrfvspebab'
#
# message = MIMEText('I miss you', 'plain', 'utf-8')
# message['From'] = sender
# message['To'] = receiver
# message['Subject'] = '丢丢丢丢丢'
#
# try:
#     server = smtplib.SMTP_SSL('smtp.qq.com', 465)
#     server.login(sender, password)
#     server.sendmail(sender, [receiver], message.as_string())
#     print('邮件发送成功！')
# except Exception as e:
#     print('发送失败：', e)
# finally:
#     server.quit()
#
# import time
#
# def job():
#     print('定时任务执行：', time.strftime('%Y-%m-%d %H:%M:%S'))
#
# while True:
#     job()
#     time.sleep(60)
# import schedule
# import time
# import datetime
#
# def morning_task():
#     print(f"{datetime.datetime.now()} - 早上好！开始备份数据...")
#
# def night_task():
#     print(f"{datetime.datetime.now()} - 晚安！清理临时文件...")
#
# # 定时任务
# schedule.every().day.at("08:00").do(morning_task)
# schedule.every().day.at("22:21").do(night_task)
#
# print("定时任务已启动... 按 Ctrl+C 退出。")
#
# try:
#     while True:
#         schedule.run_pending()
#         time.sleep(1)  # 让 CPU 休息 1 秒，减少资源占用
# except KeyboardInterrupt:
#     print("定时任务已停止。")
# import os
# import zipfile
# import datetime
# import smtplib
# from email.mime.text import MIMEText
# import schedule
# import time
#
# def backup_folder():
#     # 配置参数
#     folder_to_backup = "重要文档"
#     backup_dir = "备份文件"
#     date_str = datetime.datetime.now().strftime("%Y%m%d")
#     zip_name = f"backup_{date_str}.zip"
#     zip_path = os.path.join(backup_dir, zip_name)
#
#     # 检查待备份目录是否存在
#     if not os.path.exists(folder_to_backup):
#         print(f"错误：目录 {folder_to_backup} 不存在，备份中止！")
#         return
#
#     # 创建备份目录
#     os.makedirs(backup_dir, exist_ok=True)
#
#     # 创建压缩包
#     with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:
#         for root, _, files in os.walk(folder_to_backup):
#             for file in files:
#                 file_path = os.path.join(root, file)
#                 zipf.write(file_path, os.path.relpath(file_path, folder_to_backup))
#
#     print(f"备份完成！文件名：{zip_name}")
#     send_email(f"今日备份成功：{zip_name}")
#
# def send_email(content):
#     sender_email = "2399364892@qq.com"
#     sender_password = "ootyqhxrfvspebab"
#     receiver_email = "yue_aolong@163.com"
#
#     msg = MIMEText(content, "plain", "utf-8")
#     msg["Subject"] = "系统备份通知"
#     msg["From"] = sender_email
#     msg["To"] = receiver_email
#
#     try:
#         server = smtplib.SMTP_SSL("smtp.qq.com", 465)
#         server.login(sender_email, sender_password)
#         server.sendmail(sender_email, [receiver_email], msg.as_string())
#         print("通知邮件已发送")
#     except Exception as e:
#         print("邮件发送失败:", e)
#     finally:
#         if "server" in locals():
#             server.quit()
#
# # 设置每天凌晨 1:00 备份
# schedule.every().day.at("22:36").do(backup_folder)
#
# print("定时任务已启动... 按 Ctrl+C 退出。")
#
# # 保持程序运行
# try:
#     while True:
#         schedule.run_pending()
#         time.sleep(60)  # 每分钟检查一次任务
# except KeyboardInterrupt:
#     print("定时任务已停止。")
import os
import shutil
import datetime
import exifread
import tkinter as tk
from tkinter import filedialog


def get_photo_date(photo_path):
    """ 获取照片的拍摄日期（EXIF），若无则使用文件修改时间 """
    try:
        with open(photo_path, "rb") as f:
            tags = exifread.process_file(f, stop_tag="EXIF DateTimeOriginal")
            date_taken = tags.get("EXIF DateTimeOriginal")

        if date_taken:
            date_str = str(date_taken).split(" ")[0].replace(":", "-")  # EXIF 格式：YYYY-MM-DD
            return date_str
    except Exception as e:
        print(f"⚠️ 解析 EXIF 失败（{photo_path}）：{e}")

    # 若 EXIF 读取失败，则使用文件修改时间
    mod_timestamp = os.path.getmtime(photo_path)
    return datetime.datetime.fromtimestamp(mod_timestamp).strftime("%Y-%m-%d")


def organize_photos(source_dir):
    """ 扫描目录下的图片并按日期整理 """
    if not os.path.exists(source_dir):
        print(f"❌ 错误：目录 '{source_dir}' 不存在！")
        return

    # 支持的图片格式（可扩展）
    image_extensions = {".jpg", ".jpeg", ".png", ".heic"}

    # 计数器
    moved_count = 0
    skipped_count = 0

    # 遍历目录下的所有文件
    for filename in os.listdir(source_dir):
        file_path = os.path.join(source_dir, filename)
        file_ext = os.path.splitext(filename)[1].lower()

        if os.path.isfile(file_path) and file_ext in image_extensions:
            date_folder = get_photo_date(file_path)
            target_folder = os.path.join(source_dir, date_folder)

            # 如果文件已经在正确的文件夹里，则跳过
            if os.path.dirname(file_path) == target_folder:
                skipped_count += 1
                continue

            # 创建日期文件夹（若不存在）
            os.makedirs(target_folder, exist_ok=True)

            try:
                # 移动文件
                shutil.move(file_path, os.path.join(target_folder, filename))
                print(f"✅ 已移动: {filename} → {target_folder}")
                moved_count += 1
            except Exception as e:
                print(f"❌ 移动失败（{filename}）：{e}")

    print(f"📂 照片整理完成！移动 {moved_count} 张，跳过 {skipped_count} 张。")

# 运行脚本（支持 GUI 选择文件夹）
root = tk.Tk()
root.withdraw()  # 隐藏主窗口
source_directory = filedialog.askdirectory(title="请选择照片所在目录")

if source_directory:
    organize_photos(source_directory)
else:
    print("❌ 未选择目录，程序退出")


