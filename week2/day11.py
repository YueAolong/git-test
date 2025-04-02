# # # # # import os
# # # # # print(os.getcwd())
# # # # #
# # # # #
# # # # # from datetime import datetime
# # # # # print(datetime.now())
# # # # #
# # # # # import sys as system
# # # # # print(system.path)
# # # # #
# # # # #
# # # # # import random
# # # # # print(dir(random))
# # # #
# # # #
# # # # import os
# # # # current_dir = os.getcwd()
# # # # print('当前目录：', current_dir)
# # # #
# # # # if not os.path.exists('test_dir'):
# # # #     os.mkdir('test_dir')
# # # #     print('文件夹创建成功')
# # # #
# # # # print('目录内容：', os.listdir())
# # # #
# # # #
# # # # from datetime import datetime, timedelta
# # # #
# # # # now = datetime.now()
# # # # print('当前时间：', now.strftime('%Y-%m-%d %H:%M:%S'))
# # # #
# # # # tomorrow = now + timedelta(days=1)
# # # # print('明天此时：', tomorrow)
# # # #
# # # # date_str = '2024-05-20'
# # # # date_obj = datetime.strptime(date_str, '%Y-%m-%d')
# # # # print('转换后的时间对象：', date_obj)
# # # #
# # # # import random
# # # #
# # # # print('1-10随机数：', random.randint(1, 10))
# # # #
# # # # fruits = ['苹果', '香蕉', '橙子']
# # # # print('随机水果：', random.choice(fruits))
# # # # random.shuffle(fruits)
# # # # print('打乱后的列表：', fruits)
# # # #
# # # #
# # # # import sys
# # # #
# # # # print('脚本名称：', sys.argv[0])
# # # # print('传入参数：', sys.argv[1:])
# # # #
# # # # if len(sys.argv) < 2:
# # # #     print('错误：缺少参数')
# # # #     sys.exit(1)
# # #
# # # import os
# # # import shutil
# # #
# # # desktop = os.path.join(os.path.expanduser('~'), 'Desktop')
# # #
# # # for filename in os.listdir(desktop):
# # #     src_path = os.path.join(desktop, filename)
# # #
# # #     if os.path.isfile(src_path):
# # #         ext = filename.split('.')[-1].lower()
# # #         target_dir = os.path.join(desktop, ext + '_Files')
# # #
# # #         if not os.path.exists(target_dir):
# # #             os.mkdir(target_dir)
# # #
# # #             shutil.move(src_path, os.path.join(target_dir, filename))
# # #
# # import os
# # import shutil
# #
# # desktop = os.path.join(os.path.expanduser("~"), "Desktop")  # 获取桌面路径
# #
# # # 遍历桌面上的文件夹
# # for folder in os.listdir(desktop):
# #     folder_path = os.path.join(desktop, folder)
# #
# #     # 仅处理扩展名分类的文件夹（如 pdf_Files, jpg_Files）
# #     if os.path.isdir(folder_path) and folder.endswith("_Files"):
# #         for filename in os.listdir(folder_path):
# #             src_path = os.path.join(folder_path, filename)  # 源文件路径
# #             dest_path = os.path.join(desktop, filename)  # 目标路径（还原到桌面）
# #
# #             # 处理同名文件，避免覆盖
# #             count = 1
# #             while os.path.exists(dest_path):
# #                 name, ext = os.path.splitext(filename)
# #                 new_filename = f"{name}_restored_{count}{ext}"
# #                 dest_path = os.path.join(desktop, new_filename)
# #                 count += 1
# #
# #             # 移动文件回桌面
# #             shutil.move(src_path, dest_path)
# #             print(f"还原 {filename} → {dest_path}")
# #
# #         # 移除空的分类文件夹
# #         os.rmdir(folder_path)
# #         print(f"删除空文件夹: {folder_path}")
# #
# # print("✅ 还原完成！所有文件已移动回桌面")
#
#
# import random
# import string
#
# def generate_password(length=8):
#     chars = string.ascii_letters + string.digits + '!@#$%'
#     password = [random.choice(chars) for _ in range(length)]
#     random.shuffle(password)
#     return ''.join(password)
#
# print('随机密码：', generate_password(12))

# import os
# from datetime import datetime
#
# def backup_file(filepath):
#     backup_dir = 'backups'
#     if not os.path.exists(backup_dir):
#         os.mkdir(backup_dir)
#
#     timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
#     filename = os.path.basename(filepath)
#     new_name = f'{filename.split(",")[0]}_{timestamp}.{filename.split(".")[1]}'
#
#     target_path = os.path.join(backup_dir, new_name)
#     with open(filepath, 'rb') as src, open(target_path, 'wb') as dst:
#         dst.write(src.read())
#     print(f'备份成功：{target_path}')
#
# backup_file('text.txt')


import os
from datetime import datetime

def backup_file(filepath):
    if not os.path.exists(filepath):
        print('错误：文件不存在')
        return
    backup_dir = 'backups'
    os.makedirs(backup_dir, exist_ok=True)

    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    name, ext = os.path.splitext(os.path.basename(filepath))
    new_name = f'{name}_{timestamp}{ext}'
    target_path = os.path.join(backup_dir, new_name)

    with open(filepath, 'rb') as src, open(target_path, 'wb') as dst:
        dst.write(src.read())
    print(f'备份成功：{target_path}')

file_to_backup = input('请输入要备份的文件路径：')
backup_file(file_to_backup)