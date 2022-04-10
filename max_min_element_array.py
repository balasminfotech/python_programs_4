ele=[3,1,5,2,4]
# result=0
# for i in ele:
#     result=result+i
print(max(ele))
print(min(ele))
# print("sum of elements inan array is {} ".format(result))
ele.sort()
print("minimum value is: ", ele[0])
print("maximum value is: ", ele[-1])


max=ele[0]
for i in range(0,len(ele)):
    if ele[i] >max:
        max=ele[i]
print("Maximum value from an element is {} ".format(max))


min=ele[0]
for i in range(0,len(ele)):
    if ele[i] <min:
        min=ele[i]
print("Minimum value from an element is {} ".format(min))