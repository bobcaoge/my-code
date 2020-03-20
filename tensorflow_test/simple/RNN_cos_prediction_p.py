# /usr/bin/python3.6
# -*- coding:utf-8 -*-

import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
TIMESTEPS= 10
TRAINSTEPS = 10000
HIDDEN_SIZE = 30
NUM_LAYERS = 2
BATCH_SIZE = 32
TESTINGSTEPS= 1000


def generate_data(seq):
    x = []
    y = []
    for i in range(len(seq) - TIMESTEPS):
        x.append([seq[i:i+TIMESTEPS]])
        y.append([seq[i+TIMESTEPS]])
    return np.array(x, np.float32), np.array(y, np.float32)


def lstm_mode(x, y, is_training):
    cell = tf.nn.rnn_cell.MultiRNNCell(
        [tf.nn.rnn_cell.BasicLSTMCell(HIDDEN_SIZE) for _ in range(NUM_LAYERS)])
    outputs, _ = tf.nn.dynamic_rnn(cell, x, dtype=tf.float32)
    output = outputs[:, -1, :]
    predictions = tf.contrib.layers.fully_connected(output, 1, activation_fn=None)
    if not is_training:
        return predictions, None, None
    loss = tf.losses.mean_squared_error(labels=y, predictions=predictions)
    train_op = tf.contrib.layers.optimize_loss(
        loss, tf.train.get_global_step(),optimizer="Adagrad", learning_rate=0.01
    )
    return predictions, loss, train_op


def train(sess, train_x, train_y):
    ds = tf.data.Dataset.from_tensor_slices((train_x, train_y))
    ds = ds.repeat().shuffle(1000).batch(BATCH_SIZE)
    x, y = ds.make_one_shot_iterator().get_next()
    with tf.variable_scope("model"):
        predictions, loss, train_op = lstm_mode(x, y, True)
    tf.global_variables_initializer().run()
    for i in range(TRAINSTEPS):
        _, l = sess.run([train_op, loss])
        if i % 100 == 0:
            print("train step:" + str(i), "loss:" + str(l))


def run_eval(sess, test_x, test_y):
    print("start run eval")
    ds = tf.data.Dataset.from_tensor_slices((test_x, test_y))
    ds = ds.batch(1)
    x, y = ds.make_one_shot_iterator().get_next()
    with tf.variable_scope("model", reuse=True):
        prediction, _, _= lstm_mode(x, [1.0], False)
    predictions = []
    labels = []
    for i in range(TESTINGSTEPS):
        p, l = sess.run([prediction, y])
        predictions.append(p)
        labels.append(l)
    print("run_eval over")
    predictions = np.array(predictions).squeeze()
    labels = np.array(labels).squeeze()
    return predictions, labels


if __name__ == '__main__':
    data_train = np.cos(np.linspace(2*3.14, 2*10*3.14, TRAINSTEPS+TIMESTEPS, dtype=np.float32))
    data_test = np.cos(np.linspace(2*3.14, 2*2*3.14, TESTINGSTEPS+TIMESTEPS, dtype=np.float32))
    train_x, train_y = generate_data(data_train)
    test_x, test_y = generate_data(data_test)
    print(len(train_x))
    print(len(test_x))
    with tf.Session() as sess:
        train(sess, train_x, train_y)
        print("train over")
        predictions, labels = run_eval(sess, test_x, test_y)
        print("run_eval over")
        plt.figure()
        plt.plot(predictions, label="predictions")
        plt.plot(labels, label="real_cos")
        plt.legend()
        plt.show()


















