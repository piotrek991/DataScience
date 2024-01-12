from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn import metrics
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.feature_selection import RFE
from mrmr import mrmr_classif
import sklearn_relief as sr
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import f_classif
import time
import numpy as np



def selection_rfe(model, x_test_in, y_test_in, x_train_in, y_train_in, **kwargs) -> pd.DataFrame():
 final_data = list()
 if kwargs.get('model_n'):
  model_name = kwargs.get('model_n')
 else:
  model_name = 'not specified'

 selector = RFE(model, n_features_to_select=2, step=1)
 selector.fit(x_train_in, y_train_in)
 x_columns = x_train_in.columns


 for i in range(1, len(x_train_in.columns)):
  print(f'here calculating model with only {i} features selected')
  data_to_w = [col_name for col_name, ranked in zip(x_columns, selector.ranking_) if ranked <= i]

  # with open('ranked5.txt', 'w') as file:
  #  data_to_w_inner = [col_name + ':' + str(ranked) for col_name, ranked in zip(x_columns, selector.ranking_)]
  #  data_s = '\n'.join(data_to_w_inner)
  #  file.write(data_s)
  # time.sleep(10)

  x_train_after_sel = x_train_in.loc[:, data_to_w].to_numpy()
  x_test_after_sel = x_test_in.loc[:, data_to_w].to_numpy()
  model.fit(x_train_after_sel, y_train_in)


  y_pred = model.predict(x_test_after_sel)
  acc_score = metrics.accuracy_score(y_test_in, y_pred)

  final_data.append([model_name, 'RFE', i, acc_score])
 final_df = pd.DataFrame(columns=['Model', 'Selection Method', 'Number of features', 'Accuracy'], data = final_data)
 return final_df


def selection_mrmr(model, x_test_in, y_test_in, x_train_in, y_train_in, **kwargs) -> pd.DataFrame():
 final_data = list()
 if kwargs.get('model_n'):
  model_name = kwargs.get('model_n')
 else:
  model_name = 'not specified'
 for i in range(1,len(x_train_in.columns)):
  print(f'here calculating model with only {i} features selected')

  selected_features = mrmr_classif(X = x_train_in, y = y_train_in, K=i)
  x_train_after_sel = x_train_in.loc[:, selected_features].to_numpy()
  x_test_after_sel = x_test_in.loc[:, selected_features].to_numpy()

  model.fit(x_train_after_sel,y_train_in)
  y_pred = model.predict(x_test_after_sel)
  acc_score = metrics.accuracy_score(y_test_in, y_pred)

  final_data.append([model_name,'MRMR', i, acc_score])

 final_df = pd.DataFrame(columns = ['Model', 'Selection Method', 'Number of features', 'Accuracy'], data = final_data)
 return final_df

def selection_relieff(model, x_test_in, y_test_in, x_train_in, y_train_in) -> int:
 scaler = sr.ReliefF(n_features = 1)
 print('herer')
 scaler.fit(x_train_in.to_numpy(), y_train_in.to_numpy())
 x_train_after_sel = scaler.transform(x_train_in.to_numpy())
 x_test_after_sel = scaler.transform(x_test_in.to_numpy())
 model.fit(x_train_after_sel,y_train_in)
 y_pred = model.predict(x_test_after_sel)
 acc_score = metrics.accuracy_score(y_test_in, y_pred)
 return acc_score

def selection_kbest(model, x_test_in, y_test_in, x_train_in, y_train_in) -> int:
 scaler = SelectKBest(f_classif, k=2)
 print('herer')
 scaler.fit(x_train_in.to_numpy(), y_train_in.to_numpy())
 x_train_after_sel = scaler.transform(x_train_in.to_numpy())
 x_test_after_sel = scaler.transform(x_test_in.to_numpy())
 model.fit(x_train_after_sel,y_train_in)
 y_pred = model.predict(x_test_after_sel)
 acc_score = metrics.accuracy_score(y_test_in, y_pred)
 return acc_score

def run_elbow_method(model, x_test_in, y_test_in, x_train_in, y_train_in) -> int:
 model.fit(x_train_in, y_train_in)

 f1_scores = list()
 features = list()

 num_features_start = x_train_in.shape[1]

 while x_train_in.shape[1] > 0:
  print(f'Training model on the {x_train_in.shape[1]} most important features')
  print(type(x_test_in))
  feature_importance = model.feature_importances_
  y_pred = model.predict(x_test_in)
  f1 = metrics.f1_score(y_test_in, y_pred)
  f1_scores.append(f1)
  features.append(x_train_in.columns)

  least_important_idx = feature_importance.argmin()
  x_train_in = x_train_in.drop(x_train_in.columns[least_important_idx], axis=1)
  x_test_in = x_test_in.drop(x_test_in.columns[least_important_idx], axis=1)

  model.fit(x_train_in,y_train_in)




if __name__ == '__main__':
 data_dlbcl_train = pd.read_csv('dlbcl_training.csv')
 data_dlbcl_test = pd.read_csv('dlbcl_testing.csv', delimiter=';')

 x_train, y_train = data_dlbcl_train.iloc[:,:-1], data_dlbcl_train.iloc[:,-1]
 x_test, y_test = data_dlbcl_test.iloc[:,:-1], data_dlbcl_test.iloc[:,-1]

 knn = KNeighborsClassifier(n_neighbors=5, metric='euclidean')

 clf = DecisionTreeClassifier()

 scaler = StandardScaler()
 scaler.fit(x_train)
 svc = SVC(gamma='auto', probability=True)

 data = selection_relieff(clf, x_test, y_test, x_train, y_train)
 # with pd.ExcelWriter('resultsver2.xlsx') as writer:
 #  data.to_excel(writer, sheet_name='MRMR selection', index=False)