import os
import pandas as pd
directory = 'C:/Users/Michele/Desktop/project/13f'
os.chdir(directory)
outputDirectory = 'C:/Users/Michele/Desktop/project/'
files = os.listdir(directory)
dates = pd.to_datetime([file[:10] for file in files])
#print(*sorted(files), sep="\n")


firstIteration = True
for file, date in zip(files,dates):
    data = pd.read_csv(file)
    data['NAME OF ISSUER']=data['NAME OF ISSUER'].astype(str)
    data['TITLE OF CLASS']=data['TITLE OF CLASS'].astype(str)
    data['CUSIP']=data['CUSIP'].astype(str)
    data['SH/ PRN']=data['SH/ PRN'].astype(str)
    data['PUT/ CALL']=data['PUT/ CALL'].astype(str)
    data['INVESTMENT DISCRETION']=data['INVESTMENT DISCRETION'].astype(str)
    data['OTHER MANAGER']=data['OTHER MANAGER'].astype(str)
    data['SHARED']=data['SHARED'].astype(str)
    data['NONE']=data['NONE'].astype(str)

    data['VALUE (x$1000)']=data['VALUE (x$1000)'].replace(",","",regex = True).astype(int)
    data['VOTING AUTHORITY SOLE']=data['VOTING AUTHORITY SOLE'].replace(",","",regex = True).astype(int)
    data['SHRS OR PRN AMT']=data['SHRS OR PRN AMT'].replace(",","",regex = True).astype(int)
    data["date"] = date
    data["Value % at Quarter"] = data['VALUE (x$1000)']/sum(data['VALUE (x$1000)'])
    if firstIteration == True:
        MergedDataFrame = data
        firstIteration = False
    else:
        MergedDataFrame = pd.merge(MergedDataFrame,data,how = "outer")
        
MergedDataFrame.to_csv(f"{outputDirectory}/berkshire 13-f.csv")