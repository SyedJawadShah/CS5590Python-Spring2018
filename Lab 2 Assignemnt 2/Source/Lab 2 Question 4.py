# The purpse of this exercise is to generate a random vector of 15 integers between 0 and 20, and then find the most frequent intger.
import numpy as np # importing numpy as np
a = np.random.randint(0,20, size= 15) # creating a random vector of size 15, between 0 and 20
print('The random vector generated is: ',a) # displaying the random vector to user
common=np.bincount(a) # counting the frequency of each integer in the vector using bincount functionality of numpy
result= np.argmax(common) # getting the most frequent intiger by using the argmax functionality of numpy
print('The most Frequent integer in the list is: ', result) # printing the most frequent intger.
