import tensorflow as tf

a = tf.constant ([3,6]) # making a metrices 1x2 with constant value  and naming it to a
b = tf.constant ([4,5]) # making a metrices 1x2 with constant value and naming it to b
c = tf.constant ([9,8]) # making a metrices 1x2 with constant value  and naming it to a
d = tf.pow(a,2) # taking the power of a^2
with tf.Session() as sess: # printing the results
    result = sess.run(d)
    print("The a^2 with constant [3,6] is",result)

e = tf.add (d,b) # adding a^2 + b
with tf.Session() as sess:
    result = sess.run(e)
    print("The a^2 + b is equal to",result)


f = tf.multiply (e,c) # evalutaing (a^2 + b) * c
with tf.Session() as sess:
    result = sess.run(f)
    print("The (a^2 + b)*c is equal to",result)