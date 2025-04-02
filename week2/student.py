import json


class Student:
    """学生类"""

    def __init__(self, student_id, name, age, score):
        self.student_id = student_id  # 学号
        self.name = name  # 姓名
        self.age = age  # 年龄
        self.score = score  # 成绩

    def to_dict(self):
        """将对象转换为字典，便于 JSON 序列化"""
        return {
            "student_id": self.student_id,
            "name": self.name,
            "age": self.age,
            "score": self.score,
        }

    @staticmethod
    def from_dict(data):
        """从字典创建 Student 对象"""
        return Student(data["student_id"], data["name"], data["age"], data["score"])
