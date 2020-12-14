import librosa
import os
import numpy as np
from numpy import random


def write_wav_into_list_test_or_train(path):

    x0test = []
    x1test = []
    x2test = []
    x3test = []
    x4test = []
    x5test = []
    x6test = []
    x7test = []
    x8test = []
    x9test = []
    x_test = []

    for filename in os.listdir(test_path):
        x, s = librosa.load(test_path+filename, sr=8000)

        if len(x) > 8000:
            raise ValueError("data length cannot exceed padding length.")
        elif len(x) < 8000:
            option = "padding_left_right"
            #option = "padding_only_right"
            if option == "padding_left_right":
                data = np.zeros(8000)
                offset = np.random.randint(low=0, high=8000 - len(x))
                data[offset:offset + len(x)] = x
                x = data
            else:
                data_size = len(x)
                x = np.pad(x, (0, 8000 - data_size), 'constant')
        elif len(x) == 8000:
            # nothing to do here
            x = x

        #x = ((x - np.min(x)) / np.ptp(x))/10  # 0.0-0.1 normalization

        if filename[0] == "0":
            x0test.append(x)
        elif filename[0] == "1":
            x1test.append(x)
        elif filename[0] == "2":
            x2test.append(x)
        elif filename[0] == "3":
            x3test.append(x)
        elif filename[0] == "4":
            x4test.append(x)
        elif filename[0] == "5":
            x5test.append(x)
        elif filename[0] == "6":
            x6test.append(x)
        elif filename[0] == "7":
            x7test.append(x)
        elif filename[0] == "8":
            x8test.append(x)
        else:
            x9test.append(x)
        x_test = [x0test, x1test, x2test, x3test, x4test, x5test, x6test, x7test, x8test, x9test]
    return x_test

#print("Cały test: ", X_test)
#print("Tylko 0: ", X_test[0])
#print("Tylko pierwsze 0: ", X_test[0][0] )
#print("Pierwszy element pierwszego zera: ", X_test[0][0][0])


def init_weights(number_of_inputs, number_of_neurons):
    weights = 0.2*np.random.rand(number_of_inputs, number_of_neurons)-0.1
    return weights


def compute_outputs(weights, input_data):  # beta = 5
    u = np.matmul(weights.transpose(), input_data.transpose())
    y = u * (u>0)
    #y = 1/(1+np.exp(-0.1*u))
    return y


def train(weights_before, train_data, epochs):
    desired_outputs = np.eye(10)
    learning_coeff = 0.6
    weights_learning = weights_before
    print(weights_before)
    for i in range(epochs):
        input_digit = random.randint(0, 9)  # drawing random digit 0-9
        input_digit_sample = random.randint(0, 249)  # drawing random digit sample, there is 250 versions of each number
        input_learning = train_data[input_digit][input_digit_sample]  # choosing input digit sample
        output_of_network = compute_outputs(weights_learning, input_learning)  # computes network output
        output_error = desired_outputs[input_digit]-output_of_network  # computes network error
        input_learning = input_learning.reshape(1, 8000)
        output_error = output_error.reshape(1, 10)
        weights_adjust = learning_coeff*np.matmul(input_learning.transpose(), output_error)
        weights_learning = weights_learning + weights_adjust  # adds correction to weights
    weights_after_learning = weights_learning  # assignment of weights after learning to the new variable
    return weights_after_learning


def check(weights_after_learning, test_data, n):
    count = 0
    for i in range(n):
        input_digit_test = random.randint(0, 9)  # drawing random digit 0-9
        input_digit_sample_test = random.randint(0, 249)  # drawing random sample of on 50 possible in test data
        x = compute_outputs(weights_after_learning, test_data[input_digit_test][input_digit_sample_test])
        #print("Number: ", input_digit_test)
        #print("Sample: ", input_digit_sample_test)
        #print("Calculated output: ", x)
        if x[input_digit_test] == max(x):
            count = count + 1
        else:
            count = count
    return (count/n)*100


if __name__ == '__main__':
    train_path = '/Users/maciejnawrocki/Desktop/python/project/data_train/'
    test_path = '/Users/maciejnawrocki/Desktop/python/project/data_test/'

    train_data = write_wav_into_list_test_or_train(train_path)
    test_data = write_wav_into_list_test_or_train(test_path)

    weights_before = init_weights(8000, 10)

    weights_after_learning = train(weights_before, train_data, 5000)

    efficiency = check(weights_after_learning, train_data, 1000)
    print("Efficiency after learning: ", efficiency)
