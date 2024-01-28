# 1st Python Program

list=[1,3,2,4,2,3,5,6,3,8,9,10]
unique=[]

for i in list:
    if i not in unique:
        unique.append(i)
print(unique)

     