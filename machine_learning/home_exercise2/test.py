import numpy as np
import pandas as pd
import os
# Transformation
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import power_transform
from sklearn.pipeline import Pipeline
# Feature Selection
import sklearn_relief as sr
# Models
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

if __name__ == '__main__':
    df_amp = pd.read_csv('Amprion.csv')
    dates = df_amp['Date']
    df_amp = df_amp.T
    df_amp = df_amp[1:]
    df_amp.columns = [dates]

    df_amp.reset_index(drop=True, inplace=True)

    scaler = MinMaxScaler()
    print(df_amp)
    df_amp = power_transform(df_amp, method='yeo-johnson')
    df_amp = scaler.fit_transform(df_amp)
    X = df_amp[:,0:396]
    y = df_amp[:,396]
    print(y)
    X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.3, random_state = 0)
    #r = sr.RReliefF(n_features = 20)
    #print(r.fit_transform(X_train,y_train))