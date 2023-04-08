from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression
import pandas as pd
from sklearn.neural_network import MLPRegressor
import numpy as np
import pandas as pd
from sklearn.metrics import r2_score
import warnings
from sklearn.model_selection import train_test_split





df = pd.read_csv('Blue.csv')

print(df.head(9))
X = df[['r_org', 'g_org', 'b_org', 'r_cct', 'g_cct', 'b_cct']]
y = df['CCT']
from sklearn.linear_model import LinearRegression

model = LinearRegression()

model.fit(X, y)

y_pred = model.predict(X)
from sklearn.metrics import mean_squared_error

mse = mean_squared_error(y, y_pred)
print(f'Ortalama Kare Hata (MSE): {mse:.2f}')