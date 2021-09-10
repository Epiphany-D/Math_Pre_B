import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression


def my_fit(x, y, spot_c, line_c, name, label, marker, mode=0):
    if mode == 0:
        reg = LinearRegression().fit(x, y)
    # print(label + '_' + name + ': ')
    # print("一元回归方程为:  Y = %.4fX + (%.4f)" % (reg.coef_[0][0], reg.intercept_[0]))
    # print("R平方为: %.6s" % reg.score(x, y))
    rst_dic = {"催化剂组合编号": label, "名称": name, "斜率": "%.4f" % (reg.coef_[0][0]), "截距": "%.4f" % (reg.intercept_[0]),
               "R^2": "%.6s" % (reg.score(x, y))}
    plt.scatter(x, y, color=spot_c, marker=marker)
    plt.plot(x, reg.predict(x), color=line_c, linewidth=1)
    return rst_dic


def fig_cfg():
    plt.ylabel("Percentage")
    plt.xlabel("Temperature")
    plt.xlim([250, 400])
    plt.ylim([0, 100])

    # plt.legend(loc="upper left")  # 设置图例位置


df = pd.read_csv("file01.csv")  # input
# 清洗数据
var = df.loc[:, ["温度", "乙醇转化率", "C4烯烃选择性", "催化剂组合编号", "催化剂组合"]]
com_label = list(set(df["催化剂组合编号"]))

data = dict()

with open("img_01/data.csv", 'w', encoding='utf-8', newline="") as f:
    #     heads = ['催化剂组合编号', '名称', '斜率', '截距', 'R^2']  # 表头
    #     writer = csv.DictWriter(f, fieldnames=heads)
    #     writer.writeheader()

    for label in com_label:
        # label = "A1"
        var_tmp = var[var["催化剂组合编号"] == label]
        X = var_tmp["温度"]
        y_t = var_tmp["乙醇转化率"]
        y_s = var_tmp["C4烯烃选择性"]

        x = np.asarray(X).reshape(len(X), 1)
        y1 = np.asarray(y_t).reshape(len(y_t), 1)
        y2 = np.asarray(y_s).reshape(len(y_s), 1)

        data_y1 = dict()
        data_y2 = dict()
        # my_fit(x, y2, "b", "b", "C4烯烃选择性", label, 's')
        my_fit(x[0:4], y1[0:4], "r", "r", "乙醇转化率", label, '^')
        # writer.writerow(my_fit(x, y1, "r", "r", "乙醇转化率", label, '^'))
        # writer.writerow(my_fit(x, y2, "b", "b", "C4烯烃选择性", label, 's'))

        # print('*' * 40)
        fig_cfg()

        # output
        plt.savefig("img_01/e_" + label + ".png")
        plt.close()
