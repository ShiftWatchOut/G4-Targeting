import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt


def getData(excelName, sheetName=None):       #数据预处理
    df = pd.read_excel(excelName, skiprows=[], sheet_name=sheetName, keep_default_na=None)
    data = df[[
        'Ligand ID',
        'AlogP',
        'AlogP98',
        'Molecular solubility',
        'HBA count',
        'HBD count',
        'Rotatable bonds'
    ]]
    data = data[(data['AlogP'] != '')]  #获取到第四个表的非空行
    # return data
    return pd.DataFrame([
        # data['Ligand ID'],
        pd.to_numeric(data['AlogP'], errors='coerce').fillna(0),
        pd.to_numeric(data['AlogP98'], errors='coerce').fillna(0),
        pd.to_numeric(data['Molecular solubility'], errors='coerce').fillna(0),
        pd.to_numeric(data['HBA count'], errors='coerce').fillna(0),
        pd.to_numeric(data['HBD count'], errors='coerce').fillna(0),
        pd.to_numeric(data['Rotatable bonds'], errors='coerce').fillna(0),
    ]).T


sheetName1 = "FRET"
sheetName2 = "FRET统计"
sheetName3 = "TRAP"
sheetName4 = "Cytotoxictity"
anaData = "data.xlsx"

if __name__ == '__main__':
    kdata = getData(anaData, sheetName4)
    # print(kdata)
    kmodel = KMeans(n_clusters=5, n_jobs=4).fit(kdata)  #n_jobs是并行数，一般等于CPU数较好

    label = pd.Series(kmodel.labels_)  # 各样本的类别
    num = pd.Series(kmodel.labels_).value_counts()  # 统计各样本对应的类别的数目
    center = pd.DataFrame(kmodel.cluster_centers_)  # 找出聚类中心
    print(label, num, center)

    # 显示图形
    # X = np.linspace(-np.pi, np.pi, 256, endpoint=True)

    # C, S = np.cos(X), np.sin(X)

    # plt.plot(X, C)
    # plt.plot(X, S)
    plt.savefig('matplotlib.png')