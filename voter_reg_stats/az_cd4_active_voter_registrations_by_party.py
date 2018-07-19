from hellaPy import *
import pandas as pd

df = pd.read_csv('district4_active.csv',delim_whitespace=True)
idf = pd.read_csv('district4_inactive.csv',delim_whitespace=True)

figure(1,figsize=(15,7))
plot(df.date.astype(datetime.datetime),df.D,'b-',mec='b',mfc='b',ms=5)
plot(df.date.astype(datetime.datetime),df.D,'bo-',mec='b',mfc='b',ms=5)
clf()
plot(df.date.astype(datetime.datetime),df.D,'bo-',mec='b',mfc='b',ms=5)
df.columns
df.date = df['date'].apply(lambda x: pd.to_datetime(str(x), format='%Y%m%d'))
df.date
plot(df.date,df.D,'bo-',mec='b',mfc='b',ms=5)
clf()
df.date
close()
plot(df.date,df.D,'bo-',mec='b',mfc='b',ms=5)
plot(df.date,df.R,'ro-',mec='b',mfc='b',ms=5)
plot(df.date,df.R,'ro-',mec='b',mfc='b',ms=5)
plot(df.date,df.R,'ro-',mec='r',mfc='r',ms=5)
