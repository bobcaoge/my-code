# /usr/bin/python3.5
# -*- coding:utf-8 -*-
import tensorflow as tf
import matplotlib.pyplot as plt
image_raw_data = tf.gfile.FastGFile("../test_photo/2.png", "rb").read()
img_data = tf.image.decode_png(image_raw_data)
# **********************************************************
# **********************************************************
# **********************************************************
# 调整图片的大小
# img_data = tf.image.convert_image_dtype(img_data, dtype=tf.float32)
# resized = tf.image.resize_images(img_data, [300, 300], method=0)
# with tf.Session() as sess:
#     plt.imshow(resized.eval())
#     plt.show()
#     resized_data = tf.image.convert_image_dtype(resized, dtype=tf.uint8)
#     encode_image = tf.image.encode_png(resized_data)
#     with tf.gfile.GFile("../test_photo/resized.png", "wb") as f:
#         f.write(encode_image.eval())
# **********************************************************
# **********************************************************
# **********************************************************
# 裁剪图片
# with tf.Session() as sess:
#     resized_with_crop_or_pad = tf.image.resize_image_with_crop_or_pad(img_data, 300, 300)
#     plt.imshow(resized_with_crop_or_pad.eval())
#     plt.show()
#     encode_img = tf.image.encode_png(resized_with_crop_or_pad)
#     with tf.gfile.GFile("../test_photo/resized300.png", 'wb') as f:
#         f.write(encode_img.eval())
#
#     resized_with_crop_or_pad = tf.image.resize_image_with_crop_or_pad(img_data, 3000, 3000)
#     plt.imshow(resized_with_crop_or_pad.eval())
#     plt.show()
#     encode_img = tf.image.encode_png(resized_with_crop_or_pad)
#     with tf.gfile.GFile("../test_photo/resized3000.png", 'wb') as f:
#         f.write(encode_img.eval())

# **********************************************************
# **********************************************************
# **********************************************************
# 按比例裁剪
# with tf.Session() as sess:
#     img_data = tf.image.central_crop(img_data, 0.5)
#     encode_image = tf.image.encode_png(img_data)
#     with tf.gfile.GFile("../test_photo/central_crop.png", "wb") as f:
#         f.write(encode_image.eval())
# **********************************************************
# **********************************************************
# **********************************************************
# 翻转
# with tf.Session() as sess:
#     img_data = tf.image.flip_up_down(img_data)
#     plt.imshow(img_data.eval())
#     plt.show()
# **********************************************************
# **********************************************************
# **********************************************************
# 注释框
image_data = tf.image.convert_image_dtype(img_data, dtype=tf.float32)
batched = tf.expand_dims(image_data, 0)
with tf.Session() as sess:
    boxes = tf.constant([[[0.4141,0.1735, 0.5898, 0.2753],
                          [0.4557,0.4319, 0.5456, 0.4700]]])
    result = tf.image.draw_bounding_boxes(batched, boxes)
    plt.imshow(result[0].eval())
    plt.show()
    image_data = result[0]
    image_data = tf.image.convert_image_dtype(image_data, dtype=tf.uint8)
    encode_image = tf.image.encode_png(image_data)
    with tf.gfile.GFile("../test_photo/box.png", "wb") as f:
        f.write(encode_image.eval())
# **********************************************************
# **********************************************************
# **********************************************************
image_raw_data = tf.gfile.FastGFile("../test_photo/cat.png", "rb").read()
img_data = tf.image.decode_png(image_raw_data)


def get_begin_and_size():
    boxes = tf.constant([[[0.0329, 0.1732, 0.8263, 0.5932]]])
    begin, size, bbox_for_draw = tf.image.sample_distorted_bounding_box(
        tf.shape(img_data),
        boxes,
        min_object_covered=0.4
    )
    return begin, size


with tf.Session() as sess:
    for i in range(10):
        begin, size = get_begin_and_size()
        sliced_image = tf.slice(img_data, begin, size)
        encode_image = tf.image.encode_png(sliced_image)
        with tf.gfile.GFile("../test_photo/cat_slice"+str(i+3)+".png", "wb") as f:
            f.write(encode_image.eval())
# **********************************************************
# **********************************************************
# **********************************************************



