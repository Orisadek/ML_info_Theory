import json
import numpy as np  # check out how to install numpy
from utils import load, plot_sample

# =========================================
#       Homework on K-Nearest Neighbors
# =========================================
# Course: Introduction to Information Theory


ID = '000000000'

Xtrain, Ytrain, Xvalid, Yvalid, Xtest = load('MNIST_3_and_5.mat')  # load data
k = 19  # chosen k
len_of_sample = 1522  # length of the vector validate and train
len_of_test = 1902 # length of the vector test


def check_what_group(arr, group_of_3_group, group_of_5_group): # classify group
    dict_distance = {}
    count_3 = 0
    count_5 = 0
    z = 0
    fl = 1
    while fl:
        fl = 0
        if z < len(group_of_3_group):
            distance_3 = ((np.linalg.norm(group_of_3_group[z] - arr)) ** 2) / len_of_sample
            dict_distance[distance_3] = 3
            fl = 1
        if z < len(group_of_5_group):
            distance_5 = ((np.linalg.norm(group_of_5_group[z] - arr)) ** 2) / len_of_sample
            dict_distance[distance_5] = 5
            fl = 1
        z += 1

    sorted_arr = sorted(list(dict_distance.keys()))
    for j in range(k):
        if dict_distance[sorted_arr[j]] == 3:
            count_3 += 1
        else:
            count_5 += 1

    if count_3 <= count_5:
        return 5
    else:
        return 3


def train_data(): #create groups according to the algo'
    group_of_5_local = []
    group_of_3_local = []
    for j in range(len_of_sample):
        if Ytrain[j][0] == 3:
            group_of_3_local.append(Xtrain[j, :])
        else:
            group_of_5_local.append(Xtrain[j, :])

    return group_of_3_local, group_of_5_local


def validate_data(): # validate the data => check the algo'
    counter = 0
    for i in range(len_of_sample):
        ans_valid = check_what_group(Xvalid[i, :], group_of_3, group_of_5)
        if ans_valid == Yvalid[i][0]:
            counter += 1


group_of_3, group_of_5 = train_data()
validate_data()


def test_data(): # test the actual data and return the solutions
    y_test_tmp = []
    for i_y_test in range(len_of_test):
        test_val = check_what_group(Xtest[i_y_test, :], group_of_3, group_of_5)
        y_test_tmp.append(test_val)
    return y_test_tmp


Ytest = np.array(test_data()) #save the arr

print('saving')
np.savetxt(f'{ID}.txt', Ytest, delimiter=", ", fmt='%i')
print('done')
