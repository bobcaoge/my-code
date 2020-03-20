import tensorflow as tf
# a = tf.constant('hello world')
# sess = tf.Session()
# print(sess.run(a))

# a = tf.constant([1., 2.], name="a")
# b = tf.constant([1., 3.], name="b")
# result = a + b
# sess = tf.Session()
# with sess.as_default():
#     print(result.eval())

# tf.where and tf.greater
buffer = tf.Variable(tf.random_normal([2, 4], stddev=3, seed=1),dtype=tf.float32, name="buffer")
buffer_o = tf.Variable(tf.random_normal([2, 4], stddev=2, seed=2), dtype=tf.float32, name="buffer")
a = tf.constant([1, 2, 3, 4], name="a")
b = tf.constant([4, 3, 2, 1], name="b")
# z = tf.zeros([2, 4], dtype="float", name="z")
# buffer_o.assign(buffer)
buffer_manager = tf.assign(buffer_o, buffer)
with tf.Session() as sess:
    # sess.run(buffer.initializer)
    sess.run(tf.global_variables_initializer())
    # print("使用assign函数之前")
    # print(sess.run(buffer_o))
    print(sess.run(buffer))
    # print("使用assign函数之后")
    print(sess.run(buffer_o))
    print(sess.run(buffer_manager))
    # print(sess.run(tf.greater(a, b)))
    # print(sess.run(tf.where(tf.greater(a, b), a, b)))


