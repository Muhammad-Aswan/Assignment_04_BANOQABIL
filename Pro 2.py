# 2nd Python Program

num=int(input("Enter a number : "))
dict={}
for i in range(1,num+1):
    dict.update({i:i*i})
print(dict)