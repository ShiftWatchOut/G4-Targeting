
import numpy as np

import tools


sheetName1 = "FRET"
sheetName2 = "FRET统计"
sheetName3 = "TRAP"
sheetName4 = "Cytotoxictity"
inputFile = "data.xlsx"

if __name__ == '__main__':
    kdata = tools.getData(inputFile, sheetName4)
    # print(kdata)
    tools.my_kmeans(kdata)

    # 显示图形
    # X = np.linspace(-np.pi, np.pi, 256, endpoint=True)

    # C, S = np.cos(X), np.sin(X)

    # plt.plot(X, C)
    # plt.plot(X, S)
    # plt.savefig('matplotlib.png')