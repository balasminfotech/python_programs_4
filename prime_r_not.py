num=12
count=0
lst=[]
for i in range(1,num+1):
    if (num%i)==0:
        lst.append(num%i)
        count=count+1
if count==2:
    print(num, "is a prime number")
else:
     print(num, "is not a prime number")
print(lst)