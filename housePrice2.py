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

df_test = test_.copy()
df_train = train_.copy()

df_test.info()
df_train.info()

df_test['MSSubClass'].value_counts()

df_train['MSSubClass'].value_counts()

# MSSubClass IS OK!

df_test['MSZoning'].value_counts()

df_train['MSZoning'].value_counts()

'''Test setinde 4 tane eksik var, moduyla dolduracagim.'''

df_test['MSZoning'].fillna(df_test['MSZoning'].mode()[0],inplace=True)

# MSZoning IS OK!

df_test['LotFrontage'].value_counts()

df_train['LotFrontage'].value_counts()

'''LotFrontage degiskenini modele almayi dusunmuyorum.
Baktigimda evlerin dogrudan bagli oldugu sokaklara olan adim uzakliklari cok farklilik gostermemis.
Fiyat uzerinde cok etkisinin olacagini dusunmuyorum.'''

df_test['LotArea'].value_counts()

df_train['LotArea'].value_counts()

# LotArea IS OK!

df_test.info()
df_train.info()

df_test['Street'].value_counts()

df_train['Street'].value_counts()

# Street IS OK!

df_test['Alley'].value_counts()

df_train['Alley'].value_counts()

'''Alley degiskeninde cok fazla eksik deger var.
Street,PavedDrive degiskenleriyle bir iliskisi olabilir belki.'''

df_train.iloc[0:50,[5,6,65]]
df_test.iloc[0:50,[5,6,65]]

df_test.groupby('PavedDrive')['Street'].value_counts()
df_train.groupby('PavedDrive')['Street'].value_counts()

'''PavedDrive ile Street ayni bilgiyi tasiyor hemen hemen. Ikisi de yolun asfalt durumuyla ilgili bilgi veriyor.
O yuzden PavedDrive degiskenini almiyorum.'''

df_test.groupby('Alley')['Street'].value_counts()
df_train.groupby('Alley')['Street'].value_counts()

'''Aslinda Alley degiskeninde cok fazla eksik deger var ama bu degisken fiyati etkileyebilecek bir degisken.
Muhtemelen bos olan degerler 'NA' olacakti diye dusunerek degisiklik yapacagim.'''

df_train['Alley'].fillna('NA',inplace=True)
df_test['Alley'].fillna('NA',inplace=True)

# Alley IS OK!

df_test.info()
df_train.info()

df_test['LotShape'].value_counts()

df_train['LotShape'].value_counts()

# LotShape IS OK!

df_test['LandContour'].value_counts()

df_train['LandContour'].value_counts()

# LandContour IS OK!

'''Yukaridaki degiskenleri(LandContour,LotShape) aliyorum modele.'''

df_test['Utilities'].value_counts()

df_train['Utilities'].value_counts()

'''Utilities degiskeninin zaten butun degerleri hemen hemen AllPub oldugu icin almiyorum modele.'''

df_test['LotConfig'].value_counts()

df_train['LotConfig'].value_counts()

df_test['LandSlope'].value_counts()

df_train['LandSlope'].value_counts()

df_test['Neighborhood'].value_counts()

df_train['Neighborhood'].value_counts()

'''Yukaridaki degiskenleri de aliyorum.'''

# LotConfig IS OK!

# LandSlope IS OK!

# Neighborhood IS OK!

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

df_test['Condition'].value_counts()
df_train['Condition'].value_counts()

# Condition IS OK!

df_test['BldgType'].value_counts()

df_train['BldgType'].value_counts()

df_test['HouseStyle'].value_counts()

df_train['HouseStyle'].value_counts()

'''Bu iki degiskeni de aliyorum.'''

# BldgType IS OK!

# HouseStyle IS OK!

df_test['OverallQual'].value_counts()

df_train['OverallQual'].value_counts()

df_test['OverallCond'].value_counts()

df_train['OverallCond'].value_counts()

'''Bu iki degisken benzer seyleri ifade ediyor. Ben bu ikisini toplayip tek degisken yapacagim yine.'''

df_test['OverallQC'] = df_test['OverallQual'] + df_test['OverallCond']
df_train['OverallQC'] = df_train['OverallQual'] + df_train['OverallCond']

df_test['OverallQC'].value_counts()
df_train['OverallQC'].value_counts()

# OverallQC IS OK!

df_test['YearBuilt'].value_counts()

df_train['YearBuilt'].value_counts()

df_test['YearRemodAdd'].value_counts()

df_train['YearRemodAdd'].value_counts()

df_train.iloc[:,19:21]

'''Yil degiskenlerinin ikisi de onemli ama soyle bir durum var, eger
tadilat yoksa bu iki degisken ayni tarih oluyor. Yani tadilat olan bina ile olmayan bina
arasinda bir fark olmuyor, bunu duzeltmeliyim.'''

df_test.iloc[[i for i in df_test.index if df_test['YearRemodAdd'][i] == df_test['YearBuilt'][i]],20] = 0

df_train.iloc[[i for i in df_train.index if df_train['YearRemodAdd'][i] == df_train['YearBuilt'][i]],20] = 0

# YearBuilt IS OK!

# YearRemodAdd IS OK!

df_test['RoofStyle'].value_counts()

df_train['RoofStyle'].value_counts()

df_test['RoofMatl'].value_counts()

df_train['RoofMatl'].value_counts()

'''Bu iki degiskeni de aliyorum. Cati da fiyati etkileyecektir.'''

# RoofStyle IS OK!

# RoofMatl IS OK!

df_test['Exterior1st'].value_counts()

df_train['Exterior1st'].value_counts()

df_test['Exterior2nd'].value_counts()

df_train['Exterior2nd'].value_counts()

'''Bu iki degiskenin de test setinde birer tane eksik degeri var.
Dis kaplama da fiyat uzerinde onemli etkiye sahiptir diye dusunuyorum. Bu iki
degiskeni birlestirip tek degisken yapip modele alacagim.'''

'''once eksik degerleri dolduralim modlariyla.'''

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

df_test['Exterior1st'].replace(ext_deg1,inplace=True)

df_train['Exterior1st'].replace(ext_deg1,inplace=True)

df_test['Exterior2nd'].replace(ext_deg2,inplace=True)

df_train['Exterior2nd'].replace(ext_deg2,inplace=True)

'''Puanlama islemini tamamladik. Simdi bu iki degiskeni toplayarak yeni degiskenimizi olusturalim.'''

df_train['Exteriors'] = df_train['Exterior1st'] + df_train['Exterior2nd']

df_test['Exteriors'] = df_test['Exterior1st'] + df_test['Exterior2nd']

df_test.info()
df_train.info()

# Exteriors IS OK!

df_test['MasVnrType'].value_counts()

df_train['MasVnrType'].value_counts()

df_test['MasVnrArea'].value_counts()

df_train['MasVnrArea'].value_counts()

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

df_test.iloc[1150,25] = 'BrkFace' #salladim

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

'''Simdi train setine bakalim.'''

mvt_null_indexs_train = list(df_train[df_train['MasVnrType'].isnull()].index)
mva_null_indexs_train = list(df_train[df_train['MasVnrArea'].isnull()].index)

'''Indexler ayni, suphe uyandirici bir durum yok. 
O yuzden dolduruyorum...'''

df_train['MasVnrType'].fillna('None',inplace=True)
df_train['MasVnrArea'].fillna(0.0,inplace=True)

df_train.info()

# MasVnrType IS OK!

# MasVnrArea IS OK!


df_test['ExterQual'].value_counts()

df_train['ExterQual'].value_counts()

df_test['ExterCond'].value_counts()

df_train['ExterCond'].value_counts()

'''Bu iki degiskeni birlestirip tek bir degisken yapacagim.'''

qc = {'Po':1,'Fa':3,'TA':5,'Gd':7,'Ex':9}

df_test['ExterQual'].replace(qc,inplace=True)
df_train['ExterQual'].replace(qc,inplace=True)
df_test['ExterCond'].replace(qc,inplace=True)
df_train['ExterCond'].replace(qc,inplace=True)

df_train['ExterQC'] = df_train['ExterQual'] + df_train['ExterCond']
df_test['ExterQC'] = df_test['ExterQual'] + df_test['ExterCond']

df_test.info()
df_train.info()

# ExterQC IS OK!

df_test['Foundation'].value_counts()

df_train['Foundation'].value_counts()

# Foundation IS OK!

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

'''Test setindeki bodrum olmayan binalarin indexleri(41 tane);
[125, 133, 269, 318, 354, 387, 388, 396, 397, 398, 400, 455, 590, 606, 608, 660, 662, 729, 730, 733, 756, 764, 927, 975, 
992, 993, 1030, 1038, 1087, 1092, 1104, 1118, 1139, 1242, 1303, 1306, 1343, 1344, 1364, 1431,1444]

Train setindeki bodrum olmayan binalarin indexleri(37 tane);
[17, 39, 90, 102, 156, 182, 259, 342, 362, 371, 392, 520, 532, 533, 553, 646, 705, 736, 749, 778, 868, 894, 897, 984, 1000,
 1011, 1035, 1045, 1048, 1049, 1090, 1179, 1216, 1218, 1232, 1321,1412]
'''
a = set.difference(set(bsmntc_null_index_test),set(no_basement_index_test))

df_test.iloc[list(a),[30,31,32,33,34,35,36,37,38,47,48]]

'''BsmtFullBath ve BsmtHalfBath degiskeninde 728 indexinin olmadigini farkettim. Halbuki diger tum degerleri bodrum olmadigina dair bilgi iceriyor.
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
BsmtQual,BsmtCond,BsmtExposure degiskenlerini alacagim ama once sayisala donusturecegim.
TotalBsmtSF ve bitmis alan yuzdesini iceren bir degisken olsun. BsmtFinType1 ve BsmtFinType2 degiskenlerini de birlestireyim.
Diger bodrum degiskenlerini modele almayacagim.
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

# BsmtCond IS OK!

# BsmtQual IS OK!

# BsmtExposure IS OK!

df_train.info()
df_test.info()

'''TotalBsmtSF ve bitmis alan yuzdesini iceren degiskeni olusturalim simdi;'''

df_test['TotalBsmtSF'].value_counts()
'''TotalBsmtSF degiskeninde 0.0 degerleri de oldugu icin asagidaki esitlik bazi degerler icin istenen
sonucu vermeyecektir. Bu kisimlari duzeltecegim.'''

df_test['BsmtFinPerc'] = (df_test['TotalBsmtSF'] - df_test['BsmtUnfSF'])/ df_test['TotalBsmtSF']
df_test['BsmtFinPerc'].fillna(0.0,inplace=True)

df_test['BsmtFinPerc'].value_counts()

df_train['BsmtFinPerc'] = (df_train['TotalBsmtSF'] - df_train['BsmtUnfSF'])/ df_train['TotalBsmtSF']
df_train['BsmtFinPerc'].fillna(0.0,inplace=True)

df_train['BsmtFinPerc'].value_counts()
# BsmtFinPerc IS OK!

# TotalBsmtSF IS OK!

'''BsmtFinType1 ve BsmtFinType2 degiskenlerini birlestirelim. Oncesinde sayisala donusturelim.'''

b_types = {'GLQ':10,'ALQ':8,'BLQ':6,'Rec':4,'LwQ':2,'Unf':0,'NA':0}

df_test['BsmtFinType1'].replace(b_types,inplace=True)

df_train['BsmtFinType1'].replace(b_types,inplace=True)

df_test['BsmtFinType2'].replace(b_types,inplace=True)

df_train['BsmtFinType2'].replace(b_types,inplace=True)

df_train['BsmtFinType1'].value_counts()
df_test['BsmtFinType1'].value_counts()

df_train['BsmtFinType2'].value_counts()
df_test['BsmtFinType2'].value_counts()

df_train['BsmtFinT'] = ((df_train['BsmtFinSF1']* df_train['BsmtFinType1'])
                               + (df_train['BsmtFinSF2']* df_train['BsmtFinType2']))/(df_train['TotalBsmtSF'] - df_train['BsmtUnfSF'])
df_train['BsmtFinT'].fillna(0.0,inplace=True)

df_test['BsmtFinT'] = ((df_test['BsmtFinSF1']* df_test['BsmtFinType1'])
                               + (df_test['BsmtFinSF2']* df_test['BsmtFinType2']))/(df_test['TotalBsmtSF'] - df_test['BsmtUnfSF'])
df_test['BsmtFinT'].fillna(0.0,inplace=True)

df_train.info()
df_test.info()

# BsmtFinT IS OK!

df_train['Heating'].value_counts()
df_test['Heating'].value_counts()

df_train['HeatingQC'].value_counts()
df_test['HeatingQC'].value_counts()

df_train['CentralAir'].value_counts()
df_test['CentralAir'].value_counts()

'''Heating degiskenini alacagim modele. HeatingQC ile CentralAir degiskenini de birlerstirip tek bir degisken yapacagim.'''

# Heating IS OK!

heatQC = {'Po':1,'Fa':3,'TA':5,'Gd':7,'Ex':9}

df_test['HeatingQC'].replace(heatQC,inplace=True)

df_train['HeatingQC'].replace(heatQC,inplace=True)

ca = {'Y':5,'N':0}

df_test['CentralAir'].replace(ca,inplace=True)

df_train['CentralAir'].replace(ca,inplace=True)

df_test['HeatingQCA'] = df_test['HeatingQC'] + df_test['CentralAir']

df_train['HeatingQCA'] = df_train['HeatingQC'] + df_train['CentralAir']

# HeatingQCA IS OK!

df_train['Electrical'].value_counts()
df_test['Electrical'].value_counts()

'''Electrical degiskeninde test ve train setinde birer eksik deger var. Modlariyla dolduruyorum.'''

df_train['Electrical'].fillna(df_train['Electrical'].mode()[0],inplace=True)
df_test['Electrical'].fillna(df_test['Electrical'].mode()[0],inplace=True)

df_train.info()
df_test.info()


el = {'Mix':1,'FuseP':3,'FuseF':5,'FuseA':7,'SBrkr':9}

df_test['Electrical'].replace(el,inplace=True)

df_train['Electrical'].replace(el,inplace=True)

# Electrical IS OK!

'''Simdi yasam alanlari ile ilgili degiskenleri beraber inceleyip hangilerini alacagimiza karar verelim.
Ilgili degiskenler;
1stFlrSF,2ndFlrSF,LowQualFinSF,GrLivArea.
'''

df_train['LowQualFinSF'].value_counts()
df_test['LowQualFinSF'].value_counts()

df_train['GrLivArea'].value_counts()
df_test['GrLivArea'].value_counts()

'''Bu iki degiskeni almayi dusunuyorum. Birinci kat ikinci kat diye ayirmak yerine toplam
alani dahil edelim modele.'''

# GrLivArea IS OK!

# LowQualFinSF IS OK!

'''Simdi odalarla ilgili degiskenlere bakalim.
Yine ayni sekilde toplam oda sayilarini modele almayi dusunuyorum.
Ilgili degiskenler;
FullBath,HalfBath,BedroomAbvGr,KitchenAbvGr,KitchenQual,TotRmsAbvGrd.
FullBath,HalfBath bu iki degiskeni toplayip tek bir degisken yapalim.
KitchenQual degiskeninin test setinde 1 eksik degeri var.
'''
df_train['FullBath'].value_counts()
df_test['FullBath'].value_counts()

df_train['HalfBath'].value_counts()
df_test['HalfBath'].value_counts()

df_test['AllBath'] = df_test['FullBath'] + df_test['HalfBath']//2

df_train['AllBath'] = df_train['FullBath'] + df_train['HalfBath']//2

df_train.info()
df_test.info()

# AllBath IS OK!

df_train['KitchenAbvGr'].value_counts()
df_test['KitchenAbvGr'].value_counts()

# KitchenAbvGr IS OK!

df_train['KitchenQual'].value_counts()
df_test['KitchenQual'].value_counts()

df_train['KitchenQual'].fillna(df_train['KitchenQual'].mode()[0],inplace=True)

df_test['KitchenQual'].fillna(df_test['KitchenQual'].mode()[0],inplace=True)

kitc = {'Po':1,'Fa':3,'TA':5,'Gd':7,'Ex':9}

df_test['KitchenQual'].replace(kitc,inplace=True)

df_train['KitchenQual'].replace(kitc,inplace=True)

# KitchenQual IS OK!

df_train['TotRmsAbvGrd'].value_counts()
df_test['TotRmsAbvGrd'].value_counts()

# TotRmsAbvGrd IS OK!

df_train['Functional'].value_counts()
df_test['Functional'].value_counts()

'''Test setinde 2 degeri eksik.'''

df_test['Functional'].fillna(df_test['Functional'].mode()[0],inplace=True)

f = {'Sal':1,'Sev':3,'Maj2':5,'Maj1':7,'Mod':9,'Min2':11,'Min1':13,'Typ':15}

df_test['Functional'].replace(f,inplace=True)

df_train['Functional'].replace(f,inplace=True)

# Functional IS OK!

df_train['Fireplaces'].value_counts()
df_test['Fireplaces'].value_counts()

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

# Fireplaces IS OK!

# FireplaceQu IS OK!

df_train.info()
df_test.info()

'''Simdi garaj ile ilgili degiskenleri inceleyelim.
Ilgili degiskenler;
GarageType,GarageYrBlt,GarageFinish,GarageCars,GarageArea,GarageQual,GarageCond

Garaj ile ilgili degiskenlerin tamaminda eksikler var. Once kac tane binanin garaji yok onu ogrenelim.'''

df_train['GarageType'].value_counts()
df_test['GarageType'].value_counts()

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

# GarageType IS OK!

# GarageYrBlt IS OK!

'''Simdi GarageFinish ile GarageQual'den yeni bir degisken olusturup GarageCond degiskeniyle birlestirecegim'''

df_train['GarageFinQ'] = (df_train['GarageFinish']*df_train['GarageQual']) + df_train['GarageCond']
df_test['GarageFinQ'] = (df_test['GarageFinish']*df_test['GarageQual']) + df_test['GarageCond']

# GarageFinQ IS OK!

'''Simdi GarageArea ile GarageCars degiskenlerini de birbirleriyle carpip yeni bir degisken olusturacagim.
Boylece daha fazla arac kapasitesi olan garajlarin modeldeki etkisi artmis olacak.
'''
df_test['GarageACars'] = df_test['GarageArea'] * df_test['GarageCars']
df_train['GarageACars'] = df_train['GarageArea'] * df_train['GarageCars']

# GarageACars IS OK!

df_test['WoodDeckSF'].value_counts()
df_train['WoodDeckSF'].value_counts()

# WoodDeckSF IS OK!

'''Simdi veranda alaniyla ilgili degiskenleri inceleyelim.
Ilgili degiskenler;
OpenPorchSF,EnclosedPorch,3SsnPorch,ScreenPorch.
'''
df_train.info()
df_test.info()

'''Verisetlerinde eksik deger yok.'''

df_test['OpenPorchSF'].value_counts()
df_train['OpenPorchSF'].value_counts()

df_test['EnclosedPorch'].value_counts()
df_train['EnclosedPorch'].value_counts()

df_test['3SsnPorch'].value_counts()
df_train['3SsnPorch'].value_counts()

df_test['ScreenPorch'].value_counts()
df_train['ScreenPorch'].value_counts()

'''Bu degiskenleri oldugu gibi aliyorum.'''

# OpenPorchSF IS OK!

# EnclosedPorch IS OK!

# 3SsnPorch IS OK!

# ScreenPorch IS OK!

df_test['PoolArea'].value_counts()
df_train['PoolArea'].value_counts()

df_test['PoolQC'].value_counts()
df_train['PoolQC'].value_counts()

'''PoolQC degiskeninde her iki veriseti icin de cok eksik var.'''

pa_index_test = list(df_test[df_test['PoolArea'] == 0].index)
pa_index_train = list(df_train[df_train['PoolArea'] == 0].index)

pqc_index_test = list(df_test[df_test['PoolQC'].isnull()].index)
pqc_index_train = list(df_train[df_train['PoolQC'].isnull()].index)

no_pool_index_test = set.intersection(set(pqc_index_test),set(pa_index_test))
no_pool_index_train = set.intersection(set(pqc_index_train),set(pa_index_train))

len(no_pool_index_test)
len(no_pool_index_train)

'''Her iki verisetinde de 1453 tane havuzu olmayan bina var.'''

df_train.iloc[list(no_pool_index_train),72] = 'NA'
df_test.iloc[list(no_pool_index_test),72] = 'NA'

'''Test setinin PoolQC degiskeninde 3 tane eksik kaldi.'''
df_test.iloc[df_test[df_test['PoolQC'].isnull()].index,[71,72]]

df_test.groupby('PoolArea')['PoolQC'].value_counts()

df_test['PoolQC'].fillna('Gd',inplace=True)
'''Bir sey bulamadim ve 3 degeri Gd yaptim.'''

'''PoolQC ile PoolArea degiskenini carpip tek bir degisken olarak almak istiyorum modele.'''

pool = {'NA':0,'Fa':2,'TA':4,'Gd':6,'Ex':8}

df_test['PoolQC'].replace(pool,inplace=True)

df_train['PoolQC'].replace(pool,inplace=True)

df_test['PoolAreaQC'] = df_test['PoolQC'] * df_test['PoolArea']
df_train['PoolAreaQC'] = df_train['PoolQC'] * df_train['PoolArea']

# PoolAreaQC IS OK!

df_test['Fence'].value_counts()
df_train['Fence'].value_counts()

'''Fence degiskeninin cok fazla eksik degeri olmasi sebebiyle normalde silinebilirdi ama
 fiyata etkisinin cok olacagini dusundugum icin bos degerleri NA olacak sekilde dolduracagim. '''

df_train['Fence'].fillna('NA', inplace=True)
df_test['Fence'].fillna('NA', inplace=True)

fence = {'NA':0,'MnWw':2,'GdWo':4,'MnPrv':6,'GdPrv':8}

df_test['Fence'].replace(fence,inplace=True)

df_train['Fence'].replace(fence,inplace=True)


# Fence IS OK!

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
 ya asansor ya da tenis kortu olur diye tahmin ediyorum. Butun ozellikleri birlikte inceledigimde ise 1 katli bir bina oldugu icin asansor 
 sikkini eledim. Evin genis bir alana sahip olmasindan dolayi da tenis kortu olduguna karar verdim.'''

df_test.iloc[df_test[df_test['MiscFeature'].isnull()].index,74] = 'TenC'

# MiscFeature IS OK!

# MiscVal IS OK!

df_test['MoSold'].value_counts()
df_train['MoSold'].value_counts()

df_test['YrSold'].value_counts()
df_train['YrSold'].value_counts()

df_test['SaleType'].value_counts()
df_train['SaleType'].value_counts()

df_test['SaleCondition'].value_counts()
df_train['SaleCondition'].value_counts()

'''Test setinde SaleType 1 tane eksik. Bu degiskenlerin dordunu de modele alacagim.
 Eksik degeri de moduyla dolduracagim.'''

df_test['SaleType'].fillna(df_test['SaleType'].mode()[0],inplace=True)

# MoSold IS OK!

# YrSold IS OK!

# SaleType IS OK!

# SaleCondition IS OK!

df_train.info()
df_test.info()

model_test_cols = [1,2,4,5,6,7,8,10,11,12,15,16,19,20,21,22,25,26,29,30,31,32,38,39,42,45,46,52,53,54,55,
                   56,57,58,59,66,67,68,69,70,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90]

len(model_test_cols)
model_train_cols = [1,2,4,5,6,7,8,10,11,12,15,16,19,20,21,22,25,26,29,30,31,32,38,39,42,45,46,52,53,54,55,
                   56,57,58,59,66,67,68,69,70,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91]

'''Yukarida modele alacagimiz sutunlarin indexlerini tanimladim.
Simdi bu sutunlar icerisinde aslinda int olan fakat float gozuken degerleri int'e donusturecegim.'''

df_test.iloc[:,model_test_cols].info()
df_train.iloc[:,model_train_cols].info()

df_test['MasVnrArea'].value_counts()
df_train['MasVnrArea'].value_counts()

df_test['MasVnrArea'] = df_test['MasVnrArea'].astype('int')
df_train['MasVnrArea'] = df_train['MasVnrArea'].astype('int')

df_test['TotalBsmtSF'].value_counts()
df_train['TotalBsmtSF'].value_counts()

df_test['TotalBsmtSF'] = df_test['TotalBsmtSF'].astype('int')

df_test['GarageYrBlt'].value_counts()
df_train['GarageYrBlt'].value_counts()

df_test['GarageYrBlt'] = df_test['GarageYrBlt'].astype('int')
df_train['GarageYrBlt'] = df_train['GarageYrBlt'].astype('int')

df_test['GarageACars'].value_counts()
df_train['GarageACars'].value_counts()

df_test['GarageACars'] = df_test['GarageACars'].astype('int')

model_df_test = df_test.iloc[:,model_test_cols]
model_df_train = df_train.iloc[:,model_train_cols]

model_df_test.info()
model_df_train.info()
