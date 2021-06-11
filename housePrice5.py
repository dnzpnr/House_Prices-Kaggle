
import numpy as np
import pandas as pd
import statsmodels.api as sm
import seaborn as sns
from sklearn.preprocessing import scale
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
from sklearn.metrics import roc_auc_score,roc_curve
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error

'''warningleri gostermesin istiyorsan asagidaki kodu yaz'''
from warnings import filterwarnings
filterwarnings('ignore')

model_train = pd.read_csv('model_train.csv')

model_train.head()

model_train.info(verbose=True)

'''Bu sefer fiyata en cok etkisi olacagini dusundugum degiskenleri secerek model olusturacagim.'''

df = model_train.iloc[:,[2,5,8,11,13,14,17,28,30,32,36,37,38,39,107]].copy()

df.head()

df.info()

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
knn_params = {'n_neighbors': np.arange(1,15,1)}
knn_ = GridSearchCV(knn, knn_params, cv = 15).fit(x_train_normed,y_train)
knn_.best_params_
knn_cv = KNeighborsRegressor(n_neighbors=14).fit(x_train_normed,y_train).predict(x_test_normed)
skore1 = np.sqrt(mean_squared_error(knn_cv,y_test))

# 2- SVR

from sklearn.svm import SVR

svr = SVR('rbf')
svr_params = {'C': [0.1,0.2,1,2,4,8,20]}
svr_ = GridSearchCV(svr,svr_params,cv=15).fit(x_train_normed,y_train)
svr_.best_params_
svr_cv = SVR(C=20).fit(x_train_normed,y_train).predict(x_test_normed)
skore2 = np.sqrt(mean_squared_error(svr_cv,y_test))

# 3- MLP

from sklearn.neural_network import MLPRegressor

mlp = MLPRegressor()
mlp_params = {'hidden_layer_sizes':[[20,20],[100,100],[100,50]],
              'activation':['logistic','relu'],
              'solver':['lbfgs','adam'],
              'alpha':[0.0001,0.01,0.1,1],
              'learning_rate':['constant','invscaling']}
mlp_ = GridSearchCV(mlp,mlp_params,cv=15).fit(x_train_normed,y_train)
mlp_.best_params_
mlp_cv = MLPRegressor(hidden_layer_sizes=[20,20] , activation='relu' ,solver='lbfgs' ,alpha= 1, learning_rate= 'constant').fit(x_train_normed,y_train).predict(x_test_normed)
skore3 = np.sqrt(mean_squared_error(mlp_cv,y_test))

# 4- CART

from sklearn.tree import DecisionTreeRegressor

cart = DecisionTreeRegressor()
cart_params = {'min_samples_split':range(1,7),
               'max_leaf_nodes':range(5,10)}
cart_ = GridSearchCV(cart,cart_params,cv=15).fit(x_train_normed,y_train)
cart_.best_params_
cart_cv = DecisionTreeRegressor(min_samples_split=2,max_leaf_nodes= 8).fit(x_train_normed,y_train).predict(x_test_normed)
skore4 = np.sqrt(mean_squared_error(cart_cv,y_test))

# 5- BAGGED TREES

from sklearn.ensemble import BaggingRegressor

br = BaggingRegressor()
br_params = {'n_estimators':[500,1000],
             'max_features':[5,10,20,100,130]}
br_ = GridSearchCV(br,br_params,cv=15).fit(x_train_normed,y_train)
br_.best_params_
br_cv = BaggingRegressor(n_estimators= 1000,max_features= 20).fit(x_train_normed,y_train).predict(x_test_normed)
skore5 = np.sqrt(mean_squared_error(br_cv,y_test))


# 6- RF

from sklearn.ensemble import  RandomForestRegressor

rf = RandomForestRegressor()
rf_params = {'n_estimators':[100,200,500,1000],
             'max_features':['auto','sqrt','log2']}
rf_ = GridSearchCV(rf,rf_params,cv=15).fit(x_train_normed,y_train)
rf_.best_params_
rf_cv = RandomForestRegressor(n_estimators= 200, max_features= 'sqrt').fit(x_train_normed,y_train).predict(x_test_normed)
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
xgb_cv = XGBRegressor(n_estimators=1000 ,max_depth= 4,learning_rate= 0.01).fit(x_train_normed,y_train).predict(x_test_normed)
skore8 = np.sqrt(mean_squared_error(xgb_cv,y_test))

# 9- LIGHTGBM

sks = pd.read_csv('sample_submission1.csv',index_col=False)



