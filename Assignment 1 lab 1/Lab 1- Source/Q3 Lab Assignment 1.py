trip_list = [1,3,6,2,-1,-3,2,8,-2,9] # The list that contains integers from where the triplets need to be found
l= len(trip_list) # storing the length of the list in a variable so that it can be used to determine iterations in for loops
def sum_triplets (a,b): # defining a function that will find the triplet with sum = 0 by adding all the possible combinations.
    sum_zero = False  # a boolean flag that will indicate weather a list contains a triplet with sum = 0 or not
    for m in range(0,l-2): # 1st for loop will run from 1 element in the list till the 3rd last element.
        for n in range(m+1,l-1): # 2nd for loop will run from 2nd element in the list till the 2nd last element.
            for o in range(n+1,l): #3rd loop will run from 3rd element in the list till the last element.
                sum_trip=trip_list[m]+trip_list[n]+trip_list[o] # variable that will store the sum of triplets
                if sum_trip == 0: # logic to apply if sum of triplet = 0
                    print("The triplet in the list with sum = 0 is: [(",trip_list[m], ",", trip_list[n], ",",trip_list[o], ")]")
                    sum_zero = True # turn the flag true if such triplet is found
    if sum_zero == False: # if not a such triplet is found let the user know that list doesn't contain any with sum = 0
        print("There is not a single triplet in the list whose sum is = 0")
print("The list that is used by this program is: ", trip_list)
sum_triplets(trip_list,l) # calling the above function and passing list and its length into it.
