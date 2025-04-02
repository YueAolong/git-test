from file_util import main_read_file, write_file

# 读取文件（文件不存在时不会崩溃）
content = main_read_file("data.txt")
if content:  # 只有当内容非空时才继续操作
    print("文件内容：", content)

# 写入文件（验证是否成功）
success = write_file("output.txt", "新内容")
if success:
    print("文件保存成功！")
