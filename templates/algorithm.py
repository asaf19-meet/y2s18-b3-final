
from keras.preprocessing.image import ImageDataGenerator

from keras import losses
from keras.layers import Dense, Activation, Flatten, MaxPooling2D,Conv2D

from keras import losses
from keras.optimizers import Adam
from keras.models import Sequential
import numpy as np
from keras.preprocessing import image
from PIL import Image
classifier = Sequential()
classifier.add(Conv2D(32, (3, 3), input_shape = (64, 64, 3), activation = 'relu'))
classifier.add(MaxPooling2D(pool_size = (2, 2)))
classifier.add(Flatten())
classifier.add(Dense(units = 128, activation = 'relu'))
classifier.add(Dense(units = 1, activation = 'sigmoid'))
classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])
print('classifier compiled')
train_datagen = ImageDataGenerator(rescale = 1./255,
shear_range = 0.2,
zoom_range = 0.2,
horizontal_flip = True)
test_datagen = ImageDataGenerator(rescale = 1./255)
training_set = train_datagen.flow_from_directory('training_set',
target_size = (64, 64),
batch_size = 32,
class_mode = 'binary')
print(type(training_set))
test_set = test_datagen.flow_from_directory('test_set',
target_size = (64, 64),
batch_size = 32,
class_mode = 'binary')
classifier.fit_generator(training_set,
steps_per_epoch = 2417,
epochs = 25,
validation_data = test_set,
validation_steps = 14)
test_image = image.load_img('dataset/single_prediction/20180814232012_IMG_1289.JPG', target_size = (64, 64))
test_image = image.img_to_array(test_image)
test_image = np.expand_dims(test_image, axis = 0)
result = classifier.predict(test_image)
training_set.class_indices
if result[0][0] == 1:
	prediction = 'Trueeeee'
	print (prediction)
else:
	prediction = 'False'
	print (prediction)
