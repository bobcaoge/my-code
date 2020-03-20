# /usr/bin/python3.5
# -*- coding:utf-8 -*-
import tensorflow as tf


def parser(record):
    features = tf.parse_single_example(
        record,
        features={
            'i': tf.FixedLenFeature([], tf.int64),
            'j': tf.FixedLenFeature([], tf.int64)
        }
    )
    return features['i'], features['j']


# input_data = ['../tfrecord_files/data.tfrecord-00000-of-00004', '../tfrecord_files/data.tfrecord-00000-of-00004']
input_data = tf.placeholder(tf.string)
data_set = tf.data.TFRecordDataset(input_data)
data_set = data_set.map(parser)
iterator = data_set.make_initializable_iterator()
example, label = iterator.get_next()
with tf.Session() as sess:
    sess.run(iterator.initializer, feed_dict={
        input_data: ['../tfrecord_files/data.tfrecord-00000-of-00004', '../tfrecord_files/data.tfrecord-00000-of-00004']
    })
    while True:
        try:
            exa, lab = sess.run([example, label])
            print(exa, lab)
        except tf.errors.OutOfRangeError:
            break
