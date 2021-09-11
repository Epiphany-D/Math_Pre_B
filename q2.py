import csv


def fun(dic, k1, k2, item, data1, data2):
    dic[k1] = (dic[k1] * item + float(data1)) / (item + 1)
    dic[k2] = (dic[k2] * item + float(data2)) / (item + 1)
    return dic, item + 1


file = 'img_01/data.csv'
with open(file, 'r') as f:
    A = {'e_mean': 0, 'C4_mean': 0, 'eR_mean': 0, 'C4R_mean': 0}
    B = {'e_mean': 0, 'C4_mean': 0, 'eR_mean': 0, 'C4R_mean': 0}
    itemAe, itemBe, itemAC4, itemBC4 = 0, 0, 0, 0
    # Ae_list, Be_list, Ac4_list, Bc4_list, AeR_list, BeRlist, Ac4R_list, Bc4R_list = list(), list(), list(), list()
    reader = csv.reader(f)
    for line in reader:
        if line[1] == '乙醇转化率':
            if 'A' in line[0]:
                A, itemAe = fun(A, 'e_mean', 'eR_mean', itemAe, line[2], line[4])
            else:
                B, itemBe = fun(B, 'e_mean', 'eR_mean', itemBe, line[2], line[4])
        else:
            if 'A' in line[0]:
                A, itemAC4 = fun(A, 'C4_mean', 'C4R_mean', itemAC4, line[2], line[4])
            else:
                B, itemBC4 = fun(B, 'C4_mean', 'C4R_mean', itemBC4, line[2], line[4])
with open('img_01/mean.json', 'w', encoding='utf-8') as f:
    f.write(str(A))
    f.write("*" * 20)
    f.write(str(B))
    print(A)
    print(B)
