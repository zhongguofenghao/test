#if 2==1:
#   print("1")
#else:
#   print("2")
#from typing import AsyncGenerator


#age=int(input("请输入狗狗的年龄："))
#if age<=0:
#    print("你在逗我吧")
#elif age==1:
#    print("相当于14岁的人")
#elif age==2:
#    print("相当于22岁的人")
#else:
#    human=22+(age-2)*5
#    print("对应人类的年龄：",human)
a=100
guess=-1
while guess!=a:
    guess=int(input("猜猜这个数是多少"))
    if guess==a:
        print("你猜对了")
    elif guess>a:
        print("猜大了")
    elif guess<a:
        print("猜小了")