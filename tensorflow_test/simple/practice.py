# /usr/bin/python3.5
# -*- coding:utf-8 -*-
import tensorflow as tf
import matplotlib.pyplot as plt


def main():
    image_raw_data = tf.gfile.FastGFile("../test_photo/1.png", "rb").read()
    img_data = tf.image.decode_png(image_raw_data)
    # hue
    img_data = tf.image.adjust_hue(img_data, delta=0.4)
    img_data = tf.image.random_hue(img_data, max_delta=0.4)
    # saturation
    img_data = tf.image.adjust_saturation(img_data, 0.4)
    img_data = tf.image.random_saturation(img_data, 0.0, 2.0)
    # contrast
    img_data = tf.image.adjust_contrast(img_data, 2)
    img_data = tf.image.random_contrast(img_data, lower=0, upper=2)
    # brightness
    img_data = tf.image.adjust_brightness(img_data, 2)
    img_data = tf.image.random_brightness(img_data, max_delta=0.4)

    img_data = tf.image.convert_image_dtype(img_data, dtype=tf.float32)

    img_data = tf.clip_by_value(img_data, 0.0, 1.0)
    with tf.Session() as sess:
        plt.imshow(img_data.eval())
        plt.show()


if __name__ == '__main__':
    main()

