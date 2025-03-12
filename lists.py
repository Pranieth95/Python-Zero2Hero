x= [10, 23, 654, 777]
y= x[0]

x[0] = 30

print (y) #prints the 1st placed index of the list which is 10
print (x) #prints the list x


z = [30, 40, 50, 60]

z.append (100) #push 100 in the list as the last index
z.insert (2, 70) # insert 70 into the list as the 2nd index which is 3rd placed
z.remove (60) # delete the 60 from list
z.pop(0) # delete the oth intex of the list which is in 1st placed, 30

print (z)
print (20 in z) # check whether 20 is available in the list z
print (40 in z)
print (40 not in z) # check is 40 is not available in the list z
