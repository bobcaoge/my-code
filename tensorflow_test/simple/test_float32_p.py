# /usr/bin/python3.5
# -*- coding:utf-8 -*-
import tensorflow as tf
import matplotlib.pyplot as plt

image_raw_data = tf.gfile.FastGFile("../test_photo/2.png", "rb").read()
image_data = tf.image.decode_png(image_raw_data)
with tf.Session() as sess:
    # result = tf.image.resize_image_with_crop_or_pad(tf.image.convert_image_dtype(image_data, dtype=tf.float32), 300, 300)
    # result = tf.image.resize_image_with_crop_or_pad(image_data, 300, 300)
    image_data_float32 = tf.image.convert_image_dtype(image_data, dtype=tf.float32)
    # result = tf.image.central_crop(image_data, 0.3) # 按比例裁剪
    result = tf.image.central_crop(image_data_float32, 0.3) # 按比例裁剪
    # plt.imshow(result.eval())
    # plt.show()

# # 翻转
    tf.image.flip_up_down(image_data) #上下翻转
    tf.image.flip_left_right(image_data) #左右翻转
    tf.image.transpose_image(image_data) #沿对角线翻转
    tf.image.random_flip_up_down(image_data)# 随机上下翻转
    tf.image.random_flip_left_right(image_data)# 随机左右翻转
    tf.image.flip_up_down(image_data_float32) #上下翻转
    tf.image.flip_left_right(image_data_float32) #左右翻转
    tf.image.transpose_image(image_data_float32) #沿对角线翻转
    tf.image.random_flip_up_down(image_data_float32)# 随机上下翻转
    tf.image.random_flip_left_right(image_data_float32)# 随机左右翻转
# # 亮度
    tf.image.adjust_brightness(image_data, 0.3)# num: 增加(或减少)的亮度
    # tf.clip_by_value(image_data, 0.0, 1.0)# 将image_data中的像素值阶段在start和end之间 一般为0.0-1.0
    tf.image.random_brightness(image_data, 2.2)# 在[-max_delta, max_delta]之间随机调整图像的亮度
    tf.image.adjust_brightness(image_data_float32, 0.3)# num: 增加(或减少)的亮度
    tf.clip_by_value(image_data_float32, 0.0, 1.0)# 将image_data中的像素值阶段在start和end之间 一般为0.0-1.0
    tf.image.random_brightness(image_data_float32, 2.2)# 在[-max_delta, max_delta]之间随机调整图像的亮度
# # 对比度
    tf.image.adjust_contrast(image_data, 3) #对比度=源对比度*num
    tf.image.random_contrast(image_data, 0, 9) #在lower和upper之间随机调整对比度
    tf.image.adjust_contrast(image_data_float32, 0.3) #对比度=源对比度*num
    tf.image.random_contrast(image_data_float32, 0.0, 1.2)# 在lower和upper之间随机调整对比度
# # 色相
    tf.image.adjust_hue(image_data, 2) #调整色相为num
    tf.image.random_hue(image_data, 0.2)
    tf.image.adjust_hue(image_data_float32, 2) #调整色相为num
    tf.image.random_hue(image_data_float32, 0.2)
# # 饱和度
    tf.image.adjust_saturation(image_data, 0.4) #饱和度 = 源饱和度+num
    tf.image.random_saturation(image_data, 0.0, 3)
    tf.image.adjust_saturation(image_data_float32, 0.4) #饱和度 = 源饱和度+num
    tf.image.random_saturation(image_data_float32, 0.0, 3)
# # 标准化图片
    tf.image.per_image_standardization(image_data)
    tf.image.per_image_standardization(image_data_float32)
# # 标注框
    boxes = tf.constant([0.3, 0.3, 0.5, 0.5], dtype=tf.float32, shape=[1,1,4])
#     boxes = tf.constant([[[0.3, 0.3, 0.5, 0.5]]])
    batched = tf.expand_dims(image_data_float32, axis=0)
    tf.image.draw_bounding_boxes(batched, boxes)
#     # 需要将图片中的数据转换成实数