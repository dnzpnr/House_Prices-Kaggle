
import numpy as np
import pandas as pd
import statsmodels.api as sm
import seaborn as sns
from sklearn.preprocessing import scale
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error

'''warningleri gostermesin istiyorsan asagidaki kodu yaz'''
from warnings import filterwarnings
filterwarnings('ignore')

model_train = pd.read_csv('model_train.csv')

df = model_train.copy()

df.info(verbose=True)

df.head()

'''Simdi ML modellerimizi kuralim. Birden fazla model kuracagim ve once train
 setinde test edecegim. En iyi sonucu hangi modelden alirsam o modeli test 
 setinde calistiracagim.'''

y = df['SalePrice']
x = df.drop(['SalePrice'],axis=1)

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.15,random_state = 42)

'''degiskenlerimize normalizasyon uygulayalim'''

from sklearn.preprocessing import MinMaxScaler
mms = MinMaxScaler()
x_train_normed = mms.fit_transform(x_train)
x_test_normed= mms.fit_transform(x_test)

# 1- KNN

from sklearn.neighbors import KNeighborsRegressor

knn = KNeighborsRegressor()
knn_params = {'n_neighbors': np.arange(1,30,1)}
knn_ = GridSearchCV(knn, knn_params, cv = 15).fit(x_train_normed,y_train)
knn_.best_params_
knn_cv = KNeighborsRegressor(n_neighbors=8).fit(x_train_normed,y_train).predict(x_test_normed)
skore1 = np.sqrt(mean_squared_error(knn_cv,y_test))

# 2- SVR

from sklearn.svm import SVR

svr = SVR('rbf')
svr_params = {'C': [0.1,0.2,0.4,0.8,1,2,4,5,7,8,20]}
#svr_ = GridSearchCV(svr,svr_params,cv=15).fit(x_train_normed,y_train)
#svr_.best_params_
svr_cv = SVR(C=20).fit(x_train_normed,y_train).predict(x_test_normed)
skore2 = np.sqrt(mean_squared_error(svr_cv,y_test))

# 3- MLP

from sklearn.neural_network import MLPRegressor

mlp = MLPRegressor()
mlp_params = {'hidden_layer_sizes':[[20,20],[50,50],[100],[100,100],[100,50],[150,100]],
              'activation':['logistic','relu','tanh'],
              'solver':['lbfgs','sgd','adam'],
              'alpha':[0.0001,0.001,0.01,0.1,1],
              'learning_rate':['constant','invscaling','adaptive']}
#mlp_ = GridSearchCV(mlp,mlp_params,cv=15).fit(x_train_normed,y_train)
#mlp_.best_params_
mlp_cv = MLPRegressor(hidden_layer_sizes=[20,20] , activation='relu' ,solver='lbfgs' ,alpha= 0.01, learning_rate= 'constant').fit(x_train_normed,y_train).predict(x_test_normed)
skore3 = np.sqrt(mean_squared_error(mlp_cv,y_test))

# 4- CART

from sklearn.tree import DecisionTreeRegressor

cart = DecisionTreeRegressor()
cart_params = {'min_samples_split':range(1,15),
               'max_leaf_nodes':range(5,10)}
#cart_ = GridSearchCV(cart,cart_params,cv=15).fit(x_train_normed,y_train)
#cart_.best_params_
cart_cv = DecisionTreeRegressor(min_samples_split=2 ,max_leaf_nodes= 9).fit(x_train_normed,y_train).predict(x_test_normed)
skore4 = np.sqrt(mean_squared_error(cart_cv,y_test))

# 5- BAGGED TREES

from sklearn.ensemble import BaggingRegressor

br = BaggingRegressor()
br_params = {'n_estimators':[500,1000],
             'max_features':[5,10,20,100,130]}
#br_ = GridSearchCV(br,br_params,cv=15).fit(x_train_normed,y_train)
#br_.best_params_
br_cv = BaggingRegressor(n_estimators= 500,max_features= 100).fit(x_train_normed,y_train).predict(x_test_normed)
skore5 = np.sqrt(mean_squared_error(br_cv,y_test))


# 6- RF

from sklearn.ensemble import  RandomForestRegressor

rf = RandomForestRegressor()
rf_params = {'n_estimators':[100,200,500,1000],
             'max_features':['auto','sqrt','log2']}
#rf_ = GridSearchCV(rf,rf_params,cv=15).fit(x_train_normed,y_train)
#rf_.best_params_
rf_cv = RandomForestRegressor(n_estimators= 1000, max_features= 'sqrt').fit(x_train_normed,y_train).predict(x_test_normed)
skore6 = np.sqrt(mean_squared_error(rf_cv,y_test))

# 7- GBM

from sklearn.ensemble import GradientBoostingRegressor

gbm = GradientBoostingRegressor()
gbm_params = {'n_estimators': [100,200,500,1000],
          'max_depth': [2,4,7,10],
          'min_samples_split': [1,3,5,6],
          'learning_rate': [0.01,0.1,1],
          'loss': ['ls','lad','huber','quantile']}
#gbm_ = GridSearchCV(gbm,gbm_params,cv=15).fit(x_train_normed,y_train)
#gbm_.best_params_
gbm_cv = GradientBoostingRegressor(n_estimators= 1000,max_depth= 7, min_samples_split=3 ,learning_rate= 0.1,loss= 'lad').fit(x_train_normed,y_train).predict(x_test_normed)
skore7 = np.sqrt(mean_squared_error(gbm_cv,y_test))

# 8- XGBOOST

from xgboost import XGBRegressor

xgb = XGBRegressor()
xgb_params = {'n_estimators': [200,500,1000],
              'max_depth': [2,4,7,10],
              'learning_rate': [0.01,0.1,1]}
xgb_ = GridSearchCV(xgb,xgb_params,cv=15).fit(x_train_normed,y_train)
xgb_.best_params_
xgb_cv = XGBRegressor(n_estimators=1000 ,max_depth= 2,learning_rate= 0.1).fit(x_train_normed,y_train).predict(x_test_normed)
skore8 = np.sqrt(mean_squared_error(xgb_cv,y_test))

model_test = pd.read_csv('model_test.csv')
test_normed = mms.fit_transform(model_test.copy())
x_train_ = df.drop('SalePrice',axis=1)
y_train_ = df['SalePrice']
x_train_normed_ = mms.fit_transform(x_train_)

xgb_cv_ = XGBRegressor(n_estimators=500 ,max_depth= 4,learning_rate= 0.01).fit(x_train_normed_,y_train_).predict(test_normed)

sp = pd.read_csv('sample_submission.csv')
x = pd.DataFrame(xgb_cv_)
sp.loc[:,'SalePrice'] = x.iloc[:,0]

sp.to_csv('sample_submission3.csv',index=False)

