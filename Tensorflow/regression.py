import tensorflow as tf
import numpy as np
NUM_CORES = 6
config = tf.ConfigProto(
    inter_op_parallelism_threads=NUM_CORES,
    intra_op_parallelism_threads=NUM_CORES
)
# Creating the placeholders. Note that we include names
# for more informative errors and shapes as tensorflow will
# do static size checking.
x = tf.placeholder(tf.float32, shape=(1, 10), name='x')
W = tf.placeholder(tf.float32, shape=(10, 4), name='W')
b = tf.placeholder(tf.float32, shape=(1, 4), name='b')
# The fan-in to the summing junction and the summing
# operation.
y = tf.matmul(x, W) + b
# The activation function.
a = tf.nn.sigmoid(y)
# Adding a softmax filter.
m = tf.nn.softmax(a)
# The activation function doesn't really change here.
with tf.Session(config=config) as s:
    s.run(tf.global_variables_initializer())
    # Let's create some numpy matrices.
    # This is for a single layer of four neurons.
    W_in = np.random.rand(10, 4)
    x_in = np.random.rand(1, 10)
    b_in = np.random.rand(1, 4)
    val = s.run(m,
        feed_dict={
            x: x_in,
            W: W_in,
            b: b_in
        }
    )
    print(val)