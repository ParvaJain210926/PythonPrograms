def remove(lst):
    if len(lst) > 0:
        lst.pop()
    else:
        print("List is empty, cannot remove.")

# Test the function
l = [1, 2, 3, 4, 5]
remove(l)
print("List after removing last item:", l)
