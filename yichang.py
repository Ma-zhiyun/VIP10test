# """
#
# import time
#
# try:
#     f = open('test.txt')
#
#     try:
#         while True:
#             content = f.readline()
#             if len(content) == 0:
#                 break
#             time.sleep(2)
#             print(content)
#     except:
#         # 如果在读取⽂文件的过程中，产生了了异常，那么就会捕获到
#         # ⽐比如 按下了了 ctrl+c
#         print('意外终⽌止了了读取数据')
#     finally:
#         f.close()
#         print('关闭⽂文件')
# except:
#     print("没有这个⽂文件")
# print('hello')
#1.类-第一步：先创建类-定义属性和方法
# class Washer():
#     def wash(self):
#         print('我会洗衣服')
# #2.对象-第二步：创建类下的对象
# haier1=Washer()
# #3.调用-第三步：对象 调用 类 里的 方法
# haier1.wash()
# ONE-类外创建属性
# haier1.width=500
# haier1.height=800
# print(f'hair1的洗衣机宽度是{haier1.width}')
# print(f'hair1的洗衣机高度是{haier1.height}')
#TWO-类里创建属性
class Washer():
    def print_info(self):
        print(f'haier1洗衣机的宽度是{self.width}')
        print(f'haier2洗衣机的高度是{self.height}')
haier1=Washer()
haier1.width=500
haier1.height=800
haier1.print_info()
