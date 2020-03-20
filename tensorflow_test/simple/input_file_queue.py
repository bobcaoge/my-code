# /usr/bin/python3.5
# -*- coding:utf-8 -*-
import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


def _int64_feature(value):
    return tf.train.Feature(int64_list=tf.train.Int64List(value=[value]))


def generate_tfrecord_files(num_shards, instance_per_shards):
    for i in range(num_shards):
        filename = ("../tfrecord_files/data.tfrecord-%.5d-of-%.5d" % (i, num_shards))
        writer = tf.python_io.TFRecordWriter(filename)
        for j in range(instance_per_shards):
            example = tf.train.Example(features=tf.train.Features(
                feature={
                    "i": _int64_feature(i),
                    'j': _int64_feature(j)
                }
            ))
            writer.write(example.SerializeToString())
        writer.close()


def main():
    # generate_tfrecord_files(4, 4)
    files = tf.train.match_filenames_once("../tfrecord_files/data.tfrecord-*")
    filename_queue = tf.train.string_input_producer(files, shuffle=False)

    reader = tf.TFRecordReader()
    _, serialized_example = reader.read(filename_queue)
    features = tf.parse_single_example(
        serialized_example,
        features={
            'i': tf.FixedLenFeature([], tf.int64),
            'j': tf.FixedLenFeature([], tf.int64)
        }
    )
    with tf.Session() as sess:
        tf.local_variables_initializer().run()
        print(sess.run(files))

        coord = tf.train.Coordinator()
        threads = tf.train.start_queue_runners(sess, coord)

        for i in range(20):
            print(sess.run([features['i'], features['j']]))
        coord.request_stop()
        coord.join(threads)


def main1():
    files = tf.train.match_filenames_once("../tfrecord_files/data.tfrecord-*")
    filename_queue = tf.train.string_input_producer(files, shuffle=False)

    reader = tf.TFRecordReader()
    _, serialized_example = reader.read(filename_queue)
    features = tf.parse_single_example(
        serialized_example,
        features={
            'i': tf.FixedLenFeature([], tf.int64),
            'j': tf.FixedLenFeature([], tf.int64)
        }
    )

    example, label = features['i'], features['j']

    batch_size = 3

    capacity = 1000 + 3 * batch_size

    example_batch, label_batch = tf.train.shuffle_batch(
        [example, label], batch_size=batch_size, capacity=capacity, min_after_dequeue=12)

    with tf.Session() as sess:
        tf.global_variables_initializer().run()
        tf.local_variables_initializer().run()
        coord = tf.train.Coordinator()
        threads = tf.train.start_queue_runners(sess=sess,coord=coord)

        for i in range(2):
            cur_example_batch, cur_label_batch = sess.run(
                [example_batch, label_batch]
            )
            print(cur_example_batch, cur_label_batch)

        coord.request_stop()
        coord.join(threads)


if __name__ == '__main__':
    main1()





