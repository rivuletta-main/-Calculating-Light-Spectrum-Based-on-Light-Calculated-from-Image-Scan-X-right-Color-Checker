# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 11:54:28 2022

@author: rhaen
"""

from sklearn.neural_network import MLPRegressor
import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error, r2_score
import warnings
from sklearn.model_selection import train_test_split

warnings.filterwarnings("ignore")


df = pd.read_csv("Blue.csv")

#%%

print(df.head(9))
X = df[['r_org', 'g_org', 'b_org', 'r_cct', 'g_cct', 'b_cct']]
y = df['CCT']


#%%
X_train, X_test, y_train, y_test = train_test_split(X, y,random_state=42)


model = MLPRegressor(hidden_layer_sizes=(10, 5), activation='relu', solver='adam', alpha=0.001, batch_size='auto', learning_rate='constant', learning_rate_init=0.01, power_t=0.5, max_iter=1000, shuffle=True, random_state=None, tol=0.0001, verbose=False, warm_start=False, momentum=0.9, nesterovs_momentum=True, early_stopping=False, validation_fraction=0.1, beta_1=0.9, beta_2=0.999, epsilon=1e-08, n_iter_no_change=10)


model.fit(X_train, y_train)

predictions1 = model.predict(X_test)

y_actual = np.array(y_test.values.tolist())
predictions = np.array(predictions1)

print("Actual values = ",y_actual)
print("Predicted values = ",predictions)

mse = mean_squared_error(y_actual, predictions)
r2 = r2_score(y_actual, predictions)



# Sonuçları ekrana yazdırın
print("MSE:", mse)
print("R-kare:", r2)

#%%
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=5)
# İki gizli katmanlı bir yapay sinir ağı modeli oluşturun
model = MLPRegressor(hidden_layer_sizes=(10, 5),random_state=1, max_iter=500).fit(X_train, y_train)
# Modeli eğitin
model.fit(X_train, y_train)



from sklearn.model_selection import cross_validate
#from sklearn import cross_validation as CV

scores = cross_validate(model, X, y, cv=3, scoring='neg_mean_squared_error')
# K-fold cross validation ile model performansını ölçün
#scores = cross_val_score(model, X, y, cv=3)

# Sonuçları ekrana yazdırın
print("Cross validation skorları:", scores)
print("Ortalama skor:", np.mean(scores["test_score"]))
print("Standart sapma:", np.std(scores["test_score"]))