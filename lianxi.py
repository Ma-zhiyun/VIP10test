#分析：定义类名，定义属性，方法，调用对象，输出
#创建类
class Teacher():
    #属性：
    def __init__(self,name,sex,course):
        self.name=name
        self.sex=sex
        self.course=course
    def print_info(self):
        print(f"{self.name}老师,性别是{self.sex,},教的是{self.course}")

action=Teacher('高',19,'高数')
action.print_info()