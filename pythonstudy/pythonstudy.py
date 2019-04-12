# a = 'abcd'
# a = a.replace('d','z')
# print(a)

# str = 'My name is: {0}, the address is {1}'
# str2 = str.format('Tom','Baoan')
# print(str2)
#
# str3 = 'My name is: {name}, the address is {address}'
# str4 = str3.format(name='Jacky', address='FuTian')
# print(str4)


# lia = [x for x in range(200) if x%9 == 0]
# print(lia)
# lia2 = [x*2 for x in range(100) if x%9 == 0]
# print(lia2)
# lia3 = [x for x in range(200) if x%18 == 0]
# print(lia3)


# a = [10,20,30,40]
# a.append([100,200])
# print(a)
# a.extend([300,400])
# print(a)
#
# a.pop(-3)
# print(a)
#
# del a[1]
# print(a)
#
# del a[1]

# a = [10,20]
# b = a * 3
# print(b)

# a = ['bob','alex','Tony','Alice']
# a.sort(reverse=True)
# print(a)
#
# import random
# random.shuffle(a)
# print(a)

# a = [100,50,10,20,30,40]
# a = sorted(a)
# print(a)


# b = tuple('abc')
# print(b)
# b = tuple(range(3))
# print(b)
# b = tuple([1,2,'abc'])
# print(b)



# s = (i*2 for i in range(5))
# print(tuple(s))



# myCat1 = {'name':'Garfield', 'color':'orange', 'size':'fat'}
# print(myCat1)
#
# myCat = dict(name='Garfield', color='orange', size='fat')
# print(myCat)

# k = ['name', 'color', 'size']
# v = ['Garfield', 'orange', 'fat']
# zipped = zip(k, v)
# d = dict(zipped)
# print(d)



# a = dict.fromkeys(['name', 'color', 'size'])
# print(a)
#
# myCat1 = {'name':'Garfield', 'color':'orange', 'size':'fat'}
# print(myCat1.get('name'))
# print(myCat1.get('age', 5))
#
# print(myCat1.items())
#
#
# print(myCat1.keys())
# print(myCat1.values())
#
# print('name' in myCat1)
#
#
# del(myCat1['name'])
# print(myCat1)
#
# b = myCat1.pop('color')
# print(myCat1)


# [x,y,z] = [10,20,30]
# print(x,y,z)
#
# myCat = {'name':'Garfield', 'color':'orange', 'size':'fat'}
# a, b, c = myCat.values()
# print(a, b, c)

# s = {1,10, 4, 'python'}
# s.add('pro')
# print(s)
#
# a = ['a','b','a','c']
# b = set(a)
# print(b)


# testList = [x*2 for x in range(1,50) if x%5 == 0]
# print(testList)

# my_text = 'I love you, I love python, I love programming.'
# char_count = {char:my_text.count(char) for char in my_text}
# print(char_count)

# b = {x for x in range(1,100) if x%9==0}
# print(b)


gnt = (x for x in range(100) if x%9==0)
for i in gnt:
    print(i, end=',')




























