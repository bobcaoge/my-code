# /usr/local/lib/python3.5
# -*- coding:utf-8 -*-
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
import numpy as np
# with tf.variable_scope("first"):
#     v = tf.get_variable("v", [1])
#     print(v)
#     with tf.variable_scope("second"):
#         print(tf.get_variable_scope().reuse)
#         v2 = tf.get_variable("v2", [3])
#         print(v2)
#
# with tf.variable_scope("first", reuse=True):
#     buffer = tf.get_variable('v')
#     print(buffer)
#
# print(v)
# print(v2)
# **********************************************************
# 持久化
# a = tf.Variable(tf.constant(1.2, tf.float32, [2, 4]), name="a")
# b = tf.Variable(tf.constant(1.2, tf.float32, [2, 4]), name="b")
# result = a + b
# saver = tf.train.Saver()
# init_op = tf.global_variables_initializer()
# with tf.Session() as sess:
#     sess.run(init_op)
#     sess.run(result)
#     saver.save(sess, "./save.ckpt")
# **********************************************************
# **********************************************************
# **********************************************************
# 将v 和 v的滑动平均值 保存到文件中
# v = tf.Variable(0, dtype=tf.float32, name='v')
# ema = tf.train.ExponentialMovingAverage(0.99)
# maintain_averages_op = ema.apply(tf.global_variables())
# init_op = tf.global_variables_initializer()
#
# saver = tf.train.Saver()
# with tf.Session() as sess:
#     sess.run(init_op)
#     print(sess.run(v))
#     sess.run(tf.assign(v, 10))
#     sess.run(maintain_averages_op)
#     print(sess.run([v, ema.average(v)]))
#     saver.save(sess, '../savefile/ema.ckpt')
# **********************************************************
# **********************************************************
# **********************************************************
# 直接将ckpt文件中保存的v加载到代码中的v中
# v = tf.Variable(0, dtype=tf.float32, name='v')
# ema = tf.train.ExponentialMovingAverage(0.99)
# print(ema.variables_to_restore())
# saver = tf.train.Saver(ema.variables_to_restore())
# with tf.Session() as sess:
#     saver.restore(sess, "../savefile/ema.ckpt")
#     print(sess.run(v))
# **********************************************************
# **********************************************************
# **********************************************************

# CNN 卷积层前向传播算法

# 给出过滤器
# filter_weight = tf.get_variable(
#     'weights', [5, 5, 3, 16],
#      initializer=tf.truncated_normal_initializer(stddev=0.1)
#     )
# # 给出偏置项
# biases = tf.get_variable(
#     'biases', [16],
#     initializer=tf.truncated_normal_initializer(stddev=0.1)
#     )
# # 使用过滤器
# conv = tf.nn.conv2d(input, filter_weight, strides=[1, 1, 1, 1], padding='SAME')
# # 使用偏置项
# result = tf.nn.bias_add(conv, biases)
# # 去线性化
# actived_conv = tf.nn.relu(result)

# **********************************************************
# **********************************************************
# **********************************************************

# CNN 池化层前向传播算法
# activated_conv = None

# pool = tf.nn.max_pool(actived_conv, ksize=[1, 3, 3, 1], strides=[1, 2, 2, 1], padding='SAME')

# **********************************************************
# **********************************************************
# **********************************************************
# tfrecord 写入
#
# def _int64_feature(value):
#     return tf.train.Feature(int64_list=tf.train.Int64List(value=[value]))
#
#
# def _bytes_feature(value):
#     return tf.train.Feature(bytes_list=tf.train.BytesList(value=[value]))
#
#
# path = "../MNIST_data"
#
# mnist = input_data.read_data_sets(path, dtype=tf.uint8, one_hot=True)
#
# labels = mnist.train.labels
# # for label in labels:
# #     print(label)
# images = mnist.train.images
# filename = "../tfrecord_files/test_of_mnist.tfrecords"
# writer = tf.python_io.TFRecordWriter(filename)
# # 分辨率
# # 图片信息
# # 标签
# num_examples = mnist.train.num_examples
# for i in range(num_examples):
#     pixels = images.shape[1]
#     image_raw = images[i].tostring()
#     label = np.argmax(labels[i])
#     # print(pixels, image_raw[:5], label)
#     # print("=============")
#     example = tf.train.Example(
#         features=tf.train.Features(feature={
#             "pixels": _int64_feature(pixels),
#             "label": _int64_feature(label),
#             "image_raw": _bytes_feature(image_raw)
#         })
#     )
#     writer.write(example.SerializeToString())
# writer.close()
# **********************************************************
# **********************************************************
# **********************************************************
# q = tf.FIFOQueue(10, "int32")
# q = tf.FIFOQueue(10, tf.int32)
# init = q.enqueue_many(([0, 10], ))
# x = q.dequeue()
# y = x + 1
# q_inc = q.enqueue([y])
#
# with tf.Session() as sess:
#     init.run()
#     for _ in range(5):
#         v, _ = sess.run([x, q_inc])
#         print(v)
# **********************************************************
# **********************************************************
# **********************************************************
# 队列管理器 queue_runner coordinator
queue = tf.FIFOQueue(100, tf.float32)
queue_op = queue.enqueue([tf.truncated_normal([1])])
qr = tf.train.QueueRunner(queue, [queue_op] * 5)
out = queue.dequeue()
tf.train.add_queue_runner(qr)
with tf.Session() as sess:
    coord = tf.train.Coordinator()
    threads = tf.train.start_queue_runners(sess=sess, coord=coord)

    for _ in range(300):
        print(sess.run(out)[0])

    coord.request_stop()
    coord.join(threads)


# **********************************************************
# **********************************************************
# **********************************************************




