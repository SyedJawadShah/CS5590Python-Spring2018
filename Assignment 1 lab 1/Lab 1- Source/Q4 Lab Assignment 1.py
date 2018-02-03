Python = ['Andrew', 'Mitchel','David','Mike', 'Tom','Albert', 'Ali','Saad'] # list for python students
Web_Application = ['Nick','Jerry','Ali','Khan','Tom','Shah','Saad','Mike'] # list for Web Application students
pl= len(Python) # length of 1st list that will be use in for loop for iterations
wl = len(Web_Application) # length of second list to be used in for loops
Common_Students =[] # list that will contain common students
not_common= [] # list that will contain students that are not common in both classes

for j in range (0,pl): # for loops to find common elements in two lists
    for k in range(0,wl):
        if Python[j] == Web_Application[k]: # logic to find common elements
            Common_Students.append(Python[j])
for a in Python: # comparing common students with python to find the students that are  only taking python
    if a not in Common_Students:
        not_common.append(a)
for b in Web_Application: # comparing common students with Web_Application to find the students that are only taking Web Application
    if b not in Common_Students:
       not_common.append(b)
#Now printing all these results on the screen
print( "The students that are taking Python class are: ", Python)
print("The students that are taking Web Application class are: ", Web_Application)
print("Students that are taking both, Python and Web Application, are: ",Common_Students)
print("Students that are not common in both the classes are : ", not_common)
