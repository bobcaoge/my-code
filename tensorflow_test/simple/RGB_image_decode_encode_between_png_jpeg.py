# /usr/bin/python3.5
# -*- coding:utf-8 -*-
import tensorflow as tf
import matplotlib.pyplot as plt


image_raw_data = tf.gfile.FastGFile("../test_photo/2.png", "rb").read()
with tf.Session() as sess:
    img_data = tf.image.decode_png(image_raw_data)
    print(img_data.eval())

    plt.imshow(img_data.eval())
    plt.show()

    encoded_image = tf.image.encode_jpeg(img_data)
    with tf.gfile.GFile("../test_photo/test.jpeg", "wb") as f:
        f.write(encoded_image.eval())