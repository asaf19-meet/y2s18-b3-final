from keras.models import load_model
from keras.preprocessing import image
import numpy as np
classifier = load_model('my_model.h5')


test_image = image.load_img('test_set/20180814232012_IMG_1289.JPG', target_size = (64, 64))
test_image = image.img_to_array(test_image)
test_image = np.expand_dims(test_image, axis = 0)
result = classifier.predict(test_image)

if result[0][0] >= 0.5:
	prediction = 'Trueeeee'
	print (prediction)
else:
	prediction = 'False'
	print (prediction)