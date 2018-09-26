
import os
import sys

sys.path.append('.')
sys.path.append('../')

import tensorflow as tf
from network.vgg import VGG

if __name__ == '__main__':
	config = {
		"output dims" : 10,
		'name' : 'VGG16',
		'normalization' : 'fused_batch_norm',
		'load pretrained weight' : 'vgg16'
	}

	model = VGG(config, True)
	x = tf.placeholder(tf.float32, shape=(None, 224, 224, 3), name='input')
	y, end_points = model(x)


	for name, value in end_points.items():
		print(name, '  --> ', value.get_shape())

	for var in model.vars:
		print(var.name, ' --> ', var.get_shape())

	

	
	tfconfig = tf.ConfigProto()
	tfconfig.gpu_options.allow_growth = True

	with tf.Session(config=tfconfig) as sess:
		model.load_pretrained_weights(sess)


