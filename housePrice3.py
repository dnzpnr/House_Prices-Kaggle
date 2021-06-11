import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from housePrices.housePrice2 import model_df_test
from housePrices.housePrice2 import model_df_train

test_ = model_df_test.copy()
train_ = model_df_train.copy()

test_.info()
train_.info()

'''Verisetlerimiz modele alinmak icin hemen hemen hazir. Tek eksigimiz kategorik degiskenlerimize
one-hot donusumu uygulamak ve boylece tamamen sayisal veriden olusan bir veriseti elde etmek.
19 tane degiskene one-hot donusumu uygulayacagiz. Dummy degisken tuzagindan da kacinmak icin
yeni olusturulan sutunlardan birer tanesini silecegiz.'''

new_test = pd.get_dummies(test_,columns=['MSZoning','Street','Alley','LotShape','LandContour','LotConfig','LandSlope','Neighborhood','BldgType',
                                         'HouseStyle','RoofStyle','RoofMatl','MasVnrType','Foundation','Heating','GarageType','MiscFeature','SaleType',
                                         'SaleCondition'])

new_test.info(verbose=True)

new_train = pd.get_dummies(train_,columns=['MSZoning','Street','Alley','LotShape','LandContour','LotConfig','LandSlope','Neighborhood','BldgType',
                                         'HouseStyle','RoofStyle','RoofMatl','MasVnrType','Foundation','Heating','GarageType','MiscFeature','SaleType',
                                         'SaleCondition'])

new_train.info(verbose=True)

'''Train ile test verisetine one-hot donusumu uyguladiktan sonra degisken sayilarimiz normal olarak artti.
Ancak bu artis ile sunu farkettim. Bazi degiskenlerin turleri train setinde fazlayken test setinde az. Bu sebeple one-hot donusumunden
sonra degisken sayisi train setinde daha fazla oldu.
Modelimizin daha dogru sonuc uretebilmesi icin degiskenlerin train ve test setindeki turlerini birbirlerine benzetmeliyiz. 
Bu nedenle train setindeki fazladan turleri inceleyecegim. Silinebilecek kadar az bir veriyse de o satirlari silecegim.'''


x1 = list(train_[train_['HouseStyle']=='2.5Fin'].index)
len(x1)
# x1 = [185, 198, 267, 304, 635, 883, 1031, 1440]
x2 = list(train_[train_['RoofMatl']=='ClyTile'].index)
len(x2)
# x2 = [1298]
x3 = list(train_[train_['RoofMatl']=='Membran'].index)
len(x3)
# x3 = [271]
x4 = list(train_[train_['RoofMatl']=='Metal'].index)
len(x4)
# x4 = [120]
x5 = list(train_[train_['RoofMatl']=='Roll'].index)
len(x5)
# x5 = [1275]
x6 = list(train_[train_['Heating']=='OthW'].index)
len(x6)
# x6 = [1248, 1349]
x7 = list(train_[train_['Heating']=='Floor'].index)
len(x7)
# x7 = [1321]

'''Bu 14 satiri silerek tum degisken ve turlerini test setindekiyle ayni yapmis olacagim
ve boylece aykiri degerlerden de kurtulmus olacagim.
Bu arada sunu da belirteyim;  Aslinda test setinde olup da train setinde olmayan 
bazi turler de olabilirdi. Bu tur durumlarda Condition degiskeni icin yaptigimiz puanlama
yontemi cok etkili olmaktadir. Boylece hem degiskeni sayisallastirip modele uygun hale getirmis oluyoruz hem
de puanlama sayesinde o turun o verisetinde olmayisi problem olmaktan cikiyor. Aksi halde kategorik degiskense
one-hot donusumu yapiliyor fakat degisken sayisinin train ve test setinde tutarsiz olmasina sebebiyet veriyor.'''

x = [*x1,*x2,*x3,*x4,*x5,*x6,*x7]

train_ = train_.drop(x,axis=0)

train_.info()

'''Simdi one-hot donusumlerimizi tekrar uygulayalim'''

new_test_ = pd.get_dummies(test_,columns=['MSZoning','Street','Alley','LotShape','LandContour','LotConfig','LandSlope','Neighborhood','BldgType',
                                         'HouseStyle','RoofStyle','RoofMatl','MasVnrType','Foundation','Heating','GarageType','MiscFeature','SaleType',
                                         'SaleCondition'])

new_test_.info(verbose=True)

new_train_ = pd.get_dummies(train_,columns=['MSZoning','Street','Alley','LotShape','LandContour','LotConfig','LandSlope','Neighborhood','BldgType',
                                         'HouseStyle','RoofStyle','RoofMatl','MasVnrType','Foundation','Heating','GarageType','MiscFeature','SaleType',
                                         'SaleCondition'])

new_train_.info(verbose=True)

'''Simdi dummy degiskenleri silelim.

new_train_.drop(['MSZoning_RM','Street_Grvl','Alley_NA','LotShape_Reg','LandContour_Lvl','LandSlope_Sev','Neighborhood_Veenker',
               'BldgType_TwnhsE','HouseStyle_SLvl','RoofStyle_Shed','RoofMatl_WdShngl','MasVnrType_Stone','Foundation_Wood',
               'Heating_Wall','GarageType_NA','MiscFeature_TenC','SaleType_WD','SaleCondition_Partial'],axis=1,inplace=True)


new_test_.drop(['MSZoning_RM','Street_Grvl','Alley_NA','LotShape_Reg','LandContour_Lvl','LandSlope_Sev','Neighborhood_Veenker',
               'BldgType_TwnhsE','HouseStyle_SLvl','RoofStyle_Shed','RoofMatl_WdShngl','MasVnrType_Stone','Foundation_Wood',
               'Heating_Wall','GarageType_NA','MiscFeature_TenC','SaleType_WD','SaleCondition_Partial'],axis=1,inplace=True)


#new_test_.to_csv('model_test.csv',index=False)
#new_train_.to_csv('model_train.csv',index=False)
'''
num_columns = new_train_.select_dtypes(include=[np.number])
num_columns_correlations = num_columns.corr()
print(num_columns_correlations['SalePrice'].sort_values(ascending = False),'/n')
