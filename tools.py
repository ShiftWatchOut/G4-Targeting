import pandas as pd
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.cluster import KMeans


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

def my_kmeans(datafrm):
    # 2d、3d PCA
    pca = PCA(n_components=3).fit(datafrm)
    X = pca.transform(datafrm)
    # print(pca.explained_variance_ratio_, pca.singular_values_)
    # print(X)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(X[:, 0], X[:, 1], X[:, 1])
    # plt.show()
    # plt.scatter(X[:,0], X[:,1])
    plt.savefig('matplot.png')


    # KMeans 聚类
    # k_model = KMeans(n_clusters=5, n_jobs=4).fit(pca)
    # label = pd.Series(k_model.labels_)  # 各样本的类别
    # num = pd.Series(k_model.labels_).value_counts()  # 统计各样本对应的类别的数目
    # center = pd.DataFrame(k_model.cluster_centers_)  # 找出聚类中心
    # print(label, num, center)