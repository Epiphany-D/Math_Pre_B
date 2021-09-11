import csv

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression


def line_fit(x, y, spot_c, line_c, name, label, marker):
    reg = LinearRegression().fit(x, y)
    print(label + '_' + name + ': ')
    # print("一元回归方程为:  Y = %.4fX + (%.4f)" % (reg.coef_[0][0], reg.intercept_[0]))
    # print("R平方为: %.6s" % reg.score(x, y))
    rst_dic = {"催化剂组合编号": label, "名称": name, "斜率": "%.4f" % (reg.coef_[0][0]), "截距": "%.4f" % (reg.intercept_[0]),
               "R^2": "%.6s" % (reg.score(x, y))}
    g1 = plt.scatter(x, y, color=spot_c, marker=marker)
    plt.plot(x, reg.predict(x), color=line_c, linewidth=1)
    return rst_dic


def poly_fit(x, y, spot_c, line_c, name, label, marker):
    coef = np.polyfit(x, y, 2)
    # print(coef)
    y_fit = np.polyval(coef, x)
    g1 = plt.scatter(x, y, color=spot_c, marker=marker)
    plt.plot(x, y_fit, 'g')
    correlation = np.corrcoef(y, y_fit)[0, 1]  # 相关系数
    R = correlation ** 2  # R方
    rst_dic = {"催化剂组合编号": label, "名称": name,
               'a': '%.4f' % float(coef[0]),
               'b': '%.4f' % float(coef[1]),
               'c': '%.4f' % float(coef[2]),
               "R^2": "%.6s" % R}

    return rst_dic


def fig_cfg():
    plt.xlim([250, 400])
    plt.ylim([0, 60])
    # plt.axis('off')

    frame = plt.gca()
    # y 轴不可见
    frame.axes.get_yaxis().set_visible(False)
    # x 轴不可见
    frame.axes.get_xaxis().set_visible(False)
    # plt.legend(loc="upper left")  # 设置图例位置


df = pd.read_csv("file01.csv")  # input
# 清洗数据
var = df.loc[:, ["温度", "乙醇转化率", "C4烯烃选择性", "催化剂组合编号", "催化剂组合"]]
com_label = list(set(df["催化剂组合编号"]))

data = dict()

with open("img_01/data.csv", 'w', newline="") as f:
    heads = ['催化剂组合编号', '名称', 'a', 'b', 'c', 'R^2']  # 表头
    writer = csv.DictWriter(f, fieldnames=heads)
    writer.writeheader()
    i = 0
    for label in com_label:
        # label = "A1"
        var_tmp = var[var["催化剂组合编号"] == label]
        X = var_tmp["温度"]
        y_t = var_tmp["乙醇转化率"]
        y_s = var_tmp["C4烯烃选择性"]

        x = np.asarray(X)
        y1 = np.asarray(y_t)
        y2 = np.asarray(y_s)

        data_y1 = dict()
        data_y2 = dict()

        # 子图
        plt.subplot(5, 5, i + 1)
        # 线性拟合
        # writer.writerow(line_fit(x, y1, "r", "r", "乙醇转化率", label, '^'))
        # writer.writerow(line_fit(x, y2, "b", "b", "C4烯烃选择性", label, 's'))
        # 多项式拟合
        # writer.writerow(double_fit(x, y1, "r", "r", "乙醇转化率", label, '^'))
        # writer.writerow(poly_fit(x, y2, "b", "b", "C4烯烃选择性", label, 's'))
        fig_cfg()

        # output
        # plt.savefig("img_01/" + label + ".png")
        i = (i + 1 % 5)
plt.show()
