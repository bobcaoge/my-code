# /usr/local/lib/python3.5
# -*- coding:utf-8 -*-
import tensorflow as tf
# 导入处理mnist数据集的包
from tensorflow.examples.tutorials.mnist import input_data
# 输入节点个数, 为对应于28*28的像素个数
INPUT_NODE = 784
# 输出节点个数，对应于0-9的结果
OUTPUT_NODE = 10

# 隐藏层节点个数
LAYER1_NODE = 500
# 每批处理数据的个数
BATCH_SIZE = 100
# 基础学习率
LEARNING_RATE_BASE = 0.8
# 学习率的衰减率
LEARNING_RATE_DECAY = 0.99
# 正则化项在损失函数中的系数
REGULARIZATION_RATE = 0.0001
# 训练次数
TRAINING_STEPS = 30000
# 滑动平均衰减率
MOVING_AVERAGE_DECAY = 0.99


def inference(input_tensor, avg_class, weights1, biases1, weights2, biases2):
    """
    # 前向传播算法
    :param input_tensor:        输入张量
    :param avg_class:           滑动平均类
    :param weights1:            输入层到中间层的全连接权重
    :param biases1:             输入层到中间层的全连接偏置值
    :param weights2:            中间层到输出层的全连接权重
    :param biases2:             中间层到输出层的全连接偏置值
    :return:                    预测值
    """

    if avg_class is None:
        # 未使用滑动平均算法
        # 仅使用relu()函数去线性化
        layer1 = tf.nn.relu(tf.matmul(input_tensor, weights1) + biases1)
        # 与所用的损失函数(交叉熵)有关
        return tf.matmul(layer1, weights2) + biases2
    else:
        # 使用滑动平均算法
        # 使用relu()函数去线性化
        layer1 = tf.nn.relu(tf.matmul(input_tensor, avg_class.average(weights1)) + avg_class.average(biases1))
        # 与所用的损失函数(交叉熵)有关
        return tf.matmul(layer1, avg_class.average(weights2)) + avg_class.average(biases2)


def train(mnist):
    """
    训练神经网络
    :param mnist:   数据集
    :return:
    """
    # 输入数据
    x = tf.placeholder(tf.float32, shape=[None, INPUT_NODE], name='x_input')
    y_ = tf.placeholder(tf.float32, shape=[None, OUTPUT_NODE], name='y_input')

    # 生成隐藏层参数
    weights1 = tf.Variable(tf.truncated_normal([INPUT_NODE, LAYER1_NODE], stddev=0.1))
    biases1 = tf.Variable(tf.constant(0.1, shape=[LAYER1_NODE]))

    # 生成输出层参数
    weights2 = tf.Variable(tf.truncated_normal([LAYER1_NODE, OUTPUT_NODE], stddev=0.1))
    biases2 = tf.Variable(tf.constant(0.1, shape=[OUTPUT_NODE]))

    # 前向传播算法结果，即预测值
    y = inference(x, None, weights1, biases1, weights2, biases2)

    # 训练轮数
    global_step = tf.Variable(0, trainable=False)

    # 初始化滑动平均类 , 需要滑动平均衰减率和当前训练轮数
    variable_averages = tf.train.ExponentialMovingAverage(MOVING_AVERAGE_DECAY, global_step)
    # 对所有可训练变量应用滑动平均衰减
    variable_averages_op = variable_averages.apply(tf.trainable_variables())
    # 应用滑动平均算法的前向传播算法的结果
    average_y = inference(x, variable_averages, weights1, biases1, weights2, biases2)

    # 交叉熵
    cross_entropy = tf.nn.sparse_softmax_cross_entropy_with_logits(logits=y, labels=tf.argmax(y_, 1))
    # 计算当前batch所有交叉熵的平均值
    cross_entropy_mean = tf.reduce_mean(cross_entropy)
    # 计算L2正则化损失函数
    regularizer = tf.contrib.layers.l2_regularizer(REGULARIZATION_RATE)
    regularization = regularizer(weights1) + regularizer(weights2)
    # 计算总的损失函数
    loss = cross_entropy_mean + regularization
    # 指数衰减学习率
    learning_rate = tf.train.exponential_decay(LEARNING_RATE_BASE,
                                               global_step,
                                               mnist.train.num_examples / BATCH_SIZE,
                                               LEARNING_RATE_DECAY)
    # 训练
    train_step = tf.train.GradientDescentOptimizer(learning_rate).minimize(loss, global_step=global_step)
    # 更新神经网络中的参数以及滑动平均值
    with tf.control_dependencies([train_step, variable_averages_op]):
        train_op = tf.no_op(name='train')
    # 检测预测结果的正确性
    correct_prediction = tf.equal(tf.argmax(average_y, 1), tf.argmax(y_, 1))
    # 计算正确率
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

    with tf.Session() as sess:
        # 初始化所有变量
        tf.global_variables_initializer().run()
        validate_feed = {x: mnist.validation.images,
                         y_: mnist.validation.labels}
        test_feed = {x: mnist.test.images, y_: mnist.test.labels}

        for i in range(TRAINING_STEPS):
            if i % 1000 == 0:
                validate_acc = sess.run(accuracy, feed_dict=validate_feed)
                print("after %d training step(s), validation accuracy "
                      "using average model is %g " % (i, validate_acc))
            xs, ys = mnist.train.next_batch(BATCH_SIZE)
            sess.run(train_op, feed_dict={x: xs, y_: ys})
        test_acc = sess.run(accuracy, feed_dict=test_feed)
        print("After %d training step(s), test accuracy using average"
              " model is %g" % (TRAINING_STEPS, test_acc))


def main(argv=None):
    mnist = input_data.read_data_sets("../MNIST_data", one_hot=True)
    train(mnist)


if __name__ == '__main__':
    tf.app.run()

