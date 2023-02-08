ls = ['5', '123', '-7', '33']
li = [5, 123, -7, 33]

sorted_ls = sorted(ls)
sorted_li = sorted(li)
print("Pasul 1:")
print(sorted_ls)
print(sorted_li)

# the differences are that the lists are sorted according to the ascii value of ls and the integer values of li

print("Pasul 2:")
sorted_ls_int = sorted(ls, key=int)
print(sorted_ls_int)
print(sorted_li)

# here the ls list is sorted with each item being classified as an int thereby print in a similar fashion to li
