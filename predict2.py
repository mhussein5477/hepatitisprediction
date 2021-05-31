import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

dataset = pd.read_csv("dataset_55_hepatitis.csv")

replacements = {'no': 0,
               'yes': 1,
               'DIE': 0,
               'LIVE': 1,
               '?': np.nan,
               'female': 0,
               'male': 1}

dataset.replace(replacements, inplace = True)
dataset = dataset.astype(float)
dataset[[ 'AGE' ,'ALBUMIN', 'ALK_PHOSPHATE', 'BILIRUBIN', 'SGOT']] = dataset[['AGE' , 'ALBUMIN','ALK_PHOSPHATE', 'BILIRUBIN', 'SGOT']].applymap(np.log)

#shape
print(dataset.shape)

print(dataset.head(10))

print(dataset.describe())

"""### Drop all the columns with `NAN` values"""

dataset = dataset.dropna()

#visualize
plt.xlabel("Age")
plt.ylabel("Levels")

plt.scatter(dataset['AGE'],dataset['BILIRUBIN'])

x = dataset[['AGE' , 'ALBUMIN' , 'ALK_PHOSPHATE' , 'BILIRUBIN' , 'SGOT' , 'LIVER_BIG' , 'STEROID' , 'ANTIVIRALS' , 'FATIGUE' , 'ANOREXIA', 'LIVER_FIRM',
                     'SPLEEN_PALPABLE', 'SPIDERS', 'ASCITES', 'VARICES' ]]
y = dataset['Class']

x_train , x_test , y_train , y_test = train_test_split(x, y, test_size=0.2,  random_state = 42)
model = GaussianNB()

model.fit(x_train, y_train)
predictions = model.predict(x_test)



#Predict Output
predicted= model.predict([[ 23 , 1 , 0, 10 , 0, 0 , 0 , 0, 0, 0, 0, 0, 0,0 ,0 ]]) # 0:Overcast, 2:Mild


print(accuracy_score(y_test,predictions))
print(predicted)