
'''
KAGGLE-HOUSE PRICE-DEGISKENLER VE ACIKLAMALARI
'''

# MSSubClass = Satisa dahil olan konut tipini tanimlar (Insaat sinifi)
# MSZoning = Satışın genel imar sınıflandırmasını tanımlar
# LotFrontage = Mülkiyetin doğrudan bağlantıli oldugu sokaga adim uzakligi
# LotArea = Parsel büyüklüğü
# Street = Mulke yol erisiminin turu
# Alley = Mulke ara erisim turu
# LotShape = Parsel sekli
# LandContour = Mulkun duzlugu
# Utilities = Etrafta ulasilabilir olanaklar
# LotConfig = Parsel duzeni
# LandSlope = Mulkun egimi
# Neighborhood = Mulkun Ames şehir sınırları içindeki konumu
# Condition1 = Tren yolu gibi cesitli yerlere yakinlik
# Condition2 = Tren yolu gibi cesitli yerlere yakinlik(birden fazla varsa)
# BldgType = Konut tipi
# HouseStyle = Konut stili(evin bitmis kat durumu)
# OverallQual = Evin genel malzeme kalitesinin ve bitiş miktarinin toplam puani
# OverallCond = Evin genel durumunun puanlanarak degerlendirilmesi
# YearBuilt = Binanin orjinal insa yili
# YearRemodAdd = Tadilat tarihi (tadilat veya ekleme yoksa inşaat tarihiyle aynı)
# RoofStyle = Cati tipi
# RoofMatl = Cati malzemesi
# Exterior1st = Dis kaplama malzemesi turu
# Exterior2nd = Dis kaplama malzemesi turu( birden fazla dis kaplama varsa)

'''bu ikisi toplanip tek bir degisken olusturulsa iyi olur'''

# MasVnrType = Duvarlarin dis tarafinda ekstra katman olarak kullanilan malzeme turu
# MasVnrArea = Duvar kaplama alani (square feet)
# ExterQual = Dış cephedeki malzemenin kalitesini değerlendirir
# ExterCond = Dis cephenin suanki durumunu degerlendirir
'''aslinda bu iki degisken birbiri ile iliskili. Bir seyler yapilmali buna'''

# Foundation = Temelde kullanilan malzeme turu
# BsmtQual = Bodrumun yuksekligi
# BsmtCond = Bodrumun genel durumunun puani
# BsmtExposure = Yürüme veya bahçe seviyesindeki duvarların degerlendirme puani
# BsmtFinType1 = Bodrumun tamamlanmis alaninin kalitesi
# BsmtFinSF1 = Tip 1 bitmis alan(square feet)
# BsmtFinType2 = Bodrumun tamamlanmis alaninin kalitesi(birden fazla bitmis alan varsa)
'''BsmtFinType1 ile toplanip tek bir degisken olusturulabilir mi?'''

# BsmtFinSF2 = Tip 2 bitmis alan(square feet)
'''Tip 1 ile Tip 2 toplanip tek bir degisken olarak yazilabilir mi?'''

# BsmtUnfSF = Bodrumun bitmemiş alanı (square feet)
'''Aslinda bitmis alan ile bitmemis alan modele ayni bilgiyi verecek. Fazla degisken kullanmaktan kacinmak amaciyla bir tanesini silelim mi?'''

# TotalBsmtSF = Bodrumun toplam alani (square feet)
# Heating = Isinma sekli
# HeatingQC = Isinma durumu ve kalitesi
# CentralAir = Merkezi klima var mi yok mu?
# Electrical = Elektrik sistem tipi
# 1stFlrSF = Birinci kat alani (square feet)
# 2ndFlrSF = Ikinci kat alani (square feet)
'''Bu alanlari ayri ayri almaktansa toplam alani alsak nasil olur?'''

# LowQualFinSF = Butun katlar dahil olmak uzere dusuk kaliteye sahip bitmis alanlar(square feet)
# GrLivArea = Zemin ustunde bulunan yasama alani(square feet) (bodrum dahil degil)
# BsmtFullBath = Bodrum katindaki tam banyolar
# BsmtHalfBath = Bodrum katindaki yarim banyolar
# FullBath = Zemin ustu katlardaki tam banyolar(bodrum dahil degil)
# HalfBath = Zemin ustu katlardaki yarim banyolar(bodrum dahil degil)
# BedroomAbvGr = Zemin katin ustundeki yatak odalari (bodrum dahil degil)
# KitchenAbvGr = Zemin katin ustundeki mutfaklar (bodrum dahil degil)
# KitchenQual = Mutfak kaliteleri
# TotRmsAbvGrd = Zemin ustundeki katlarda bulunan banyolar haric tum odalar(bodrum dahil degil)
# Functional = Ev islevselligi degerlendirmesi
'''Bu degiskenlerin cogunu birlestirmeyi planliyorum'''

# Fireplaces = Somine sayilari
# FireplaceQu = Somine kalitesi
# GarageType = Garaj yeri
# GarageYrBlt = Garajın yapım yılı
# GarageFinish = Garajin ic dekorasyonunun tamamlanma durumu
# GarageCars = Araba kapasitesine göre garaj boyutu
# GarageArea = Garaj boyutu
'''Aslinda bu iki degisken de hemen hemen ayni seyi ifade ediyor, birlestirme yapilabilir'''

# GarageQual = Garaj kalitesi
# GarageCond = Garajin durumu
'''Bu iki degisken de benzer seyleri ifade ediyor sanki, birlestirme yapilabilir'''

# PavedDrive = Araba yolunun asfalt durumu
# WoodDeckSF = Ahsap doseme alani(square feet)
# OpenPorchSF = Kapı önündeki açık veranda alanı(square feet)
# EnclosedPorch = Kapı önündeki kapali veranda alanı(square feet)
'''Bu degiskenler de birbiriyle toplanip tek degisken olabilir'''

# 3SsnPorch = Üç mevsim veranda alanı(square feet)
# ScreenPorch = Manzarali veranda alani(square feet)
# PoolArea = Havuz alani(square feet)
# PoolQC = Havuzun kalitesi
# Fence = Cit durumu (hem kalite hem de cit turu acisindan)
# MiscFeature = Diğer kategorilerde olmayan çeşitli özellikler
# MiscVal = MiscFeature daki özelliklerin $ değeri
# MoSold = Satildigi ay
# YrSold = Satildigi yil
# SaleType = Satis turu
# SaleCondition = Satis durumu

#########################################################################################

# VERISETLERINI INCELEME VE DUZENLEME

'''Simdi test ve train verisetlerimizi inceleyelim. Eksik ve yanlis yerler varsa duzenlemeye calisalim.'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 170)
pd.set_option('display.max_rows', None)

test_ = pd.read_csv('test.csv')
train_ = pd.read_csv('train.csv')

test_.info()
train_.info()
'''Degiskenleri belirlemek icin ev ile ilgili temel ozellikleri ana kategoriler olarak ayiracagim. Daha sonra her bir ana kategori
icin ilgili degiskenleri birarada inceleyecegim. Bazi yerlerde degiskenleri birlestirerek yeni degiskenler olusturacagim.
Degisken sayisini olabildigince az ve oz tutmaya calisacagim ki kuracagim modelden alacagim sonuc daha iyi olsun. Fazla 
degisken modelde gereksiz bilgi islenmesine ve dolayisiyla gurultuye sebep olmaktadir.
ANA KATEGORILER;
Bodrum,Cit, Veranda, Havuz, Oda sayisi, Alanlar,Dis kaplama, Cati, Insa yili, Satis yili, Malzeme kalitesi, Somine, Garaj, Isinma, 
Bolgesel durum/konum, Satis turu/durumu, Sahip olunan olanaklar.
'''

df_test = test_.copy()
df_train = train_.copy()

df_test.info()
df_train.info()

# Bodrum;

'''Simdi bodrumla ilgili tum degiskenleri inceleyelim.'''

df_test['BsmtQual'].value_counts()

df_train['BsmtQual'].value_counts()

df_test['BsmtCond'].value_counts()

df_train['BsmtCond'].value_counts()

'''Sanirim bodrum kati olmayan binalar var. Once onlari tespit edelim.
Ilgili degiskenler;
BsmtQual test setinde 44 tane eksik, train setinde 37 tane eksik.
BsmtCond test setinde 45 tane eksik, train setinde 37 tane eksik.
BsmtExposure test setinde 44 tane eksik, train setinde 38 tane eksik.
BsmtFinType1 test setinde 42 tane eksik, train setinde 37 tane eksik.
BsmtFinSF1 test setinde 1 tane eksik.
BsmtFinType2 test setinde 42 tane eksik, train setinde 38 tane eksik.
BsmtFinSF2 test setinde 1 tane eksik.
BsmtUnfSF test setinde 1 tane eksik.
TotalBsmtSF test setinde 1 tane eksik.
BsmtFullBath test setinde 2 tane eksik.
BsmtHalfBath test setinde 2 tane eksik.
'''
df_train.info()
df_test.info()

df_test['BsmtExposure'].value_counts()

df_train['BsmtExposure'].value_counts()

df_test['BsmtFinType1'].value_counts()

df_train['BsmtFinType1'].value_counts()

df_test['BsmtFinSF1'].value_counts()

df_train['BsmtFinSF1'].value_counts()

df_test['BsmtFinType2'].value_counts()

df_train['BsmtFinType2'].value_counts()

df_test['BsmtFinSF2'].value_counts()

df_train['BsmtFinSF2'].value_counts()

df_test['BsmtUnfSF'].value_counts()

df_train['BsmtUnfSF'].value_counts()

df_test['TotalBsmtSF'].value_counts()

df_train['TotalBsmtSF'].value_counts()

df_test['BsmtFullBath'].value_counts()

df_train['BsmtFullBath'].value_counts()

df_test['BsmtHalfBath'].value_counts()

df_train['BsmtHalfBath'].value_counts()


bsmntq_null_index_test = list(df_test[df_test['BsmtQual'].isnull()].index)
bsmntq_null_index_train = list(df_train[df_train['BsmtQual'].isnull()].index)

bsmntc_null_index_test = list(df_test[df_test['BsmtCond'].isnull()].index)
bsmntc_null_index_train = list(df_train[df_train['BsmtCond'].isnull()].index)

bsmntexp_null_index_test = list(df_test[df_test['BsmtExposure'].isnull()].index)
bsmntexp_null_index_train = list(df_train[df_train['BsmtExposure'].isnull()].index)

bsmnttype1_null_index_test = list(df_test[df_test['BsmtFinType1'].isnull()].index)
bsmnttype1_null_index_train = list(df_train[df_train['BsmtFinType1'].isnull()].index)

bsmnt1_null_index_test = list(df_test[df_test['BsmtFinSF1']==0.0].index)
bsmnt1_null_index_test.append(df_test[df_test['BsmtFinSF1'].isnull()].index[0])
bsmnt1_null_index_train = list(df_train[df_train['BsmtFinSF1']==0].index)

bsmnttype2_null_index_test = list(df_test[df_test['BsmtFinType2'].isnull()].index)
bsmnttype2_null_index_train = list(df_train[df_train['BsmtFinType2'].isnull()].index)

bsmnt2_null_index_test = list(df_test[df_test['BsmtFinSF2']==0.0].index)
bsmnt2_null_index_test.append(df_test[df_test['BsmtFinSF2'].isnull()].index[0])
bsmnt2_null_index_train = list(df_train[df_train['BsmtFinSF2']==0].index)

bsmnt_null_index_test = list(df_test[df_test['BsmtUnfSF']==0.0].index)
bsmnt_null_index_test.append(df_test[df_test['BsmtUnfSF'].isnull()].index[0])
bsmnt_null_index_train = list(df_train[df_train['BsmtUnfSF']==0].index)

bsmnttotal_null_index_test = list(df_test[df_test['TotalBsmtSF']==0.0].index)
bsmnttotal_null_index_test.append(df_test[df_test['TotalBsmtSF'].isnull()].index[0])
bsmnttotal_null_index_train = list(df_train[df_train['TotalBsmtSF']==0].index)

bsmntfull_null_index_test = list(df_test[df_test['BsmtFullBath']==0.0].index)
bsmntfull_null_index_test.append(df_test[df_test['BsmtFullBath'].isnull()].index[0])
bsmntfull_null_index_train = list(df_train[df_train['BsmtFullBath']==0].index)

bsmnthalf_null_index_test = list(df_test[df_test['BsmtHalfBath']==0.0].index)
bsmnthalf_null_index_test.append(df_test[df_test['BsmtHalfBath'].isnull()].index[0])
bsmnthalf_null_index_train = list(df_train[df_train['BsmtHalfBath']==0].index)

no_basement_index_test = set.intersection(set(bsmntq_null_index_test),set(bsmntc_null_index_test),set(bsmntexp_null_index_test),set(bsmnttype1_null_index_test),
        set(bsmnt1_null_index_test),set(bsmnttype2_null_index_test),set(bsmnt2_null_index_test),set(bsmnt_null_index_test),set(bsmnttotal_null_index_test),
        set(bsmntfull_null_index_test),set(bsmnthalf_null_index_test))

len(no_basement_index_test)

no_basement_index_train = set.intersection(set(bsmntq_null_index_train),set(bsmntc_null_index_train), set(bsmntexp_null_index_train), set(bsmnttype1_null_index_train), set(bsmnt1_null_index_train),
        set(bsmnttype2_null_index_train), set(bsmnt2_null_index_train), set(bsmnt_null_index_train), set(bsmnttotal_null_index_train), set(bsmntfull_null_index_train),
        set(bsmnthalf_null_index_train))

len(no_basement_index_train)

'''Test setindeki bodrumu olmayan binalarin indexleri(41 tane);
[125, 133, 269, 318, 354, 387, 388, 396, 397, 398, 400, 455, 590, 606, 608, 660, 662, 729, 730, 733, 756, 764, 927, 975, 
992, 993, 1030, 1038, 1087, 1092, 1104, 1118, 1139, 1242, 1303, 1306, 1343, 1344, 1364, 1431,1444]

Train setindeki bodrum olmayan binalarin indexleri(37 tane);
[17, 39, 90, 102, 156, 182, 259, 342, 362, 371, 392, 520, 532, 533, 553, 646, 705, 736, 749, 778, 868, 894, 897, 984, 1000,
 1011, 1035, 1045, 1048, 1049, 1090, 1179, 1216, 1218, 1232, 1321,1412]
'''
a = set.difference(set(bsmntc_null_index_test),set(no_basement_index_test))
df_test.iloc[list(a),[30,31,32,33,34,35,36,37,38,47,48]]

'''Test setindeki BsmtFullBath ve BsmtHalfBath degiskeninde 728 indexinin olmadigini farkettim. Halbuki diger tum degerleri bodrum olmadigina dair bilgi iceriyor.
Index 728 i de bodrum yokmus gibi duzeltelim.'''

b = set.difference(set(bsmntexp_null_index_train),set(no_basement_index_train))
df_train.iloc[list(b),[30,31,32,33,34,35,36,37,38,47,48]]

'''SON DURUM!
Test setindeki bodrum olmayan binalarin indexleri(42 tane);
[125, 133, 269, 318, 354, 387, 388, 396, 397, 398, 400, 455, 590, 606, 608, 660, 662, 728, 729, 730, 733, 756, 764, 927, 975, 
992, 993, 1030, 1038, 1087, 1092, 1104, 1118, 1139, 1242, 1303, 1306, 1343, 1344, 1364, 1431,1444]

Train setindeki bodrum olmayan binalarin indexleri(37 tane);
[17, 39, 90, 102, 156, 182, 259, 342, 362, 371, 392, 520, 532, 533, 553, 646, 705, 736, 749, 778, 868, 894, 897, 984, 1000,
 1011, 1035, 1045, 1048, 1049, 1090, 1179, 1216, 1218, 1232, 1321,1412]
'''

nobtest = [125, 133, 269, 318, 354, 387, 388, 396, 397, 398, 400, 455, 590, 606, 608, 660, 662, 728, 729, 730, 733, 756, 764, 927, 975,
992, 993, 1030, 1038, 1087, 1092, 1104, 1118, 1139, 1242, 1303, 1306, 1343, 1344, 1364, 1431,1444]

nobtrain = [17, 39, 90, 102, 156, 182, 259, 342, 362, 371, 392, 520, 532, 533, 553, 646, 705, 736, 749, 778, 868, 894, 897, 984, 1000,
 1011, 1035, 1045, 1048, 1049, 1090, 1179, 1216, 1218, 1232, 1321,1412]

df_test.iloc[nobtest,[30,31,32,33,35]] = 'NA'
df_test.iloc[nobtest,[34,36,37,38,47,48]] = 0.0

df_test.info()

df_train.iloc[nobtrain,[30,31,32,33,35]] = 'NA'
df_train.iloc[nobtrain,[34,36,37,38,47,48]] = 0

df_train.info()

'''Bodrumla ilgili bazi degiskenlerde hala eksikler var, onlari da modlariyla dolduralim.
'''
df_test['BsmtQual'].fillna(df_test['BsmtQual'].mode()[0],inplace=True)
df_test['BsmtCond'].fillna(df_test['BsmtCond'].mode()[0],inplace=True)
df_test['BsmtExposure'].fillna(df_test['BsmtExposure'].mode()[0],inplace=True)
df_train['BsmtExposure'].fillna(df_train['BsmtExposure'].mode()[0],inplace=True)
df_train['BsmtFinType2'].fillna(df_train['BsmtFinType2'].mode()[0],inplace=True)


'''Simdi gelelim hangi degiskenleri nasil modele alacagimiza.
Butun bodrum degiskenlerini modele birlestirerek alacagim. Ama oncesinde degiskenlerimizi sayisallastiralim.
'''
bq= {'NA':0,'Po':2,'Fa':4,'TA':6,'Gd':8,'Ex':10}

df_test['BsmtQual'].replace(bq,inplace=True)

df_train['BsmtQual'].replace(bq,inplace=True)

df_test['BsmtCond'].replace(bq,inplace=True)

df_train['BsmtCond'].replace(bq,inplace=True)

df_test['BsmtQual'].value_counts()

df_train['BsmtQual'].value_counts()

df_test['BsmtCond'].value_counts()

df_train['BsmtCond'].value_counts()


b_ex = {'NA':0,'No':0,'Mn':2,'Av':4,'Gd':6}

df_test['BsmtExposure'].replace(b_ex,inplace=True)

df_train['BsmtExposure'].replace(b_ex,inplace=True)

df_test['BsmtExposure'].value_counts()

df_train['BsmtExposure'].value_counts()


b_types = {'GLQ':10,'ALQ':8,'BLQ':6,'Rec':4,'LwQ':2,'Unf':1,'NA':0}

df_test['BsmtFinType1'].replace(b_types,inplace=True)

df_train['BsmtFinType1'].replace(b_types,inplace=True)

df_test['BsmtFinType2'].replace(b_types,inplace=True)

df_train['BsmtFinType2'].replace(b_types,inplace=True)

df_train['BsmtFinType1'].value_counts()

df_test['BsmtFinType1'].value_counts()

df_train['BsmtFinType2'].value_counts()

df_test['BsmtFinType2'].value_counts()

df_train.info()

df_test.info()

'''Simdi bodrumla ilgili tum bilgileri kapsayan yeni degiskenimizi olusturalim.'''

df_test['Bsmt'] = (df_test['BsmtQual'] * df_test['BsmtQual'] * df_test['BsmtQual'] * df_test['BsmtQual'] * df_test['BsmtQual']) + df_test['TotalBsmtSF'] + df_test['BsmtFinSF1'] * df_test['BsmtFinType1'] + df_test['BsmtExposure'] * df_test['BsmtExposure'] * df_test['BsmtExposure'] * df_test['BsmtExposure'] * df_test['BsmtExposure'] + df_test['BsmtFullBath'] * df_test['BsmtFullBath'] * df_test['BsmtFullBath'] * df_test['BsmtFullBath'] * df_test['BsmtFullBath'] + df_test['BsmtUnfSF']*15 + df_test['BsmtCond'] * df_test['BsmtCond'] * df_test['BsmtCond'] * df_test['BsmtCond'] *2 + df_test['BsmtFinType2'] * df_test['BsmtFinType2'] * df_test['BsmtFinType2'] * df_test['BsmtFinType2'] + df_test['BsmtFinSF2']*15
df_train['Bsmt'] = (df_train['BsmtQual'] * df_train['BsmtQual'] * df_train['BsmtQual'] * df_train['BsmtQual'] * df_train['BsmtQual']) + df_train['TotalBsmtSF'] + df_train['BsmtFinSF1'] * df_train['BsmtFinType1'] + df_train['BsmtExposure'] * df_train['BsmtExposure'] * df_train['BsmtExposure'] * df_train['BsmtExposure'] * df_train['BsmtExposure'] +  + df_train['BsmtFullBath'] * df_train['BsmtFullBath'] * df_train['BsmtFullBath'] * df_train['BsmtFullBath'] * df_train['BsmtFullBath'] + df_train['BsmtUnfSF']*15 + df_train['BsmtCond'] * df_train['BsmtCond'] * df_train['BsmtCond'] * df_train['BsmtCond'] *2 + df_train['BsmtFinType2'] * df_train['BsmtFinType2'] * df_train['BsmtFinType2'] * df_train['BsmtFinType2'] + df_train['BsmtFinSF2']*15

'''Yeni degiskeni neden bu sekilde olusturdugumu soyle aciklayabilirim;
Ileride model kismina gecmeden once yazdigim korelasyon ile ilgili olan kismi tekrar tekrar calistirdim. 
 Tabi her seferinde once yeni degiskeni degistirdim ve denedim. SalePrice ile olan korelasyonu en
 fazla bu sekilde oldu.'''


#num_columns = df_train.select_dtypes(include=[np.number])
num_columns = df_train.loc[:,['BsmtQual','TotalBsmtSF','BsmtFinSF1','BsmtFinType1','BsmtExposure','BsmtFullBath','BsmtHalfBath','BsmtUnfSF','BsmtCond','BsmtFinType2','BsmtFinSF2','SalePrice']]
num_columns_correlations = num_columns.corr()
print(num_columns_correlations['SalePrice'].sort_values(ascending = False),'/n')


# Cit(fence)

df_train['Fence'].value_counts()
df_test['Fence'].value_counts()

'''Fence degiskeninde cok fazla eksik deger var. Eksik degerleri
sanki o binanin citi yokmus gibi kabul edecegim ve NA ile dolduracagim.'''

df_train['Fence'].fillna('NA',inplace=True)
df_test['Fence'].fillna('NA',inplace=True)

'''Simdi fence degiskenini sayisala donusturelim.'''

fence = {'NA':0,'MnWw':2,'GdWo':4,'MnPrv':6,'GdPrv':8}
df_test['Fence'].replace(fence,inplace=True)
df_train['Fence'].replace(fence,inplace=True)


# Veranda(porch)

df_train.info()
df_test.info()

df_test['OpenPorchSF'].value_counts()

df_train['OpenPorchSF'].value_counts()

df_test['EnclosedPorch'].value_counts()

df_train['EnclosedPorch'].value_counts()

df_test['3SsnPorch'].value_counts()

df_train['3SsnPorch'].value_counts()

df_test['ScreenPorch'].value_counts()

df_train['ScreenPorch'].value_counts()

'''Veranda alanlarini birlestirerek yeni bir degisken olusturacagim.
Fiyati ScreenPorch ile 3SsnPorch daha fazla etkileyecegi icin bunlari iki ile carparak ekleyecegim.'''

df_train['Porch'] = df_train['OpenPorchSF'] + df_train['EnclosedPorch'] + df_train['3SsnPorch']*2 + df_train['ScreenPorch']*2
df_test['Porch'] = df_test['OpenPorchSF'] + df_test['EnclosedPorch'] + df_test['3SsnPorch']*2 + df_test['ScreenPorch']*2


# Havuz

df_test['PoolArea'].value_counts()

df_train['PoolArea'].value_counts()

df_test['PoolQC'].value_counts()

df_train['PoolQC'].value_counts()

df_test.iloc[df_test[df_test['PoolArea'] != 0].index,71:73]


# Oda sayilari

df_train.info()
df_test.info()

df_train['BsmtFullBath'].value_counts()
df_test['BsmtFullBath'].value_counts()

df_train['BsmtHalfBath'].value_counts()
df_test['BsmtHalfBath'].value_counts()

df_train['FullBath'].value_counts()
df_test['FullBath'].value_counts()

df_train['HalfBath'].value_counts()
df_test['HalfBath'].value_counts()

df_train['BedroomAbvGr'].value_counts()
df_test['BedroomAbvGr'].value_counts()

df_train['KitchenAbvGr'].value_counts()
df_test['KitchenAbvGr'].value_counts()

df_train['KitchenQual'].value_counts()
df_test['KitchenQual'].value_counts()

df_test.iloc[df_test[df_test['KitchenQual'].isnull()].index,52:54]

df_test['KitchenQual'].fillna(df_test['KitchenQual'].mode()[0],inplace=True)

kitc = {'Po':1,'Fa':3,'TA':5,'Gd':7,'Ex':9}
df_test['KitchenQual'].replace(kitc,inplace=True)
df_train['KitchenQual'].replace(kitc,inplace=True)

df_train['TotRmsAbvGrd'].value_counts()
df_test['TotRmsAbvGrd'].value_counts()

'''Simdi oda syilariyla ilgili yeni degiskenimizi olusturalim.'''

df_test['AllRooms'] =  df_test['TotRmsAbvGrd'] + df_test['FullBath'] + df_test['HalfBath'] +  df_test['BsmtFullBath'] + df_test['BsmtHalfBath']
df_train['AllRooms'] =  df_train['TotRmsAbvGrd'] + df_train['FullBath'] + df_train['HalfBath'] + df_train['BsmtFullBath'] + df_train['BsmtHalfBath']

# Area (Alanlar)

df_test.info()
df_train.info()

df_test['LotArea'].value_counts()
df_train['LotArea'].value_counts()

df_train['LowQualFinSF'].value_counts()
df_test['LowQualFinSF'].value_counts()

df_train['GrLivArea'].value_counts()
df_test['GrLivArea'].value_counts()

df_train['1stFlrSF'].value_counts()
df_test['1stFlrSF'].value_counts()

df_train['2ndFlrSF'].value_counts()
df_test['2ndFlrSF'].value_counts()

'''Bu degiskenleri kullanarak yeni degiskenimizi olusturalim.'''

df_train['Areas'] =  df_train['GrLivArea'] + df_train['TotalBsmtSF'] - df_train['LowQualFinSF']*2
df_test['Areas'] = df_test['GrLivArea'] + df_test['TotalBsmtSF'] - df_test['LowQualFinSF']*2

# Dis kaplama

df_test['Exterior1st'].value_counts()

df_train['Exterior1st'].value_counts()

df_test['Exterior2nd'].value_counts()

df_train['Exterior2nd'].value_counts()

'''Bu iki degiskenin de test setinde birer tane eksik degeri var. 
Once eksik degerleri dolduralim modlariyla.'''

df_test['Exterior1st'].fillna(df_test['Exterior1st'].mode()[0],inplace=True)
df_test['Exterior2nd'].fillna(df_test['Exterior2nd'].mode()[0],inplace=True)

df_test.info()
df_train.info()

'''Simdi de iki degiskeni puanlayalim ve puanlari toplayalim. Puanlama yaparken
de herhangi bir ture agirlik vermemek icin Exterior1st degiskenindeki en az puan verdigim
turu Exterior2nd degiskeni icin en cok puan vererek modeldeki agirligini esitlemeyi dusunuyorum.'''

'''Yalniz incelerken test ve train setinde CmentBd,Wd Shng,Brk Cmn turlerinde yanlis yazim oldugunu farkettim.
 Bu duzeltmeyi de puanlamayi yaptigim sozluk yapisinin icinde yapacagim.'''

ext_deg1 = {'WdShing':1,'Wd Shng':1,'Wd Sdng':2,'VinylSd':3,'Stucco':4,'Stone':5,'PreCast':6,'Plywood':7,'Other':8,'MetalSd':9,
            'ImStucc':10,'HdBoard':11,'CemntBd':12,'CmentBd':12,'CBlock':13,'BrkFace':14,'BrkComm':15,'Brk Cmn':15,'AsphShn':16,'AsbShng':17}
ext_deg2 = {'WdShing':17,'Wd Shng':17,'Wd Sdng':16,'VinylSd':15,'Stucco':14,'Stone':13,'PreCast':12,'Plywood':11,'Other':10,'MetalSd':9,
            'ImStucc':8,'HdBoard':7,'CemntBd':6,'CmentBd':6,'CBlock':5,'BrkFace':4,'BrkComm':3,'Brk Cmn':3,'AsphShn':2,'AsbShng':1}

df_test['Exterior1st'].replace(ext_deg2,inplace=True)
df_train['Exterior1st'].replace(ext_deg2,inplace=True)
df_test['Exterior2nd'].replace(ext_deg2,inplace=True)
df_train['Exterior2nd'].replace(ext_deg2,inplace=True)

df_test['MasVnrType'].value_counts()

df_train['MasVnrType'].value_counts()

df_test['MasVnrArea'].value_counts()

df_train['MasVnrArea'].value_counts

'''Train setinde bu iki degiskenin sekiz 8 tane eksik degeri var. Test setinde ise MasVnrType
degiskeninin 16, MasVnrArea degiskeninin 15 eksik degeri var.
'''

mvt_null_indexs_test = list(df_test[df_test['MasVnrType'].isnull()].index)
mva_null_indexs_test = list(df_test[df_test['MasVnrArea'].isnull()].index)

'''Yukarida iki degisken icin bos degerlerin indexlerini kiyasladim acaba
gercekten ekstra dis kaplama alani 0 oldugunda ekstra dis kaplamada kullanilan malzeme de None
mi degil mi bunu gormek icin.
 1150. indexte problem var.

MasVnrType(None) = 878 adet + 16 (14 olmali ki MasVnrArea ile esitlensin)
MasVnrArea(0.0) = 877 adet + 15 
MasVnrArea'nin 0 oldugu yerlerde MasVnrType None disinda bir deger almis.
Bu yuzden 1150.index MasVnrType None haricinde birsey olmali.
Demekki MasVnrType(None) degerlerinden 1 tanesinde daha problem var.Onu da bulup duzeltmeliyim.
'''

df_test.iloc[1150,23:29]

df_test.iloc[:,23:29]

df_test.iloc[1150,25] = 'BrkFace'

x = list(df_test[df_test['MasVnrType']== 'None'].index)
y = list(df_test[df_test['MasVnrArea']==0.0].index)
diff_ = set.difference(set(x),set(y))
# diff_ =  {209, 992}

df_test.iloc[[209,992,1150],23:29]

'''Bu indexlerde bir hata var ama ne olmasi gerektigi konusunda bir cozum bulamadim.
O yuzden MasVnrType ve MasVnrArea degerleri eksik olan indexleri ekstra kaplama
alani olmadigi dusuncesine dayanarak dolduralim.'''

df_test['MasVnrType'].fillna('None',inplace=True)
df_test['MasVnrArea'].fillna(0.0,inplace=True)


df_test.info()
df_train.info()

'''Train seti icin;'''

mvt_null_indexs_train = list(df_train[df_train['MasVnrType'].isnull()].index)
mva_null_indexs_train = list(df_train[df_train['MasVnrArea'].isnull()].index)

'''Indexler ayni, suphe uyandirici bir durum yok. 
O yuzden dolduruyorum...'''

df_train['MasVnrType'].fillna('None',inplace=True)
df_train['MasVnrArea'].fillna(0.0,inplace=True)

df_train.info()

'''Insaat sektoruyle ilgili biraz arastirma yaptigimda BrkFace turunun en pahali malzeme oldugunu ogrendim.
Devaminda ise pahalidan ucuza BrkCmn, Stone ve CBlock gelmektedir. Bu dort malzemenin fiyata etkisi neredeyse ayni fakat ben yine de puanlandirmayi 
bu siraya gore yapacagim.'''

mvt_ = {'None':0,'CBlock':1,'Stone':1.5,'BrkCmn':2,'BrkFace':2.5}
df_test['MasVnrType'].replace(mvt_,inplace=True)
df_train['MasVnrType'].replace(mvt_,inplace=True)

df_test['ExterQual'].value_counts()

df_train['ExterQual'].value_counts()

df_test['ExterCond'].value_counts()

df_train['ExterCond'].value_counts()

'''Bu iki degiskeni de sayisallastiralim.'''

qc = {'Po':1,'Fa':3,'TA':5,'Gd':7,'Ex':9}
df_test['ExterQual'].replace(qc,inplace=True)
df_train['ExterQual'].replace(qc,inplace=True)
df_test['ExterCond'].replace(qc,inplace=True)
df_train['ExterCond'].replace(qc,inplace=True)

df_test.info()
df_train.info()

'''Simdi yeni degiskenimizi olusturalim.'''

df_train['Exterior_'] = df_train['ExterQual'] * df_train['MasVnrArea'] // df_train['MasVnrType']
df_test['Exterior_'] = df_test['ExterQual'] * df_test['MasVnrArea'] // df_test['MasVnrType']

# Cati

df_test['RoofStyle'].value_counts()

df_train['RoofStyle'].value_counts()

df_test['RoofMatl'].value_counts()

df_train['RoofMatl'].value_counts()

df_test.info()
df_train.info()

# Insa yili

df_test['YearBuilt'].value_counts()

df_train['YearBuilt'].value_counts()

df_test['YearRemodAdd'].value_counts()

df_train['YearRemodAdd'].value_counts()


df_test[df_test['YearRemodAdd']< df_test['YearBuilt']].loc[:,['YearBuilt','YearRemodAdd']]

df_train[df_train['YearRemodAdd']< df_train['YearBuilt']].loc[:,['YearBuilt','YearRemodAdd']]

'''Test setinde 416.indexte bir problem tespit ettim. Tadilat yili insaat yilindan kucuk olmamali.'''

df_test.loc[416,'YearRemodAdd'] = 2002

'''Bu iki degiskeni toplayip tek bir degisken elde edecegim.'''

df_test['NewYear'] = df_test['YearRemodAdd'] + df_test['YearBuilt']
df_train['NewYear'] = df_train['YearRemodAdd'] + df_train['YearBuilt']

df_test.info()
df_train.info()


# Satldigi yil

df_test['MoSold'].value_counts()
df_train['MoSold'].value_counts()

df_test['YrSold'].value_counts()
df_train['YrSold'].value_counts()

df_train.groupby('MoSold')['SalePrice'].sum().value_counts()

df_train.groupby('YrSold')['SalePrice'].sum().value_counts()


# Evin kalitesi

df_test['OverallQual'].value_counts()

df_train['OverallQual'].value_counts()

df_test['OverallCond'].value_counts()

df_train['OverallCond'].value_counts()

df_test['Functional'].value_counts()

df_train['Functional'].value_counts()

'''Test setinde 2 tane Functional degeri eksik.'''

df_test['Functional'].fillna(df_test['Functional'].mode()[0],inplace=True)

'''Maj1 ile Maj2 yi, Min1 ile Min2 yi, Sal ile de Sev i toplamak istiyorum.'''
df_train.loc[df_train['Functional']=='Sal','Functional'] = 'Sev'
df_test.loc[df_test['Functional']=='Sal','Functional'] = 'Sev'

df_train.loc[df_train['Functional']=='Maj2','Functional'] = 'Maj1'
df_test.loc[df_test['Functional']=='Maj2','Functional'] = 'Maj1'

df_train.loc[df_train['Functional']=='Min1','Functional'] = 'Min2'
df_test.loc[df_test['Functional']=='Min1','Functional'] = 'Min2'

f = {'Sev':2,'Maj1':4,'Mod':6,'Min2':8,'Typ':10}
df_test['Functional'].replace(f,inplace=True)
df_train['Functional'].replace(f,inplace=True)

'''Simdi evin genel kalitesi hakkinda bilgi veren yeni bir degisken olusturalim.'''

df_train['Quality'] = df_train['OverallQual'] + df_train['OverallCond']
df_test['Quality'] = df_test['OverallQual'] + df_test['OverallCond']


# Somine

df_train['Fireplaces'].value_counts()
df_test['Fireplaces'].value_counts()

df_test.info()
df_train.info()

'''FireplaceQu degiskeninde cok fazla eksik deger var. Acaba sominesi olmayan kac bina var?
Ilgili degiskenler;
Fireplaces,FireplaceQu
'''
df_train['FireplaceQu'].value_counts()
df_test['FireplaceQu'].value_counts()

no_fire = list(df_test[df_test['Fireplaces']==0].index)
no_fireQ = list(df_test[df_test['FireplaceQu'].isnull()].index)

nof = set.intersection(set(no_fire),set(no_fireQ))
len(nof)
'''Test setinde 730 tane binanin sominesi yokmus sonucuna vardim.'''

no_fire_t = list(df_train[df_train['Fireplaces']==0].index)
no_fireQ_t = list(df_train[df_train['FireplaceQu'].isnull()].index)

nof_t = set.intersection(set(no_fire_t),set(no_fireQ_t))
len(nof_t)
'''Train setinde 690 tane binanin sominesi yokmus sonucuna vardim.
SImdi gerekli duzenlemeleri yapalim;'''

df_train.iloc[list(nof_t),57] = 'NA'
df_test.iloc[list(nof),57] = 'NA'

'''FireplaceQu degiskenindeki eksik degerleri tamamladik. Simdi sayisala donusturelim.'''

fire_q = {'NA':0,'Po':2,'Fa':4,'TA':6,'Gd':8,'Ex':10}
df_test['FireplaceQu'].replace(fire_q,inplace=True)
df_train['FireplaceQu'].replace(fire_q,inplace=True)

'''Simdi bu iki degiskeni kullanarak yeni degiskenimizi olusturalim.'''

df_test['New_Fireplace'] = df_test['FireplaceQu'] * df_test['Fireplaces']
df_train['New_Fireplace'] = df_train['FireplaceQu'] * df_train['Fireplaces']

# Garage

'''Simdi garaj ile ilgili degiskenleri inceleyelim.
Ilgili degiskenler;
GarageType,GarageYrBlt,GarageFinish,GarageCars,GarageArea,GarageQual,GarageCond

Garaj ile ilgili degiskenlerin tamaminda eksikler var. Once kac tane binanin garaji yok onu ogrenelim.'''

df_train['GarageType'].value_counts()
df_test['GarageType'].value_counts()

'''GarageType degiskeni de one-hot yapilmasi gereken degiskenlerden biri.
O yuzden simdilik kalsin, en son karar vereyim.'''

gt_test = list(df_test[df_test['GarageType'].isnull()].index)
gt_train = list(df_train[df_train['GarageType'].isnull()].index)

df_train['GarageYrBlt'].value_counts()
df_test['GarageYrBlt'].value_counts()

gy_test = list(df_test[df_test['GarageYrBlt'].isnull()].index)
gy_train = list(df_train[df_train['GarageYrBlt'].isnull()].index)

df_train['GarageFinish'].value_counts()
df_test['GarageFinish'].value_counts()

gf_test = list(df_test[df_test['GarageFinish'].isnull()].index)
gf_train = list(df_train[df_train['GarageFinish'].isnull()].index)

df_train['GarageCars'].value_counts()
df_test['GarageCars'].value_counts()

gc_test = list(df_test[df_test['GarageCars']==0.0].index)
gc_test.append(df_test[df_test['GarageCars'].isnull()].index[0])
gc_train = list(df_train[df_train['GarageCars']==0].index)

df_train['GarageArea'].value_counts()
df_test['GarageArea'].value_counts()

ga_test = list(df_test[df_test['GarageArea']==0.0].index)
ga_test.append(df_test[df_test['GarageArea'].isnull()].index[0])
ga_train = list(df_train[df_train['GarageArea']==0].index)

df_train['GarageQual'].value_counts()
df_test['GarageQual'].value_counts()

gq_test = list(df_test[df_test['GarageQual'].isnull()].index)
gq_train = list(df_train[df_train['GarageQual'].isnull()].index)

df_train['GarageCond'].value_counts()
df_test['GarageCond'].value_counts()

gco_test = list(df_test[df_test['GarageCond'].isnull()].index)
gco_train = list(df_train[df_train['GarageCond'].isnull()].index)

no_garage_index_test = set.intersection(set(gt_test),set(gy_test),set(gf_test),set(gc_test),set(ga_test),
                                        set(gq_test),set(gco_test))
len(no_garage_index_test)

'''Test setindeki 76 tane binanin garaji yokmus.'''

no_garage_index_train = set.intersection(set(gt_train),set(gy_train),set(gf_train),set(gc_train),set(ga_train),
                                        set(gq_train),set(gco_train))
len(no_garage_index_train)

'''Train setindeki 81 tane binanin garaji yokmus. Simdi bu kisimlardaki yanlislari duzeltelim.'''

df_test.iloc[list(no_garage_index_test),[58,60,63,64]] = 'NA'
df_train.iloc[list(no_garage_index_train),[58,60,63,64]] = 'NA'
df_train.iloc[list(no_garage_index_train),59] = 0.0
df_train.iloc[list(no_garage_index_train),[61,62]] = 0
df_test.iloc[list(no_garage_index_test),[59,61,62]] = 0.0

'''Train setindeki garaj degiskenleri ok, ama test setinde hala eksikler var.'''

df_test.iloc[df_test[df_test['GarageYrBlt'].isnull()].index,[58,59,60,61,62,63,64]]

'''Index 1116'da GarageType degiskeni haric hepsi Nan. Bu yuzden bu indexi de garaj yokmus
gibi degerlendirecegim.
Test setindeki garaji olmayan bina sayisi 77'ye cikti.
'''
df_test.iloc[1116,[58,60,63,64]] = 'NA'
df_test.iloc[1116,[59,61,62]] = 0.0

df_test.iloc[df_test[df_test['GarageFinish'].isnull()].index,[58,59,60,61,62,63,64]]

'''Eksik kalan diger kisimlari (0 ve NA haricinde) modlariyla dolduracagim.'''

df_test['GarageYrBlt'].fillna(2005.0, inplace= True)
df_test['GarageFinish'].fillna(df_test['GarageFinish'].mode()[0], inplace= True)
df_test['GarageQual'].fillna(df_test['GarageQual'].mode()[0], inplace= True)
df_test['GarageCond'].fillna(df_test['GarageCond'].mode()[0], inplace= True)

'''Simdi garaj ile ilgili hangi degiskenleri nasil modele alacagima karar verelim.
GarageType,GarageYrBlt degiskenlerini modele alacagim. Fakat GarageFinish ile 
GarageQual'den yeni bir degisken olusturup GarageCond degiskeniyle birlestirecegim.
Boylece garajin bitmeme durumunun(GarageFinish) agirligini bir miktar GarageQual
degiskenine yuklemis olacagim. Cunku bitmemis olan bir garajin puanlamasinin olmasi
beni bunu dusunmeye yonlendirdi.
GarageArea ile GarageCars degiskenlerini de birbirleriyle carpip yeni bir degisken olusturacagim.
Boylece araba kapasitesi fazla olan garajlarin modeldeki etkisini arttirmis olacagim.
'''
df_test.iloc[df_test[df_test['GarageFinish']=='Unf'].index,[58,59,60,61,62,63,64]]

'''SImdi gerekli duzenlemeleri yapalim. Degiskenerimizi sayisal veriye donusturelim.'''

garf = {'NA':0,'Unf':1,'RFn':3,'Fin':5}
df_test['GarageFinish'].replace(garf,inplace=True)
df_train['GarageFinish'].replace(garf,inplace=True)

df_test['GarageFinish'].value_counts()
df_train['GarageFinish'].value_counts()


garq = {'NA':0,'Po':2,'Fa':4,'TA':6,'Gd':8,'Ex':10}
df_test['GarageQual'].replace(garq,inplace=True)
df_train['GarageQual'].replace(garq,inplace=True)

df_test['GarageQual'].value_counts()
df_train['GarageQual'].value_counts()

df_test['GarageCond'].replace(garq,inplace=True)
df_train['GarageCond'].replace(garq,inplace=True)

df_test['GarageCond'].value_counts()
df_train['GarageCond'].value_counts()

'''Simdi yeni degiskenimizi tanimlayalim'''

df_train['Garage'] = df_train['GarageCars'] * df_train['GarageArea'] + df_train['GarageFinish'] * df_train['GarageFinish']*df_train['GarageFinish']*df_train['GarageFinish'] + df_train['GarageQual']*df_train['GarageQual']*df_train['GarageQual'] - df_train['GarageCond']*df_train['GarageCond']*df_train['GarageCond']
df_test['Garage'] =  df_test['GarageCars'] * df_test['GarageArea'] + df_test['GarageFinish']*df_test['GarageFinish']*df_test['GarageFinish']*df_test['GarageFinish'] + df_test['GarageQual']*df_test['GarageQual']*df_test['GarageQual'] - df_test['GarageCond']* df_test['GarageCond']* df_test['GarageCond']
df_test.info()
df_train.info()

# Heating

df_train['Heating'].value_counts()
df_test['Heating'].value_counts()

df_train['HeatingQC'].value_counts()
df_test['HeatingQC'].value_counts()

df_train['CentralAir'].value_counts()
df_test['CentralAir'].value_counts()

heatQC = {'Po':1,'Fa':3,'TA':5,'Gd':7,'Ex':9}
df_test['HeatingQC'].replace(heatQC,inplace=True)
df_train['HeatingQC'].replace(heatQC,inplace=True)

ca = {'Y':5,'N':0}
df_test['CentralAir'].replace(ca,inplace=True)
df_train['CentralAir'].replace(ca,inplace=True)

df_test['HeatingQCA'] = df_test['HeatingQC'] * df_test['HeatingQC'] + df_test['CentralAir']*7
df_train['HeatingQCA'] = df_train['HeatingQC'] * df_train['HeatingQC'] + df_train['CentralAir']*7

df_test.info()
df_train.info()

# Mulkiyetin bolgesel durumu/konumu

'''MSSubClass degiskenini en son karar vereyim, cunku alirsam one hot donusumu uygulamam lazim ki cok fazla degisken oluyor o zaman.'''

df_test['Condition1'].value_counts()

df_train['Condition1'].value_counts()

df_test['Condition2'].value_counts()

df_train['Condition2'].value_counts()

'''Condition1 ile Condition2 degiskeninin fiyat uzerinde onemli bir etkisinin olacagini dusunuyorum.
Ama iki degiskeni birlestirip oyle almak istiyorum. Bu birlestirmeyi yapmadan once puanlama yapacagim.
Condition1'de az puan verdigim turun puanini Condition2'de o miktarda fazla vererek tum turlerin agirliginin
esit olmasini saglayacagim.'''

con1 = {'RRAe':0,'RRNe':1,'PosA':2,'PosN':3,'RRAn':4,'RRNn':5,'Norm':6,'Feedr':7,'Artery':8}
con2 = {'RRAe':8,'RRNe':7,'PosA':6,'PosN':5,'RRAn':4,'RRNn':3,'Norm':2,'Feedr':1,'Artery':0}
df_test['Condition1'].replace(con1,inplace=True)
df_test['Condition2'].replace(con2,inplace=True)
df_train['Condition1'].replace(con1,inplace=True)
df_train['Condition2'].replace(con2,inplace=True)


df_train['Condition'] = df_train['Condition1'] + df_train['Condition2']
df_test['Condition'] = df_test['Condition1'] + df_test['Condition2']


# Satis durumu

df_test['SaleType'].value_counts()
df_train['SaleType'].value_counts()

df_test['SaleCondition'].value_counts()
df_train['SaleCondition'].value_counts()

'''Test setinde SaleType 1 tane eksik.
 Eksik degeri moduyla dolduracagim.'''

df_test['SaleType'].fillna(df_test['SaleType'].mode()[0],inplace=True)

'''Bu iki degisken icin de sonradan karar verecegim.'''

# Olanaklar

df_test['Utilities'].value_counts()

df_train['Utilities'].value_counts()

'''Utilities degiskeninin zaten butun degerleri hemen hemen AllPub oldugu icin almiyorum modele.'''

df_test['HouseStyle'].value_counts()

df_train['HouseStyle'].value_counts()

'''Bu degiskeni sayisallastiralim.'''

hs = {'1Story':1,'1.5Unf':3,'1.5Fin':5,'2Story':7,'2.5Unf':9,'2.5Fin':11,'SFoyer':13,'SLvl':15}
df_test['HouseStyle'].replace(hs,inplace=True)
df_train['HouseStyle'].replace(hs,inplace=True)

df_test.info()
df_train.info()

df_test['MiscFeature'].value_counts()
df_train['MiscFeature'].value_counts()

df_test['MiscVal'].value_counts()
df_train['MiscVal'].value_counts()

mf_index_test = list(df_test[df_test['MiscFeature'].isnull()].index)
mf_index_train = list(df_train[df_train['MiscFeature'].isnull()].index)

mv_index_test = list(df_test[df_test['MiscVal'] == 0].index)
mv_index_train = list(df_train[df_train['MiscVal'] == 0].index)

no_misc_index_test = set.intersection(set(mf_index_test),set(mv_index_test))
no_misc_index_train = set.intersection(set(mf_index_train),set(mv_index_train))

len(no_misc_index_test)
len(no_misc_index_train)

df_train.iloc[list(no_misc_index_train),74] = 'NA'
df_test.iloc[list(no_misc_index_test),74] = 'NA'

'''Test setinde MiscFeature degiskeninin 1 degeri daha bos kaldi.'''

df_test.iloc[df_test[df_test['MiscFeature'].isnull()].index,:]

'''Eksik degeri inceledigimde MiscVal degiskeninin 17000 oldugunu goruyorum
ve bu rakamin digerlerine gore asiri bir deger oldugu ortada. Bu fiyata olsa olsa
 ya asansor ya da Garage2 olur diye tahmin ediyorum. Butun ozellikleri birlikte inceledigimde ise 1 katli bir bina oldugu icin asansor 
 sikkini eledim. Evin genis bir alana sahip olmasindan dolayi da Garage2 olduguna karar verdim.'''

df_test.iloc[df_test[df_test['MiscFeature'].isnull()].index,74] = 'Gar2'

df_train.loc[df_train['MiscFeature'] != 'NA',['MiscFeature','MiscVal']]
df_test.loc[df_test['MiscFeature'] != 'NA',['MiscFeature','MiscVal']]

'''Simdi degiskeni sayisallastiralim.'''
mf = {'NA':0,'Othr':2,'TenC':10,'Shed':6,'Elev':8,'Gar2':4}
df_test['MiscFeature'].replace(mf,inplace=True)
df_train['MiscFeature'].replace(mf,inplace=True)

'''Simdi yeni degiskenimizi olusturalim'''

df_test['New_utilities'] = df_test['HouseStyle'] * df_test['HouseStyle'] + df_test['MiscFeature'] * df_test['MiscVal']
df_train['New_utilities'] = df_train['HouseStyle'] * df_train['HouseStyle'] + df_train['MiscFeature'] * df_train['MiscVal']


df_train.info()
df_test.info()

model_test_cols = [71,73,80,81,82,83,84,85,86,87,88,89,90,91]
len(model_test_cols)

model_train_cols = [71,73,80,81,82,83,84,85,86,87,88,89,90,91,92]

'''Yukarida modele alacagimiz sutunlarin indexlerini tanimladim.
Simdi bu sutunlar icerisinde aslinda int olan fakat float gozuken degerleri int'e donusturecegim.'''

df_test.iloc[:,model_test_cols].info()
df_train.iloc[:,model_train_cols].info()

df_test['Bsmt'].value_counts()
df_train['Bsmt'].value_counts()

df_test['Bsmt'] = df_test['Bsmt'].astype('int')

df_test['AllRooms'].value_counts()
df_train['AllRooms'].value_counts()

df_test['AllRooms'] = df_test['AllRooms'].astype('int')

df_test['Garage'].value_counts()
df_train['Garage'].value_counts()

df_test['Garage'] = df_test['Garage'].astype('int')
df_train['Garage'] = df_train['Garage'].astype('int')

model_df_test = df_test.iloc[:,model_test_cols].copy()
model_df_train = df_train.iloc[:,model_train_cols].copy()

model_df_test.info()
model_df_train.info()

df_train['GrLivArea'].value_counts()
df_test['GrLivArea'].value_counts()
#########################################################################

'''Tum sayisal degiskenlerin SalePrice ile olan korelasyonu'''

num_columns = df_train.select_dtypes(include=[np.number])
num_columns_correlations = num_columns.corr()
print(num_columns_correlations['SalePrice'].sort_values(ascending = False),'/n')

#########################################################################
df_train.groupby('MoSold')['SalePrice'].sum()

model1_test_cols = [17,27,53,80,82,83,85,87,88,89]
len(model1_test_cols)

#Korelasyonu yuksek olup modele alacagim degiskenler: ['OverAllQual','Bsmt','ExterQual','KitchenQual','Garage','NewYear','AllRooms','New_Fireplace','HeatingQCA','Areas','SalePrice']
model1_train_cols = [17,27,53,80,81,83,84,86,88,89,90]
new_df_test = df_test.iloc[:,model1_test_cols].copy()
new_df_train = df_train.iloc[:,model1_train_cols].copy()
new_df_test.info()
new_df_train.info()

'''Yukarida modele alacagimiz sutunlarin indexlerini tanimladim.
Simdi bu sutunlar icerisinde aslinda int olan fakat float gozuken degerleri int'e donusturecegim.'''

df_test['Areas'].value_counts()

new_df_test['Areas'] = new_df_test['Areas'].astype('int')

##########################################################################

'''Simdi modeli kurmaya baslayabiliriz.'''

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

df = new_df_train.copy()


y = df['SalePrice']
x = df.drop(['SalePrice'],axis=1)
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.15,random_state = 42)


'''degiskenlerimize normalizasyon uygulayalim'''

from sklearn.preprocessing import MinMaxScaler
mms = MinMaxScaler()
x_train_normed = mms.fit_transform(x_train)
x_test_normed= mms.fit_transform(x_test)



from sklearn.ensemble import  RandomForestRegressor
rf = RandomForestRegressor()
rf_params = {'n_estimators':[100,200,500,1000],
             'max_features':['auto','sqrt','log2']}
#rf_ = GridSearchCV(rf,rf_params,cv=15).fit(x_train_normed,y_train)
rf_.best_params_

rf_cv = RandomForestRegressor(n_estimators= 100, max_features= 'sqrt').fit(x_train_normed,y_train).predict(x_test_normed)
skore = np.sqrt(mean_squared_error(rf_cv,y_test))


test_normed = mms.fit_transform(new_df_test)
new_df_train_ = new_df_train.drop('SalePrice',axis=1)
new_df_test_ = new_df_train['SalePrice']
new_df_train_normed = mms.fit_transform(new_df_train_)

rf_cv = RandomForestRegressor(n_estimators= 100, max_features= 'sqrt').fit(new_df_train_normed,new_df_test_).predict(test_normed)

sp = pd.read_csv('sample_submission.csv')
x = pd.DataFrame(rf_cv)
sp.loc[:,'SalePrice'] = x.iloc[:,0]

sp.to_csv('sample_submission.csv',index=False)

'''KNN,SVR,MLP,CART,BAGGED TREES,RF,GBM,XGBOOST,LIGHTGBM algoritmalarini denedim.
Iclerinde en iyi sonucu Random Forest ile elde ettim. Bu yuzden sadece rf kod kismini
gosterdim. Modelin ciktisini sample_submission dosyasina aktardim ve kaggle'a yukledim.
Skorum = 0.15'''






