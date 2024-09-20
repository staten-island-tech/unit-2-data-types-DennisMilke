test_list1 = [1, 2, 3, 4, 5,]
test_list2 = [4, 5, 6, 7,]
 
# printing original lists
print("The original list 1 is : " + str(test_list1))
print("The original list 2 is : " + str(test_list2))
 
# Intersection in Tuple Records Data
# Using list comprehension
res = [ele1 for ele1 in test_list1 
       for ele2 in test_list2 if ele1 == ele2]
