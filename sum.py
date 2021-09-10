end=int(input("请输入一个整数"))
start=1
sum=0
while start<=end:
    sum+=start
    start+=1
print("从1到%d的和为：%d"%(end,sum))
print(dir())