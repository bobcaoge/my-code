# /usr/bin/python3.5
# -*- coding:utf-8 -*-
import tensorflow as tf
import numpy as np
# import matplotlib as mpl
# mpl.use("Agg")
from matplotlib import pyplot as plt

# 隐藏层参数个数
HIDDEN_SIZE = 30
# LSTM层数
NUM_LAYERS = 2

# 时间点  用前面十个点预测下一个点
TiMESTEPS = 10
# 训练次数
TRAINING_STEPS = 10000
# 每个batch的大小
BATCH_SIZE = 32

# 训练样本数
TRAINING_EXAMPLES = 10000
# 测试样本数
TESTING_EXAMPLES = 1000
# 采样间隔
SAMPLE_GAP = 0.01


def generate_data(seq):
    """
    产生用于训练的数据
    :param seq:
    :return: 返回前timesteps个训练值和其后的一个真实值
    """
    x_input = []
    y_output = []
    # 用前TIMESTEPS个点预测后面那个点
    for i in range(len(seq) - TiMESTEPS):
        x_input.append([seq[i: i + TiMESTEPS]])
        y_output.append([seq[i + TiMESTEPS]])
    return np.array(x_input, dtype=np.float32), np.array(y_output, dtype=np.float32)


def lstm_mode(x, y, is_training):
    """
    定义LSTM训练模型
    :param x: 输入
    :param y: 输出
    :param is_training: 是否用于训练
    :return: 预测值，损失函数，训练操作
    """
    # 得到RNN模型
    cell = tf.nn.rnn_cell.MultiRNNCell(
        [tf.nn.rnn_cell.BasicLSTMCell(HIDDEN_SIZE) for _ in range(NUM_LAYERS)]
    )

    # 获得输出
    outputs, _ = tf.nn.dynamic_rnn(cell, x, dtype=tf.float32)
    # outputs 是顶层LSTM在每一步的输出结果， 它的维度是[batch_size, time, HIDDEN_SIZE]
    # 取最后一组预测值
    output = outputs[:, -1, :]
    # 加一层全连接层
    predictions = tf.contrib.layers.fully_connected(output, 1, activation_fn=None)
    if not is_training:
        return predictions, None, None

    # 损失函数
    loss = tf.losses.mean_squared_error(labels=y, predictions=predictions)
    # 创建模型优化器，并获得优化步骤
    train_op = tf.contrib.layers.optimize_loss(
        loss, tf.train.get_global_step(),
        optimizer="Adagrad", learning_rate=0.1
    )
    return predictions, loss, train_op


def train(sess, train_x, train_y):
    """
    训练神经网络
    :param sess:
    :param train_x:
    :param train_y:
    :return:
    """
    # 以数据集的形式提供数据
    ds = tf.data.Dataset.from_tensor_slices((train_x, train_y))
    ds = ds.repeat().shuffle(1000).batch(BATCH_SIZE)
    # 从迭代器中获得数据
    x, y = ds.make_one_shot_iterator().get_next()

    with tf.variable_scope("model"):
        predictions, loss, train_op = lstm_mode(x, y, True)

    tf.global_variables_initializer().run()
    for i in range(TRAINING_STEPS):
        _, l = sess.run([train_op, loss])
        if i % 100 == 0:
            print("train step: " + str(i) + ", loss: " + str(l))


def run_eval(sess, test_x, test_y):
    ds = tf.data.Dataset.from_tensor_slices((test_x, test_y))
    ds = ds.batch(1)
    x, y = ds.make_one_shot_iterator().get_next()

    with tf.variable_scope("model", reuse=True):
        prediction, _, _ = lstm_mode(x, [0.0], False)
    predictions = []
    labels = []
    for i in range(TESTING_EXAMPLES):
        p, l = sess.run([prediction, y])
        predictions.append(p)
        labels.append(l)

    predictions = np.array(predictions).squeeze()
    labels = np.array(labels).squeeze()
    rmse = np.sqrt(((predictions - labels) ** 2).mean(axis=0))
    print("Mean Square Error is: %f" % rmse)
    return predictions, labels


def main():
    train_x, train_y = generate_data(np.sin(np.linspace(
        2*3.14, 2*16*3.14, TRAINING_EXAMPLES+ TiMESTEPS, dtype=np.float32
    )))
    test_x, test_y = generate_data(np.sin(np.linspace(
        2*3.14, 2*2*3.14, TESTING_EXAMPLES+ TiMESTEPS, dtype=np.float32
    )))
    # plt.figure()
    # plt.plot(np.sin(np.linspace(
    #     2*3.14, 2*5*3.14, TESTING_EXAMPLES + TiMESTEPS, dtype=np.float32
    # )))
    # plt.legend()
    # plt.show()
    with tf.Session() as sess:
        train(sess, train_x, train_y)
        predictions, labels = run_eval(sess, test_x, test_y)
        plt.figure()
        plt.plot(predictions, label='predictions')
        plt.plot(labels, label='real_sin')
        plt.legend()
        plt.show()


if __name__ == '__main__':
    main()







