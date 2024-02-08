def count(lst, element):
    return lst.count(element)
l = [1, 2, 3, 2, 4, 2, 5]
element= int(input("Enter the element to count: "))
occ = count(l, element)
print("Number of times occurs in the list:", occ)
