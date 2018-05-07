#Algorithm V11.py
#Neural Network computes the rating of a person based on their measurements
#Use to test various parameters
#Current iteration: 15 nodes per layer, learning rate 0.001
#balanced neural network (35 entries, 3 iterations) (V15)
#Try to print weights during training to see progression (V15)
#Used a random selection system to create batches of data (V16)
#Uses new measurementCalc, which regularizes data (V16)
#Uses 50 nodes per layer, rather than 15 (V16)
#Checking to see if this works (just train 2 images until overfit to death)

##REQUIREMENTS FOR NN:
#1. feed in .txt files which were generated using PointSelector GUI
#2. Algorithm will train the things one batch at a time


import tensorflow as tf
import numpy as np
import measurementCalcV5 as mc #Updated 20180421
import answerCalc as ac #Updated 20180417
import random
import sys

#Increase the threshold of prints
np.set_printoptions(threshold=sys.maxsize)
numMeasurements = 15
x = tf.placeholder('float', shape = [None,numMeasurements])
y = tf.placeholder('float')

def neural_network(data):
	num_nodes_hl1 = 50 #500 #for now
	num_nodes_hl2 = 50#500 #for now
	num_nodes_hl3 = 50 #500 #for now
	num_nodes_hl4 = 50 #500 #for now
	num_nodes_hl5 = 50 #500 #for now
	num_classes_1 = 10 #100 #for now

	#Declare all the dictionaries
	#hlayerx_parameters contains the parameters which will generate hlayerx
	hlayer1_parameters = {'weights': tf.Variable(tf.random_normal([numMeasurements, num_nodes_hl1])), 
						'biases': tf.Variable(tf.random_normal([1, num_nodes_hl1]))}
	
	hlayer2_parameters = {'weights': tf.Variable(tf.random_normal([num_nodes_hl2, num_nodes_hl1])), 
						'biases': tf.Variable(tf.random_normal([1, num_nodes_hl2]))}
	
	hlayer3_parameters = {'weights': tf.Variable(tf.random_normal([num_nodes_hl3, num_nodes_hl2])), 
						'biases': tf.Variable(tf.random_normal([1, num_nodes_hl3]))}
	
	hlayer4_parameters = {'weights': tf.Variable(tf.random_normal([num_nodes_hl4, num_nodes_hl3])), 
						'biases': tf.Variable(tf.random_normal([1, num_nodes_hl4]))}
	
	hlayer5_parameters = {'weights': tf.Variable(tf.random_normal([num_nodes_hl5, num_nodes_hl4])), 
						'biases': tf.Variable(tf.random_normal([1, num_nodes_hl5]))}
	
	output_layer_parameters =  {'weights': tf.Variable(tf.random_normal([num_nodes_hl5, num_classes_1])), 
							'biases': tf.Variable(tf.random_normal([1, num_classes_1]))}


	hlayer1 = tf.add(tf.matmul(data, hlayer1_parameters['weights']), hlayer1_parameters['biases'])
	hlayer1 = tf.nn.relu(hlayer1)

	hlayer2 = tf.add(tf.matmul(hlayer1, hlayer2_parameters['weights']), hlayer2_parameters['biases'])
	hlayer2 = tf.nn.relu(hlayer2)

	hlayer3 = tf.add(tf.matmul(hlayer2, hlayer3_parameters['weights']), hlayer3_parameters['biases'])
	hlayer3 = tf.nn.relu(hlayer3)

	hlayer4 = tf.add(tf.matmul(hlayer3, hlayer4_parameters['weights']), hlayer4_parameters['biases'])
	hlayer4 = tf.nn.relu(hlayer4)

	hlayer5 = tf.add(tf.matmul(hlayer4, hlayer5_parameters['weights']), hlayer5_parameters['biases'])
	hlayer5 = tf.nn.relu(hlayer5)

	#No activation for final layer
	output_layer = tf.add(tf.matmul(hlayer5, output_layer_parameters['weights']), output_layer_parameters['biases'])
	#output_layer = tf.nn.relu(output_layer)
	return output_layer
	
def neural_network_Trainer(inputMatrix, label, num_epochs):
	#Training method:
	#declare prediction, cost function, optimizer, feed in x values for each
	#This function trains the NN 1 image at a time
	#1. Declare what our prediction will be each time
	prediction = neural_network(x)		

	intY= tf.cast(y, tf.int32)
	
	#2. Convert y into onehot coding
	oneHotY = tf.one_hot(intY-1, depth = 10, axis = 1) #changes the value into a 1-hot code with length num_classes (subtract 1 from answer b/c 0 translates into (1,0,0, ... )
	#3. Compute cost, optimize
	cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits = prediction, labels = oneHotY))
	optimizer = tf.train.AdamOptimizer(0.001).minimize(cost)		
	
	saver = tf.train.Saver()

	with tf.Session() as sess:
		sess.run(tf.global_variables_initializer())

		for epoch in range(0, num_epochs):
			epoch_loss = 0
			_, c = sess.run([optimizer, cost], feed_dict = {x:inputMatrix, y:label})
			epoch_loss+=c
			print("epoch ", epoch, "loss: ", c)

		saver.save(sess, "/tmp/model1.ckpt")

if (__name__ == '__main__'):
	#1. Collect information
	mode = input("Are we training or predicting this iteration? Please select 'train' or 'predict'\nSelection:")
	if(mode == "train"):
		numEpoch = int(input("How many epochs (training cycles) would you like to run? Please enter an integer value: "))
		trainingFilePath = input("Where is the file containing the training set located? ") #Stores the file in which the training set is stored
		answerFilePath = input("Where are the correct answers of the training set located? ") #Stores the file in which answers are stored
		
		trainingMatrix = mc.measurementCalculator(trainingFilePath)

			#2. Process correct answers
			#answerList will be 1 x batchSize array
		answerList = ac.answerCalculator(answerFilePath)

		neural_network_Trainer(trainingMatrix, answerList, numEpoch)
	
	else:
		filePath = input("Where is the file containing the training set located? ") #Stores the file in which the training set is stored
		
		inputContents = mc.measurementCalculator(filePath)

		#saver = tf.train.import_meta_graph('./testModel.meta')
		#saver.restore(sess,tf.train.latest_checkpoint('./'))
		num_nodes_hl1 = 50 #500 #for now
		num_nodes_hl2 = 50#500 #for now
		num_nodes_hl3 = 50 #500 #for now
		num_nodes_hl4 = 50 #500 #for now
		num_nodes_hl5 = 50 #500 #for now
		num_classes_1 = 10 #100 #for now

		#Declare all the dictionaries
		#hlayerx_parameters contains the parameters which will generate hlayerx
		hlayer1_parameters = {'weights': tf.Variable(tf.random_normal([numMeasurements, num_nodes_hl1])), 
							  'biases': tf.Variable(tf.random_normal([1, num_nodes_hl1]))}
		
		hlayer2_parameters = {'weights': tf.Variable(tf.random_normal([num_nodes_hl2, num_nodes_hl1])), 
							  'biases': tf.Variable(tf.random_normal([1, num_nodes_hl2]))}
		
		hlayer3_parameters = {'weights': tf.Variable(tf.random_normal([num_nodes_hl3, num_nodes_hl2])), 
							  'biases': tf.Variable(tf.random_normal([1, num_nodes_hl3]))}
		
		hlayer4_parameters = {'weights': tf.Variable(tf.random_normal([num_nodes_hl4, num_nodes_hl3])), 
							  'biases': tf.Variable(tf.random_normal([1, num_nodes_hl4]))}
		
		hlayer5_parameters = {'weights': tf.Variable(tf.random_normal([num_nodes_hl5, num_nodes_hl4])), 
							  'biases': tf.Variable(tf.random_normal([1, num_nodes_hl5]))}
		
		output_layer_parameters =  {'weights': tf.Variable(tf.random_normal([num_nodes_hl5, num_classes_1])), 
								    'biases': tf.Variable(tf.random_normal([1, num_classes_1]))}


		hlayer1 = tf.add(tf.matmul(x, hlayer1_parameters['weights']), hlayer1_parameters['biases'])
		hlayer1 = tf.nn.relu(hlayer1)

		hlayer2 = tf.add(tf.matmul(hlayer1, hlayer2_parameters['weights']), hlayer2_parameters['biases'])
		hlayer2 = tf.nn.relu(hlayer2)

		hlayer3 = tf.add(tf.matmul(hlayer2, hlayer3_parameters['weights']), hlayer3_parameters['biases'])
		hlayer3 = tf.nn.relu(hlayer3)

		hlayer4 = tf.add(tf.matmul(hlayer3, hlayer4_parameters['weights']), hlayer4_parameters['biases'])
		hlayer4 = tf.nn.relu(hlayer4)

		hlayer5 = tf.add(tf.matmul(hlayer4, hlayer5_parameters['weights']), hlayer5_parameters['biases'])
		hlayer5 = tf.nn.relu(hlayer5)

		#No activation for final layer
		output_layer = tf.add(tf.matmul(hlayer5, output_layer_parameters['weights']), output_layer_parameters['biases'])
	#output_layer = tf.nn.relu(output_layer)
		with tf.Session() as sess:
			tf.train.Saver().restore(sess, "/tmp/model1.ckpt")
			print("Model restored")

			prediction = sess.run([output_layer], feed_dict = {x:inputContents, y:1})
			print("Prediction: ", prediction[0][0])			
			print("Rating: ", sess.run(tf.argmax(prediction[0][0])) + 1)

			'''writeFile = open("/home/justinhai/Desktop/johnshopkins/NoseJob/v19/weightsBiases201804232110.txt", 'w')
			writeFile.write("Weights Layer 1: " + str(sess.run([hlayer1_parameters['weights']], feed_dict = {x:inputContents, y:1})[0]) + '\n')
			writeFile.write("Biases Layer 1: "+ str(sess.run([hlayer1_parameters['biases']], feed_dict = {x:inputContents, y:1})[0]) + '\n')
			writeFile.write("Weights Layer 2: " + str(sess.run([hlayer2_parameters['weights']], feed_dict = {x:inputContents, y:1})[0]) + '\n')
			writeFile.write("Biases Layer 2: "+ str(sess.run([hlayer2_parameters['biases']], feed_dict = {x:inputContents, y:1})[0]) + '\n')
			writeFile.write("Weights Layer 3: " + str(sess.run([hlayer3_parameters['weights']], feed_dict = {x:inputContents, y:1})[0]) + '\n')
			writeFile.write("Biases Layer 3: "+ str(sess.run([hlayer3_parameters['biases']], feed_dict = {x:inputContents, y:1})[0]) + '\n')
			writeFile.write("Weights Layer 4: " + str(sess.run([hlayer4_parameters['weights']], feed_dict = {x:inputContents, y:1})[0]) + '\n')
			writeFile.write("Biases Layer 4: "+ str(sess.run([hlayer4_parameters['biases']], feed_dict = {x:inputContents, y:1})[0]) + '\n')
			writeFile.write("Weights Layer 5: " + str(sess.run([hlayer5_parameters['weights']], feed_dict = {x:inputContents, y:1})[0]) + '\n')
			writeFile.write("Biases Layer 5: "+ str(sess.run([hlayer5_parameters['biases']], feed_dict = {x:inputContents, y:1})[0]) + '\n')
			writeFile.write("Weights Output Layer: " + str(sess.run([output_layer_parameters['weights']], feed_dict = {x:inputContents, y:1})[0]) + '\n')
			writeFile.write("Biases Output Layer: "+ str(sess.run([output_layer_parameters['biases']], feed_dict = {x:inputContents, y:1})[0]) + '\n')
			writeFile.close()'''
			
			np.savetxt("weights1.csv", sess.run([hlayer1_parameters['weights']], feed_dict = {x:inputContents, y:1})[0])
			np.savetxt("biases1.csv", sess.run([hlayer1_parameters['biases']], feed_dict = {x:inputContents, y:1})[0])
			np.savetxt("weights2.csv", sess.run([hlayer2_parameters['weights']], feed_dict = {x:inputContents, y:1})[0])
			np.savetxt("biases2.csv", sess.run([hlayer2_parameters['biases']], feed_dict = {x:inputContents, y:1})[0])
			np.savetxt("weights3.csv", sess.run([hlayer3_parameters['weights']], feed_dict = {x:inputContents, y:1})[0])
			np.savetxt("biases3.csv", sess.run([hlayer3_parameters['biases']], feed_dict = {x:inputContents, y:1})[0])
			np.savetxt("weights4.csv", sess.run([hlayer4_parameters['weights']], feed_dict = {x:inputContents, y:1})[0])
			np.savetxt("biases4.csv", sess.run([hlayer4_parameters['biases']], feed_dict = {x:inputContents, y:1})[0])
			np.savetxt("weights5.csv", sess.run([hlayer5_parameters['weights']], feed_dict = {x:inputContents, y:1})[0])
			np.savetxt("biases5.csv", sess.run([hlayer5_parameters['biases']], feed_dict = {x:inputContents, y:1})[0])
			np.savetxt("weightsouter.csv", sess.run([output_layer_parameters['weights']], feed_dict = {x:inputContents, y:1})[0])
			np.savetxt("biasesoutside.csv", sess.run([output_layer_parameters['biases']], feed_dict = {x:inputContents, y:1})[0])
