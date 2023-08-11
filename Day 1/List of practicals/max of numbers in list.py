list1=[]
a = int(input("Enter the number of elements:"))
for i in range(a):
    list1.append(int(input("Enter a number:")))
print(list1)

print("The maximum of the given numbers in the list is:", max(list1))
