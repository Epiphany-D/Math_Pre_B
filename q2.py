import csv

import numpy as np

file = 'img_01/data.csv'
with open(file, 'r', encoding='utf-8') as f:
    Ae_list, Be_list, Ac4_list, Bc4_list = list(), list(), list(), list()
    reader = csv.reader(f)
    for line in reader:
        if line[1] == '乙醇转化率':
            if 'A' in line[0]:
                Ae_list.append(float(line[2]))
            else:
                Be_list.append(float(line[2]))
        else:
            if 'A' in line[0]:
                Ac4_list.append(float(line[2]))
            else:
                Bc4_list.append(float(line[2]))
    print('Ae_max:%.4f' % np.max(Ae_list))
    print('Be_max:%.4f' % np.max(Be_list))
    print('Ac4_max:%.4f' % np.max(Ac4_list))
    print('Bc4_max:%.4f' % np.max(Bc4_list))
    # print('Ae_mean:%.4f' % (np.mean(Ae_list)))
    # print('Ae_std:%.4f' % (np.std(Ae_list)))
    # print('Ac4_mean:%.4f' % (np.mean(Ac4_list)))
    # print('Ac4_std:%.4f' % (np.std(Ac4_list)))
    # print('*' * 15)
    # print('Be_mean:%.4f' % (np.mean(Be_list)))
    # print('Be_std:%.4f' % (np.std(Be_list)))
    # print('Bc4_mean:%.4f' % (np.mean(Bc4_list)))
    # print('Bc4_std:%.4f' % (np.std(Bc4_list)))
