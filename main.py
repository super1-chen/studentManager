from managerSystem import MSystem

DATA_PATH = "student.data"

def get_student_info():
    name = input("姓名: ")
    gender = input("性别: ")
    phone_num = input("电话: ")
    return name, gender, phone_num

def main():
    print_help()
    management = MSystem(DATA_PATH)
    support_cmd = list("admflsq")
    while True:
        cmd = input("请输入你的指令: ")
        # 主要部分
        # 判断命令合法性
        if cmd not in support_cmd:
            print("请输入正确的命令")
        # list
        if cmd == "l":
            management.list_students()
            continue
        # find
        if cmd == "f":
            search = input("输入要查询学生的名字或者手机号码: ")
            students = management.find_student(search)
            if students:
                print("学生信息如下")
                for s in students:
                    print(s)
            else:
                print("查无此人")
            continue
        # add
        if cmd == "a":
            while True:
                name, gender, phone_num = get_student_info()
                if not name or not gender or not phone_num:
                    print("姓名，性别 电话不能为空，请重新输入")
                    continue
                management.add_student(name, gender, phone_num)
                break
            continue
        # delete
        if cmd == "d":
            if not management.data:
                print("无学生，请先添加")
                continue
            while True:
                idx = int(input("输入编号"))
                if idx < 0 or idx > len(management.data):
                    print("非法id，请重新输入")
                    continue
                management.delete_student(idx)
                break
            continue
        if cmd == "m":
            if not management.data:
                print("无学生，请先添加")
                continue
            idx = -1
            name = ""
            gender = ""
            phone_num = ""
            while True:
                idx = int(input("输入编号"))
                if idx < 0 or idx > len(management.data):
                    print("非法id，请重新输入")
                    continue
                break
            while True:
                name, gender, phone_num = get_student_info()
                if not name and not gender and not phone_num:
                    print("姓名，性别，手机不能都为空")
                    continue
                management.modify_student(idx, name, gender, phone_num)
                break
            continue
        if cmd == "s":
            management.save_data()    
            continue
        if cmd == "q":
            management.save_data()
            print("退出...")
            return
        
def print_help():
    print("学生管理系统, 支持功能:")
    print("\ta: 添加学生")
    print("\td: 删除学生")
    print("\tm: 修改学生")
    print("\tf: 查询学生")
    print("\tl: 显示学生信息")
    print("\ts: 保存")
    print("\tq: 退出")


if __name__ == "__main__":
    main()