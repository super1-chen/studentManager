class Student:
    def __init__(self, name: str, gender: str, phone_num: str) -> str:
        self.name = name
        self.gender = gender
        self.phone_num = phone_num
    
    def is_match(self, search: str):
        return self.name == search or self.phone_num == search
      
    def __str__(self):
        return f"学生信息, 姓名: {self.name}, 性别: {self.gender}, 手机号: {self.phone_num}"

    def to_info(self) -> str:
        return ",".join([self.name, self.gender, self.phone_num])