import os
from typing import List
from student import Student

class MSystem:
    def __init__(self, data_path: str):
        self.data_path = data_path
        self.data: List[Student] = self.load_data(data_path)

    def load_data(self, data_path: str):
        if not os.path.exists(data_path):
            return []
        data = []
        print("加载数据.....")
        with open(data_path, "r") as fp:
            for item in fp.readlines():
                if not item:
                    continue
                data.append(self.load_student(item))
        return data
    def load_student(self, data_info: str) -> Student:
        if not data_info:
            return
        data_info = data_info.strip()
        name, gender, phone_num = data_info.split(",")
        return Student(name, gender, phone_num)
    
    def save_data(self):
        with open(self.data_path, "w") as fp:
            for student in self.data:
                fp.write(student.to_info() + "\n")
        print("保存数据成功")
        
    def find_student(self, search):
        students = []
        for s in self.data:        
            if s.is_match(search):
                students.add(s)
        return students
    
    def delete_student(self, idx: int):
        self.data.pop(idx-1)
        print("删除成功")
    
    def add_student(self, name, gender, phone_num):
        s = Student(name, gender, phone_num)
        self.data.append(s)
        print("添加成功")
        
    def modify_student(self, idx: int, name: str="", gender: str="", mobile: str=""):
        student = self.data[idx-1]
        if name:
            student.name = name
        if gender:
            student.gender = gender
        if mobile:
            student.name = mobile
        print("修改成功")
    def list_students(self):
        print("学生列表:")
        for idx, student in enumerate(self.data):
            print(idx+1, student)