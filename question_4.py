
def last(n):
	return n[m]

def sort(tuples):
	return sorted(tuples, key = last)

size=int(input("enter your list size:"))
list1=[]
for i in range(size):
    list2=[]
    print("enter your 1st element in tuple:",end="")
    list2.append(int(input()))
    print("enter your 2st element in tuple:",end="")
    list2.append(int(input()))
    tuple1=tuple(list2)
    list1.append(tuple1)
    
m = 1
print("Sorted:"),
print(sort(list1))
