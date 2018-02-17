# The purpose of this exercise is to generate a dictionary that stores book and their respective prices
# Once such dictionary is created, the program should print the books to the user with in a given price range
book = dict() # creating a dicitonary for books
results=[] # The list that will hold the books in range
book ['calc'] = 10 # Entering the Key value pairs in book dictionary
book ["Chem"] = 30
book ["Bio"] = 45
book ["python"] = 60
book ["Java"] = 70
book ["Math"] = 90
book ["English"] = 35
book ["Physics"] = 40
print'The books with their respective prices are: ',book,'\n' # Displaying the book with their respective prices to user
a= input("please enter the starting range of the books you are looking for: ") # asking user for initial price range
b= input("please enter the ending range of the books you are looking for: ") # asking user for final price range
c = b + 1 # The final price +1 will make the upper range inclusive
for x in book: #logic for printing the books with in a given range
    if book[x] in range(a,c):
        results.append(x)
if results != []: # if user has given a valid range print the books
    print'The books you can purchase: ',results
else: # if user has given a range that doesn't exisits then print the error message
    print'There are no books in a given range'