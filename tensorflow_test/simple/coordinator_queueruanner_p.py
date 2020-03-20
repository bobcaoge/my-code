# /usr/bin/python3.5
# -*- coding:utf-8 -*-
import tensorflow as tf


def main():
    queue = tf.FIFOQueue(10, tf.float32)
    queue_op = queue.enqueue([tf.random_normal([1])])
    qr = tf.train.QueueRunner(queue, [queue_op]*5)
    tf.train.add_queue_runner(qr)
    out_tensor = queue.dequeue()
    coord = tf.train.Coordinator()
    with tf.Session() as sess:
        threads = tf.train.start_queue_runners(sess, coord)
        for _ in range(3000):
            print(sess.run(out_tensor)[0])
        coord.request_stop()
        coord.join(threads)


if __name__ == '__main__':
    main()
