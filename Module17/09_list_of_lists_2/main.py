nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
             [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]

list1=[x for y in nice_list  for nice_list1 in y for x in nice_list1]
print(list1)
