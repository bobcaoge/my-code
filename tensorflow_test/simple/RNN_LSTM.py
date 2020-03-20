# /usr/bin/python3.5
# -*- coding:utf-8 -*-
# 此代码仅为一个轮廓，并不可运行
import tensorflow as tf
from tensorflow.contrib.layers import fully_connected

lstm_hidden_size = []
batch_size = 1000
num_steps = 10000
expected_output = []
lstm = tf.nn.rnn_cell.BasicLSTMCell(lstm_hidden_size)
state = lstm.zero_state(batch_size, tf.float32)
current_input = []
loss = 0


def calc_loss(final_output, expected_output):
    pass


for i in range(num_steps):
    if i > 0:
        tf.get_variable_scope().reuse_variables()
    lstm_output, state = lstm(current_input, state)
    final_output = fully_connected(lstm_output)
    loss += calc_loss(final_output, expected_output)
