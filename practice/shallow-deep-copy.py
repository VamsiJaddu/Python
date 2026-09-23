######### l1 = l2 #############

# l1 = [1,2,3,4,5]
# print(id(l1))
# print(id(l1[0]))
# l2 = l1
# print(id(l2))   
# print(id(l2[0]))

####### shallow copy ##########
l1 = [1,2,3,4,5,[6,7,8]]
# l2 = l1.copy()
# print("l1 :",id(l1))
# print("l2 :",id(l2))
# print("l1[5] :",id(l1[5]))
# print("l2[5] :",id(l2[5]))
# print("l1[5][0] :",id(l1[5][0]))
# print("l2[5][0] :",id(l2[5][0]))

# l1[5][0] = 100
# print("l1 :",l1)
# print("l2 :",l2)
# print("l1 :",id(l1))
# print("l2 :",id(l2))
# print("l1[5] :",id(l1[5]))
# print("l2[5] :",id(l2[5]))
# print("l1[5][0] :",id(l1[5][0]))
# print("l2[5][0] :",id(l2[5][0]))

###########deep copy ############
import copy
l3 = copy.deepcopy(l1)
print("l3 :",id(l3))
print("l3[5] :",id(l3[5]))
print("l3[5][0] :",id(l3[5][0]))
print("l1 :",id(l1))
print("l1[5] :",id(l1[5]))      
print("l1[5][0] :",id(l1[5][0]))

l1[5][0] = 100
print("l1 :",l1)
print("l3 :",l3)
print("l3[5][0] :",id(l3[5][0]))
print("l1 :",id(l1))
print("l1[5] :",id(l1[5]))      
print("l1[5][0] :",id(l1[5][0]))
