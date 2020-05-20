import pandas as pd
import file_sheet_name as fs
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt
from sklearn import svm

def show_result(test, pred, n):
    plt.subplot(3,3,n)
    plt.scatter(test, pred)
    plt.xticks(rotation=45)

def load_data():
    df = pd.read_excel(fs.inputFile, sheet_name=fs.sheetName1)
    df2 = df[~df['activity'].isin(['delta T((m))', 'T((1/2))'])].dropna()
    data = df2[['AlogP', 'AlogP98', 'Formal charge', 'Molecular solubility', 'HBA count',	'HBD count', 'Rotatable bonds', 'Metal atoms']]
    target = df2['activity']
    le = preprocessing.LabelEncoder()
    le.fit(target)
    labels = le.transform(target)
    return data, labels

def svm_predict():
    x, y = load_data()
    for i in range(1, 10):
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)
        clf = svm.SVC()  #RandomForestClassifier()
        clf.fit(x_train, y_train)
        rbf_score = clf.score(x_test, y_test)
        y_pred = clf.predict(x_test)
        show_result(y_test, y_pred, i)
        print('Mean accuracy ({}):  '.format(i), rbf_score)
    plt.show()

if __name__ == '__main__':
    svm_predict()