import librosa
import os
import numpy as np
from numpy import random


def write_wav_into_list_test_or_train(test_path):

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


def init_weights(number_of_inputs1, number_of_neurons1, number_of_inputs2, number_of_neurons2): #8000, 100, 100, 10
    weights1 = 0.2*np.random.rand(number_of_inputs1, number_of_neurons1)-0.1
    weights2 = 0.2*np.random.rand(number_of_inputs2, number_of_neurons2)-0.1
    return weights1, weights2


def compute_outputs(weights1, weight2, input_data):
    #beta = 5
    u1 = np.matmul(weights1.transpose(), input_data.transpose())
    #y1 = 1/(1+np.exp(-1*beta*u1))
    y1 = u1 * (u1 > 0)
    u2 = np.matmul(weight2.transpose(), y1)
    #y2 = 1/(1+np.exp(-1*beta*u2))
    y2 = u2 * (u2 > 0)
    return y1, y2


def train(weights_before1, weights_before2, train_data, epochs):
    desired_outputs = np.eye(10)
    learning_coeff = 0.1
    weights_learning1 = weights_before1
    weights_learning2 = weights_before2
    for i in range(epochs):
        input_digit = random.randint(0, 9)  # drawing random digit 0-9
        input_digit_sample = random.randint(0, 100)  # drawing random digit sample, there is 250 versions of each number
        input_learning = train_data[input_digit][input_digit_sample]  # choosing input digit sample
        output_of_network1, output_of_network2 = compute_outputs(weights_learning1, weights_learning2, input_learning)  # computes network output
        output_error2 = desired_outputs[input_digit] - output_of_network2
        output_error1 = np.matmul(weights_learning2, output_error2)
        input_learning = input_learning.reshape(8000, 1)
        output_error1 = output_error1.reshape(80, 1)
        weights1_adjust = learning_coeff*np.matmul(input_learning, output_error1.transpose())
        output_of_network1 = output_of_network1.reshape(80, 1)
        output_error2 = output_error2.reshape(10, 1)
        weights2_adjust = learning_coeff*np.matmul(output_of_network1, output_error2.transpose())
        weights_learning1 = weights_learning1 + weights1_adjust
        weights_learning2 = weights_learning2 + weights2_adjust
    weights1_after_learning = weights_learning1
    weights2_after_learning = weights_learning2
    return weights1_after_learning, weights2_after_learning

def check(weights1_after_learning, weights2_after_learning, test_data, n):
    count = 0
    for i in range(n):
        input_digit_test = random.randint(0, 9)  # drawing random digit 0-9
        input_digit_sample_test = random.randint(101, 200)  # drawing random sample of on 50 possible in test data
        y1, y2 = compute_outputs(weights1_after_learning, weights2_after_learning, test_data[input_digit_test][input_digit_sample_test])
        print("Number: ", input_digit_test)
        print("Sample: ", input_digit_sample_test)
        print("Calculated output: ", y2)
        if y2[input_digit_test] == max(y2):
            count = count + 1
        else:
            count = count
    return (count/n)*100

if __name__ == '__main__':
    train_path = '/data_train/'
    test_path = '/data_test/'

    train_data = write_wav_into_list_test_or_train(train_path)
    test_data = write_wav_into_list_test_or_train(test_path)

    weights_before1, weights_before2 = init_weights(8000, 80, 80, 10)

    weights1_after_learning, weights2_after_learning = train(weights_before1, weights_before2, train_data, 500)

    efficiency = check(weights1_after_learning, weights2_after_learning, train_data, 1000)
    print("Efficiency after learning: ", efficiency)
