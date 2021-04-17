#print("hello world")
# try:
#     print(num)
# except NameError:
#     print('有错误')

# try:
#     f=open('test.txt','r')
# except:
#     f=open('test.txt,'w'')

# try:
#     print(num)
# except (IndexError,ImportError,NameError) as msg:
#     print(msg)

# try:
#     print(1)
# except Exception as jieguo:
#     print(jieguo)
# else:
#     print('我是else，是没有异常的时候执行的代码')

try:
    f=open('test.txt','r')
except Exception as jieguo:
    f=open('test.txt','w')
else:
    print('没有异常，开心呀')
finally:
    f.close()