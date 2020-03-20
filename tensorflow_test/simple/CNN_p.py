# /usr/bin/python3.5
# -*- coding:utf-8 -*-
"""
本代码仅为卷积神经网络Le-Net5的前向传播算法，无法单独运行
"""
import tensorflow as tf
import tensorflow.contrib.slim as slim
INPUT_NODE = 784
OUTPUT_NODE = 10

IMAGE_SIZE = 28
NUM_CHANNEL = 3
NUM_LABELS = 10

CONV1_DEEP = 32
CONV1_SIZE = 5

CONV2_DEEP = 32
CONV2_SIZE = 5

FC_SIZE = 512


def inference(input_tensor, train, regularizer):

    with tf.variable_scope("layer1-conv1"):
        conv1_weight = tf.get_variable("conv1-weight", [CONV1_SIZE, CONV1_SIZE, NUM_CHANNEL, CONV1_DEEP], tf.float32, initializer=tf.truncated_normal_initializer(stddev=1))
        conv1_bias = tf.get_variable("conv1-bias", [CONV1_DEEP], initializer=tf.constant_initializer(0.0))
        layer1 = tf.nn.conv2d(input_tensor, conv1_weight, strides=[1, 2, 2, 1], padding="SAME")
        conv1 = tf.nn.relu(tf.nn.bias_add(layer1, conv1_bias))
        if regularizer is not None:
            tf.add_to_collection("losses", regularizer(conv1_weight))
    with tf.variable_scope("layer2-poo11"):
        pool1 = tf.nn.max_pool(conv1, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding="SAME")

    with tf.variable_scope("layer3-conv2"):
        conv2_weight = tf.get_variable("conv2-weight", [CONV2_SIZE, CONV2_SIZE, CONV1_DEEP, CONV2_DEEP], tf.float32, initializer=tf.truncated_normal_initializer(stddev=1))
        conv2_bias = tf.get_variable("conv2-bias", [CONV1_DEEP], initializer=tf.constant_initializer(0.0))
        layer3 = tf.nn.conv2d(pool1, conv2_weight, strides=[1, 2, 2, 1], padding="SAME")
        conv2 = tf.nn.relu(tf.nn.bias_add(layer3, conv2_bias))
        if regularizer is not None:
            tf.add_to_collection("losses", regularizer(conv2_weight))
    with tf.variable_scope("layer4-poo12"):
        pool2 = tf.nn.max_pool(conv2, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding="SAME")

    pool_shape = pool2.get_shape().as_list()

    nodes = pool_shape[1] * pool_shape[2] * pool_shape[3]

    layer4 = tf.reshape(pool2, [pool_shape[0], nodes])

    with tf.variable_scope("layer5-fc1"):
        fc1_weight = tf.get_variable("weight", [nodes, FC_SIZE], initializer=tf.truncated_normal_initializer(stddev=1))
        fc1_bias = tf.get_variable("bias", [FC_SIZE], initializer=tf.constant_initializer(0.0))
        layer5 = tf.nn.relu(tf.matmul(layer4, fc1_weight) + fc1_bias)
        if regularizer:
            tf.add_to_collection("losses", regularizer(fc1_weight))
        if train:
            layer5 = tf.nn.dropout(layer5, 0.5)

    with tf.variable_scope("layer6-fc2"):
        fc2_weight = tf.get_variable("weight", [FC_SIZE, NUM_LABELS], initializer=tf.truncated_normal_initializer(stddev=1))
        fc2_bias = tf.get_variable("bias", [NUM_LABELS], initializer=tf.constant_initializer(0.0))
        layer6 = tf.nn.relu(tf.matmul(layer5, fc2_weight) + fc2_bias)
        if regularizer:
            tf.add_to_collection("losses", regularizer(fc2_weight))
        if train:
            layer6 = tf.nn.dropout(layer6, 0.5)

    return layer6


def inference_with_slim(input_tensor):
    """
    使用slim搭建CNN结构，实现前向传播算法
    :param input_tensor: 输入张量
    :return:
    """
    layer1 = slim.conv2d(input_tensor, CONV1_DEEP, [CONV1_SIZE, CONV1_SIZE])
    layer2 = slim.max_pool2d(layer1, kernel_size=2)
    layer3 = slim.conv2d(layer2, CONV2_DEEP, [CONV2_SIZE, CONV2_SIZE])
    layer4 = slim.max_pool2d(layer3, kernel_size=2)
    layer4 = slim.flatten(layer4)
    layer5 = slim.fully_connected(layer4, FC_SIZE)
    layer6 = slim.fully_connected(layer5, NUM_LABELS)
    return layer6








