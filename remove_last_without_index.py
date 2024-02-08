def remove(lst):
    if len(lst) > 0:
        lst.remove(lst[-1]) 
    else:
        print("List is empty, cannot remove.")
l = [1, 2, 3, 4, 5]
remove(l)
print("List after removing last item:", l)
