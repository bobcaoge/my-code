# /usr/bin/python3.5
# -*- coding:utf-8 -*-
import tensorflow as tf
import matplotlib.pyplot as plt


def manage_color(image):
    # print(tf.shape(image))
    manage_image_data = tf.image.random_brightness(image, max_delta=32./255.)
    manage_image_data = tf.image.random_contrast(manage_image_data, lower=0.5, upper=1.5)
    manage_image_data = tf.image.random_hue(manage_image_data, max_delta=0.2)
    manage_image_data = tf.image.random_saturation(manage_image_data, lower=0.5, upper=1.5)
    return tf.clip_by_value(manage_image_data, 0.0, 1.0)


def get_train_image(img_data, bbox=None):
    manage_data = tf.image.convert_image_dtype(img_data, dtype=tf.float32)

    if bbox is None:
        bbox = tf.constant([[[0.0, 0.0, 1.0, 1.0]]])

    begin, size, bbox_for_draw = tf.image.sample_distorted_bounding_box(
        tf.shape(manage_data),
        bounding_boxes=bbox,
        min_object_covered=0.6
    )
    sliced_data = tf.slice(manage_data, begin, size)

    # resized_image =                                  tf.image.resize_images(sliced_data, shape, random.randint(0, 3))
    flipped_image = tf.image.random_flip_up_down(sliced_data)
    distort_image = manage_color(flipped_image)
    return distort_image


image_raw_data = tf.gfile.FastGFile("../test_photo/2.png", "rb").read()
print(image_raw_data)
with tf.Session() as sess:
    image_data = tf.image.decode_png(image_raw_data)
    boxes = tf.constant([[[0.0329, 0.1732, 0.8263, 0.5932]]])
    for i in range(6):
        managed_image_data = get_train_image(image_data,boxes)
        managed_image_data = tf.image.convert_image_dtype(managed_image_data, dtype=tf.uint8)
        # plt.imshow(managed_image_data.eval())
        # plt.show()
        encode_image = tf.image.encode_png(managed_image_data)
        # print(encode_image)
        with tf.gfile.GFile("../test_photo/cat_train"+str(i)+".png", "wb") as f:
            f.write(encode_image.eval())

