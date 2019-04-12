#
# list1 = [1,2,3,4]
#
# print([x for x in list1 if x>2])
# print([x*2 for x in list1 if x>2])
#
# print({x:"item" + str(x) for x in list1})


#斐波那契（Fibonacci）數列是一个非常简单的递归数列，除第一个和第二个数外，任意一个数都可由前两个数相加得到。
#1 1 2 3 5 8 13 21 34 55
def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1

for x in fab(10):
    print(x)


#另一个 yield 的例子来源于文件读取。如果直接对文件对象调用 read() 方法，会导致不可预测的内存占用。
# 好的方法是利用固定长度的缓冲区来不断读取文件内容。
# 通过 yield，我们不再需要编写读文件的迭代类，就可以轻松实现文件读取：
# def read_file(fpath):
#     BLOCK_SIZE = 1024
#     with open(fpath, 'rb') as f:
#         while True:
#             block = f.read(BLOCK_SIZE)
#             if block:
#                 yield block
#             else:
#                 return
#
# p = read_file("C:\se\Random.txt")
# for x in p:
#     print(x)

