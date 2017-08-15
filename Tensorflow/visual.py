import tensorflow as tf
sess = tf.InteractiveSession()
file_writer = tf.summary.FileWriter('/path/to/logs', sess.graph)
