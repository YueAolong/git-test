def read_file(filename):
    """读取文件内容"""
    with open(filename, 'r', encoding='utf-8') as f:
        return f.read()


def write_file(filename, content):
    """写入文件"""
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
