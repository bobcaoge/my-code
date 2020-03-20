# /usr/bin/python3.5
# -*- coding:utf-8 -*-
import tensorflow as tf
import time
import numpy as np
import threading


def my_loop(coord, worker_id):
    while not coord.should_stop():
        if np.random.rand() < 0.1:
            print("Stopping from id:" + str(worker_id))
            coord.request_stop()
        else:
            print("Working on id:" + str(worker_id))
        time.sleep(1)


def main():
    coord = tf.train.Coordinator()
    threads = [threading.Thread(target=my_loop, args=(coord, i,)) for i in range(5)]
    for thread in threads:
        thread.start()
    coord.join(threads)


if __name__ == '__main__':
    main()


