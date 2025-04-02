# file = open('demo1.tet', 'w', encoding='utf-8')
#
# file.write('第一行内容\n')
# file.write('第二行内容')
#
# file.close
#
# with open('demo2.tet', 'w', encoding='utf-8') as file:
#     file.write('使用with语句更安全！')
#
# with open('demo.tet', 'r', encoding='utf-8') as file:
#     content = file.read()
# print(content)
#
# with open('demo1.tet', 'r', encoding='utf-8') as file:
#     lines = file.readlines()
# print(lines)

# def save_contacts(contacts):
#     with open('contacts.txt', 'w', encoding='utf-8') as file:
#         for name, phone in contacts.items():
#             file.write(f'{name},{phone}\n')
#
#
# contacts = {'小明': '18637247945', '客服': '10086'}
# save_contacts(contacts)


# def loading_contacts():
#     contacts = {}
#     try:
#         with open('contacts.txt', 'r', encoding='utf-8') as file:
#             for line in file:
#                 name, phone = line.strip().split(',')
#                 contacts[name] = phone
#     except FileNotFoundError:
#         print('通讯录文件不存在，将创建新文件')
#         return contacts
#
#
# contacts = loading_contacts()
# print('加载的联系人：', contacts)
# import os
#
# def load_contacts():
#     contacts = {}
#     filename = "contacts.txt"
#
#     if not os.path.exists(filename):
#         print("通讯录文件不存在，将创建新文件")
#         return contacts
#
#     try:
#         with open(filename, "r", encoding="utf-8") as file:
#             for line in file:
#                 parts = line.strip().split(",")
#                 if len(parts) == 2:
#                     name, phone = parts
#                     contacts[name] = phone
#                 else:
#                     print(f"忽略格式错误的行: {line.strip()}")
#     except Exception as e:
#         print(f"读取通讯录时出错: {e}")
#
#     return contacts
#
# # 使用示例
# contacts = load_contacts()
# print("加载的联系人：", contacts)


#
# with open('data.csv', 'w', encoding='utf-8') as file:
#     file.write('姓名，年龄,城市\n')
#     file.write('小明,18,北京\n')
#     file.write('小红,20,上海\n')
# # with open("data.csv", "w", encoding="utf-8") as file:
# #     file.write("姓名,年龄,城市\n")
# #     file.write("小明,18,北京\n")
# #     file.write("小红,20,上海\n")
#
# with open('data.csv', 'r', encoding='utf-8') as file:
#     header = file.readline()
#     for line in file:
#         name, age, city = line.strip().split(',')
#         print(f'{name} | {age}岁 | {city}')
# # 写入CSV
# with open("data.csv", "w", encoding="utf-8") as file:
#     file.write("姓名,年龄,城市\n")
#     file.write("小明,18,北京\n")
#     file.write("小红,20,上海\n")

# 读取CSV
# with open("data.csv", "r", encoding="utf-8") as file:
#     header = file.readline()  # 读取标题行
#     for line in file:
#         name, age, city = line.strip().split(",")
#         print(f"{name} | {age}岁 | {city}")
#
# import csv
#
#
# with open('data.csv', 'w', newline='', encoding='utf-8') as file:
#     writer = csv.writer(file)
#     writer.writerow(['姓名', '年龄', '城市'])
#     writer.writerow(['小明', '18', '北京'])
#     writer.writerow(['小红', '20', '上海'])
#
#
# with open('data.csv', 'r', encoding='utf-8') as file:
#     reader = csv.reader(file)
#     next(reader)
#     for row in reader:
#         print(f'{row[0]} | {row[1]}岁 | {row[2]}')

from datetime import datetime

def write_diary():
    content = input("请输入今天的日记：")
    filename = datetime.now().strftime("%Y-%m-%d") + ".txt"
    with open(filename, "a", encoding="utf-8") as file:
        file.write(content + "\n")

def read_diary():
    date = input("输入要查看的日期（格式：2024-05-20）：")
    try:
        with open(f"{date}.txt", "r", encoding="utf-8") as file:
            print(file.read())
    except FileNotFoundError:
        print("该日期的日记不存在")

# 主程序
while True:
    choice = input("1.写日记 2.读日记 3.退出：")
    if choice == "1":
        write_diary()
    elif choice == "2":
        read_diary()
    elif choice == "3":
        break