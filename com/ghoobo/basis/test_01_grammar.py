# 基本语法
import sys
import unittest
from sys import argv, path


class test_grammar(unittest.TestCase):

    def test_telloWorld(self):
        print("HelloWrold!")

    def test_if(self):
        if True:
            print("true")
        elif False:
            print("false")
        else :
            print("impossible")

    def test_input(self):
        # 输入流
        input("按下 enter 键退出，其他任意键显示...\n")

    def test_str(self):
        x = 'ghoobo';
        # 等价print()
        sys.stdout.write(x + '\n')

        str1 = "guohaobo is so handsome!"
        str2 = '''abcdefg'''
        str3 = 'abcdefg'
        print(str1)
        # 输出第一个字符
        print(str1[0])
        # 输出第一个到倒数第二个的所有字符
        print(str1[0:-1])
        # 输出第三个字符开始的所有字符
        print(str1[2:])
        # 输出从第二个开始到第五个且每隔两个的字符
        print(str1[1:5:2])
        # 以下用于反转字符串
        print(str1[-1::-1])
        # 连续输出字符串2次
        print(str1 * 2)
        # 连接字符串
        print("str1 is : " + str1)

        # 使用反斜杠(\)+n转义特殊字符
        print("hello\nworld!")
        # 在字符串前面添加一个 r，表示原始字符串，不会发生转义,"r"指"raw"，即raw string，会自动将反斜杠转义
        print(r"hello\nworld!")
        # 或者多加一个转义符，即将转义符转义
        print("hello\\nworld!")

        a="hello"
        b="world"
        # 换行输出
        print(a)
        print(b)
        # 不换行输出
        print(a, end=" ")
        print(b)
        # 不换行输出
        print(a,b)

    def test_for(self):
        str1 = "guohaobo is so handsome!"
        for i in str1:
            print(i)

    def test_import(self):
        for i in sys.argv:
            print (i)
        print ('python 路径为:')
        for i in sys.path:
            print (i)

    def test_from_import(self):
        print ('python 路径为:')
        for i in path:
            print (i)
        print ('命令行参数为:',argv)