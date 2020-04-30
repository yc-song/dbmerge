import pandas as pd
import glob
import xlrd
import openpyxl

#우선 모든 자료들을 raw data folder에 저장
all_data = pd.DataFrame()
all_data1 = pd.DataFrame()
for f in glob.glob("rawdata/*.xlsx"): #rawdata 디렉토리에 있는 xlsx파일들 불러옴
    df=pd.read_excel(f, sheet_name=None)
    all_data1 = pd.concat(df, ignore_index=True)
###########
    all_data1.rename(columns={"Gender":"성별","Age":"나이","Name":"이름"},inplace=True) #추가된 부분
###########
    all_data=all_data.append(all_data1,ignore_index=True)

for f in glob.glob("rawdata/*.csv"): #csv 불러옴
    df=pd.read_csv(f,index_col=None, header=0, encoding='UTF8')
    all_data1 = pd.concat([df], ignore_index=True)
    all_data1.rename(columns={"Gender":"성별","Age":"나이","Name":"이름"},inplace=True)
    all_data=all_data.append(all_data1,ignore_index=True)

all_data.to_excel('합본.xlsx',encoding='utf-8-sig') #저장
# all_data.to_csv('합본.csv',encoding='utf-8-sig') #csv로 저장
