import tensorflow as tf

w = tf.Variable(tf.random_normal([2, 3], stddev=1), name='w')
x = tf.placeholder(dtype=tf.float32, shape=(1, 2), name='x')
y = tf.matmul(x, w)
with tf.Session() as sess:
    init_op = tf.global_variables_initializer()
    sess.run(init_op)
    print(sess.run(y, feed_dict={x: [[1.0, 2.0]]}))