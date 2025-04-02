import json
import os
from student import Student


class StudentManager:
    """学生管理类"""

    def __init__(self, filename="students.json"):
        self.filename = filename
        self.students = self.load_students()

    def load_students(self):
        """从 JSON 文件加载学生数据"""
        if not os.path.exists(self.filename):
            return []  # 文件不存在，则返回空列表
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                data = json.load(f)
                return [Student.from_dict(student) for student in data]
        except (json.JSONDecodeError, FileNotFoundError):
            return []

    def save_students(self):
        """保存学生数据到 JSON 文件"""
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump([student.to_dict() for student in self.students], f, ensure_ascii=False, indent=4)

    def add_student(self):
        """添加学生"""
        try:
            student_id = input("请输入学号：")
            name = input("请输入姓名：")
            age = int(input("请输入年龄："))
            score = float(input("请输入成绩："))

            student = Student(student_id, name, age, score)
            self.students.append(student)
            self.save_students()
            print(f"✅ 学生 {name} 添加成功！")
        except ValueError:
            print("❌ 年龄或成绩输入错误，请输入正确的数字！")

    def remove_student(self):
        """删除学生"""
        student_id = input("请输入要删除的学号：")
        self.students = [s for s in self.students if s.student_id != student_id]
        self.save_students()
        print("✅ 学生删除成功！")

    def update_student(self):
        """修改学生信息"""
        student_id = input("请输入要修改的学号：")
        for student in self.students:
            if student.student_id == student_id:
                try:
                    student.name = input("请输入新姓名：")
                    student.age = int(input("请输入新年龄："))
                    student.score = float(input("请输入新成绩："))
                    self.save_students()
                    print("✅ 学生信息更新成功！")
                    return
                except ValueError:
                    print("❌ 年龄或成绩输入错误！")
                    return
        print("❌ 未找到该学生！")

    def list_students(self):
        """显示所有学生信息"""
        if not self.students:
            print("暂无学生数据！")
        else:
            print("\n📋 学生列表：")
            for student in self.students:
                print(f"学号：{student.student_id} | 姓名：{student.name} | 年龄：{student.age} | 成绩：{student.score}")

    def run(self):
        """主菜单"""
        while True:
            print("\n📚 学生管理系统")
            print("1. 添加学生")
            print("2. 删除学生")
            print("3. 修改学生信息")
            print("4. 显示所有学生")
            print("5. 退出")
            choice = input("请选择操作：")

            if choice == "1":
                self.add_student()
            elif choice == "2":
                self.remove_student()
            elif choice == "3":
                self.update_student()
            elif choice == "4":
                self.list_students()
            elif choice == "5":
                print("📌 退出系统！")
                break
            else:
                print("❌ 请输入正确的选项！")


if __name__ == "__main__":
    manager = StudentManager()
    manager.run()
