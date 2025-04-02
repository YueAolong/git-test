#
# import sqlite3
#
# conn = sqlite3.connect('mydatabase.db')
# cursor = conn.cursor()
#
# # 每次运行代码前清空表，防止数据重复
# cursor.execute("DELETE FROM books")
# conn.commit()
#
# cursor.execute('''CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title TEXT, author TEXT, price REAL)''')
# conn.commit()
#
# cursor.execute('INSERT INTO books (title, author, price) VALUES (?, ?, ?)', ('Python入门', '张三', 49.9))
# conn.commit()
#
# books = [
#     ('Flask Web开发', '李四', 69.9),
#     ('数据分析实战', '王五', 59.9)
# ]
# cursor.executemany('INSERT INTO books (title, author, price) VALUES (?, ?, ?)', books)
# conn.commit()
#
# cursor.execute('SELECT * FROM books')
# all_books = cursor.fetchall()
# print('所有书籍：')
# for book in all_books:
#     print(book)
#
# cursor.execute('SELECT title, price FROM books WHERE price > 50')
# expensive_books = cursor.fetchall()
# print('\n价格超过50的书籍：')
# for book in expensive_books:
#     print(f'{book[0]} - ￥{book[1]}')
#
# cursor.execute('UPDATE books SET price = ? WHERE id = ?', (55.0, 1))
# conn.commit()
# print('更新成功！')
#
# cursor.execute('DELETE FROM books WHERE id = 3')
# conn.commit()
# print('删除成功！')
#
# conn.close()
# from sqlalchemy import create_engine, Column, Integer, String, Float
# from sqlalchemy.orm import declarative_base
#
# Base = declarative_base()
#
#
# class Book(Base):
#     __tablename__ = 'books'
#     id = Column(Integer, primary_key=True)
#     title = Column(String(50))
#     author = Column(String(30))
#     price = Column(Float)
#
#
# engine = create_engine('sqlite:///mydatabase.db')
# Base.metadata.create_all(engine)
#
# from sqlalchemy.orm import sessionmaker
#
# Session = sessionmaker(bind=engine)
# session = Session()
#
# new_book = Book(title='西游记', author='吴承恩', price=50)
# session.add(new_book)
# session.commit()
#
# books = session.query(Book).filter(Book.price > 40).all()
# for book in books:
#     print(f'{book.title} - ￥{book.price}')
import sqlite3
from typing import List, Tuple, Optional


# 初始化数据库
def init_db():
    conn = sqlite3.connect('books.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS books
                      (id INTEGER PRIMARY KEY AUTOINCREMENT,
                       title TEXT NOT NULL,
                       author TEXT,
                       price REAL)''')
    conn.commit()
    conn.close()


# 添加新书
def add_book(title: str, author: str, price: float) -> bool:
    try:
        conn = sqlite3.connect('books.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO books (title, author, price) VALUES (?, ?, ?)",
                       (title, author, price))
        conn.commit()
        return True
    except sqlite3.Error as e:
        print(f"添加书籍失败: {e}")
        return False
    finally:
        conn.close()


# 根据书名查询书籍
def search_book(title: str) -> List[Tuple]:
    try:
        conn = sqlite3.connect('books.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM books WHERE title LIKE ?", ('%' + title + '%',))
        return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"查询失败: {e}")
        return []
    finally:
        conn.close()


# 显示所有书籍
def list_all_books() -> List[Tuple]:
    try:
        conn = sqlite3.connect('books.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM books ORDER BY title")
        return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"获取书籍列表失败: {e}")
        return []
    finally:
        conn.close()


# 修改书籍价格
def update_book_price(book_id: int, new_price: float) -> bool:
    try:
        conn = sqlite3.connect('books.db')
        cursor = conn.cursor()
        cursor.execute("UPDATE books SET price = ? WHERE id = ?",
                       (new_price, book_id))
        conn.commit()
        return cursor.rowcount > 0
    except sqlite3.Error as e:
        print(f"更新价格失败: {e}")
        return False
    finally:
        conn.close()


# 删除书籍
def delete_book(book_id: int) -> bool:
    try:
        conn = sqlite3.connect('books.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM books WHERE id = ?", (book_id,))
        conn.commit()
        return cursor.rowcount > 0
    except sqlite3.Error as e:
        print(f"删除书籍失败: {e}")
        return False
    finally:
        conn.close()


# 获取书籍详情
def get_book_details(book_id: int) -> Optional[Tuple]:
    try:
        conn = sqlite3.connect('books.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM books WHERE id = ?", (book_id,))
        return cursor.fetchone()
    except sqlite3.Error as e:
        print(f"获取书籍详情失败: {e}")
        return None
    finally:
        conn.close()


# 用户界面
def main_menu():
    print("\n图书管理系统")
    print("1. 添加新书")
    print("2. 搜索书籍")
    print("3. 显示所有书籍")
    print("4. 修改书籍价格")
    print("5. 删除书籍")
    print("0. 退出")


def main():
    init_db()

    while True:
        main_menu()
        choice = input("请选择操作: ")

        if choice == '1':
            print("\n添加新书")
            title = input("书名: ")
            author = input("作者: ")
            try:
                price = float(input("价格: "))
                if add_book(title, author, price):
                    print("添加成功!")
                else:
                    print("添加失败!")
            except ValueError:
                print("价格必须是数字!")

        elif choice == '2':
            print("\n搜索书籍")
            title = input("输入书名(支持模糊搜索): ")
            books = search_book(title)
            if books:
                print("\n搜索结果:")
                for book in books:
                    print(f"ID: {book[0]}, 书名: {book[1]}, 作者: {book[2]}, 价格: {book[3]}")
            else:
                print("未找到匹配的书籍")

        elif choice == '3':
            print("\n所有书籍列表:")
            books = list_all_books()
            if books:
                for book in books:
                    print(f"ID: {book[0]}, 书名: {book[1]}, 作者: {book[2]}, 价格: {book[3]}")
            else:
                print("书库为空")

        elif choice == '4':
            print("\n修改书籍价格")
            book_id = input("输入要修改的书籍ID: ")
            try:
                book_id = int(book_id)
                book = get_book_details(book_id)
                if book:
                    print(f"当前信息 - 书名: {book[1]}, 价格: {book[3]}")
                    new_price = float(input("输入新价格: "))
                    if update_book_price(book_id, new_price):
                        print("价格更新成功!")
                    else:
                        print("更新失败!")
                else:
                    print("未找到该ID的书籍")
            except ValueError:
                print("ID和价格必须是数字!")

        elif choice == '5':
            print("\n删除书籍")
            book_id = input("输入要删除的书籍ID: ")
            try:
                book_id = int(book_id)
                if delete_book(book_id):
                    print("删除成功!")
                else:
                    print("删除失败或书籍不存在")
            except ValueError:
                print("ID必须是数字!")

        elif choice == '0':
            print("感谢使用图书管理系统!")
            break

        else:
            print("无效选择，请重新输入!")


if __name__ == "__main__":
    main()

