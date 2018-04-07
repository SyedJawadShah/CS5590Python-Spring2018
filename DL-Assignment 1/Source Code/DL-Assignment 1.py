import tensorflow as tf

from tensorflow.examples.tutorials.mnist import input_data
# data reading
# mist data is loaded by using TF Learn's built in function
Data_Mn = input_data.read_data_sets("home/Downloads/mnist", one_hot=True)
# Model parameter defined below
learn_scale = 0.01
Collection_amount = 128
num_span = 25
# labels and feature placeholder creation
# image size in mist data = 28*28 = 784
# tensor to represent each image is 1 X 784
# For every Image, digits 0 to 9 represent ten classes.
# one hot vector represents each label.
X = tf.placeholder(tf.float32, [Collection_amount, 784])
Y = tf.placeholder(tf.float32, [Collection_amount, 10])
# bias and weight creation
# weight is created with random variables of mean  0, and stddev 0.01
# bias is created 0
# weight dimensions depends on X and Y
# bias dimensions depends on Y only
weight = tf.Variable(tf.random_normal(shape=[784, 10], stddev=0.01), name="weights")
bias = tf.Variable(tf.zeros([1, 10]), name="bias")
# from X, weight and bias pridection of Y
# a size 10 tensor demonstrates the probability of digits
lgit = tf.matmul(X, weight) + bias
#loss function defination
entropy = tf.nn.softmax_cross_entropy_with_logits(logits=lgit, labels=Y)
loss = tf.reduce_mean(entropy) # computes the mean over examples in the batch
# defination of training op
optmz =tf.train.GradientDescentOptimizer(learning_rate=learn_scale).minimize(loss)
initialz = tf.global_variables_initializer()
with tf.Session() as sess:
    writer = tf.summary.FileWriter('./graphs/logisticregression', sess.graph)
    sess.run(initialz)

    num_batch = int(Data_Mn.train.num_examples/Collection_amount)
    for i in range(num_span): # train the model num_span times
        for _ in range(num_batch):
            X_batch, Y_batch = Data_Mn.train.next_batch(Collection_amount)
            sess.run([optmz, loss], feed_dict={X: X_batch, Y:Y_batch})

    num_batch = int(Data_Mn.test.num_examples/Collection_amount)
    total_correct_preds = 0
    for i in range(num_batch):
            X_batch, Y_batch = Data_Mn.test.next_batch(Collection_amount)
            _, loss_batch, lgit_batch = sess.run([optmz, loss, lgit],
feed_dict={X: X_batch, Y:Y_batch})
            preds = tf.nn.softmax(lgit_batch)
            correct_preds = tf.equal(tf.argmax(preds, 1), tf.argmax(Y_batch, 1))
            accuracy = tf.reduce_sum(tf.cast(correct_preds, tf.float32))
            total_correct_preds += sess.run(accuracy)
    print( "Model Accuracy = {0}".format(total_correct_preds/Data_Mn.test.num_examples))