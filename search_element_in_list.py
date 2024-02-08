def getindex(lst, element):
    if element in lst:
        return lst.index(element)
    else:
        return -1

l = [190, 29, 37, 40,45]
element= int(input("Enter the element to find: "))
index = getindex(l,element)
if index != -1:
    print("Index is : ", index)
else:
    print("Element not found in the list.")
