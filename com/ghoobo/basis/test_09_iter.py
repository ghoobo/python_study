import sys
import unittest

class test_iter(unittest.TestCase):

    def test_for(self):
        list = [1, 2, 3, 4, 5]
        for x in list:
            print(x, end=" ")
            if x == 4:
                print("end")
                break
        else:   # list为空时候执行
            print("没有循环数据")

    def test_while(self):
        a = 1
        while a < 10:
            print(a, end=" ")
            a+=1    # a++报红
        else:   # while后为False时执行一次，然后结束循环
            print("结束")
        '''
        while True:
            print("死循环")
        '''

    def test_iter(self):
        list1 = [1, 2, 3, 4, 5]
        list2 = [1, 2, 3, 4, 5]
        it1 = iter(list1)
        it2 = iter(list2)
        # for
        for x in it1:
            print(x, end=" ")
        else:   # for循环结束执行
            print()
        # while
        while True:
            try:
                print(next(it2), end=" ")
            except StopIteration:
                sys.exit()  # 当try块中StopIteration异常时，执行

    def fibonacci(self,n):  # 生成器函数 - 斐波那契
        a, b, counter = 0, 1, 0
        while True:
            if (counter > n):
                return
            yield a
            a, b = b, a + b
            counter += 1

    def test_yield(self):
        f = self.fibonacci(10)  # f 是一个迭代器，由生成器返回生成

        while True:
            try:
                print(next(f), end=" ")
            except StopIteration:
                sys.exit()