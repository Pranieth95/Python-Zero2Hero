x = {'1000' : "Colombo", '2000' : "Kurunegala"}  #Initializing a dictionary
x ['3000'] = "Kotte" #Include vales to a dictionary

print (x)
print (x.values()) #print only the values inside the dictionary
print (x.keys()) #print only the keys inside the dictionary



y= x.get(3, 0) #Check if 3 is in the dictionary and if not return 0
print (y)