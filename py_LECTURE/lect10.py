"""from faker import Faker as fk
import os

#temp = fk()
temp = fk("ko-KR")
print(temp.name())

folder = "data/"
if not os.path.isdir(folder):
    os.mkdir(folder)

with open(folder + "fktemp.csv", "w", encoding='utf8') as f :
    f.write("name,address,postcode,company,job,phone,email,id,ip_prv,ip_pub,catch_parase,color\n")

with open(folder + "fktemp.csv", "a", newline='', encoding='utf8') as f :
    for i in range(30) :
        f.write(temp.name() + "," + 
            temp.address() + "," + 
            temp.postcode() + "," + 
            temp.company() + "," + 
            temp.job() + "," + 
            temp.phone_number() + "," + 
            temp.email() + "," + 
            temp.user_name() + "," + 
            temp.ipv4_private() + "," + 
            temp.ipv4_public() + "," + 
            temp.catch_phrase() + "," + 
            temp.color_name() + "\n")
"""
"""
import pandas as pd

folder = "data/"
target = folder + "fktemp.csv"

df = pd.read_csv(target)
""""""
#print(df.name == "김성훈")
#print(df.company == "김성훈")

#temp = df[df.postcode > 70000]
#print(temp)

#res = df[df.color == "Indigo"].head(3)
#print(res)

#res = df[df.postcode > 70000][["name", "posrcode","color"]]
#print(res)
#print(res.count)


#temp = df.postcode.mean()
#temp = df.postcode.sum()
#print(temp)

#temp = df[df.color == "Magenta"].postcode.mean()
#print(temp)


#temp = df[df.color == "Magenta"].postcode.sum()
#print(temp)

#temp = df[df.postcode > df.postcode.mean()][["name", "posrcode"]]
#temp = df[df.postcode > df.postcode.mean()]
#print(temp)

#temp = df.company.isnull()
#print(temp)

#temp = df.company.empty
#temp = df[df.company.isnull()][["name", "posrcode"]]
#print(temp)

#temp = df.company.isnull()
#for el in temp:
#    if el ==True:
#        print(el)
        
#temp = df.name.empty
#df[df.company.isnull()][["name", "posrcode"]]
#print(temp)

#temp = df[(df.color == "Magenta")]
#temp = df[~(df.color == "Magenta")]
#temp = df[~(df.color == "Magenta")]["name"]
#print(temp.color.count())


#temp = df[(df.color == "Magenta")&(df.postcode > 70000)]
#temp = df[(df.color == "Magenta")|(df.postcode > 70000)]
#temp = df[(df.color == "Magenta")|(df.postcode > 70000)][["name"]]

#print(temp)


#temp = df.sort_values("postcode")
#print(temp)

#temp = df.sort_values("postcode" ,"name",ascending=False )
#print(temp)

#데이터 재배열

import pandas as pd

col = ['Machine','Country','Price','Brand']
data = [['TV','Korea',1000,'A'],
        ['TV','Japan',1300,'B'],
        ['TV','China',300,'C'],
        ['PC','Korea',2000,'A'],
        ['PC','Japan',3000,'E'],
        ['PC','China',450,'F']]
df = pd.DataFrame(data=data, columns=col)
print(df)

print("\n-----------------------------\n")

print(df.pivot(index='Machine',columns='Country',values='Price'))
print(df.pivot(index='Brand',columns='Machine',values='Price'))
print(df.pivot(index='Country',columns='Machine',values='Price'))
print(df.pivot(index='price',columns='Brand',values='Machine'))"""

"""import pandas as pd 

folder = "data/"
target = folder + "fktemp.csv"

df = pd.read_csv(target)
"""
"""df["aver"] = df.postcode.rank(method="average")
#print(df[["postcode", "aver"]])

df["dense"] = df.postcode.rank(method="dense")
#print(df[["postcode", "dense"]])

df["first"] = df.postcode.rank(method="first")
#print(df[["postcode", "first"]])

df["min"] = df.postcode.rank(method="min")
#print(df[["postcode", "min"]])

df["max"] = df.postcode.rank(method="max")"""
#print(df[["postcode", "max"]])

#print(df[["postcode" ,"max" ,"min" ,"first" ,"dense" ,"aver"]])

#전치 컬럼-로우변환

#print(df.transpose())

#누적 계산
#print(df["postcode"].expanding().sum())
#print(df["postcode"].expanding())

#내림차순 기준
#print(df.postcode.idxmax(axis=0))
#print(df.postcode.idxmin(axis=0))

#empty 추가
#print(df.empty)
#print(df.company.empty)

#검색
#print(df.isin([49732]))

#print(df.isin(["김성훈"]))

#print(df.isin([49732, 96822]))

#print(df.isin([49732, 96822, "서동현"]))

#기기 계산

#period = pd.period_range(start="2023-11-10 00:00:00", end="2023-11-10 02:30:00", freq="30T")
#period = pd.period_range(start="2023-11-10 00:00:00", end="2023-11-10 02:30:00", freq="30T")
#dt = {"col1":[1,2,3,4,5,6],"col2":period}
#idx = ["row1","row2","row3","row4","row5","row6"]
#pf = pd.DataFrame(data=dt, index=idx)
#print(pf)

#인덱스 시간 - 간격 생성

"""#i = pd.date_range("2023-11-10", periods=10, freq="1H")
i = pd.date_range("2023-11-10", periods=10, freq="3H")
df = pd.DataFrame({"col1":[1,2,3,4,5,6,7,8,9,10]}, index=i)
print(df)

print("\n-----------------------------\n")
#특정시간 찾기
print(df.at_time("09:00"))
print(df.at_time("03:00"))

print("\n-----------------------------\n")
"""
#범위 찾기

#df.between_time(start_time="12:00", end_time="00:00")
#df.between_time(start_time="03:00", end_time="09:00")

#X일 간격 생성 - 기간별 찾기

"""i = pd.date_range("2023-11-10", periods=10, freq="3D")
#i = pd.date_range("2023-11-10", periods=10, freq="5D")
df = pd.DataFrame({'col1':[1,2,3,4,5,6,7,8,9,10]}, index=i)
print(df)

#print(df.first("3D"))

print(df.first("5D"))

print(df.first("7D"))"""
"""import pandas as pd 

folder = "data/"
target = folder + "fktemp.csv"

df = pd.read_csv(target)"""

"""df["aver"] = df.postcode.rank(method="average")
#print(df[["postcode", "aver"]])

df["dense"] = df.postcode.rank(method="dense")
#print(df[["postcode", "dense"]])

df["first"] = df.postcode.rank(method="first")
#print(df[["postcode", "first"]])

df["min"] = df.postcode.rank(method="min")
#print(df[["postcode", "min"]])

df["max"] = df.postcode.rank(method="max")"""
#print(df[["postcode", "max"]])

#print(df[["postcode" ,"max" ,"min" ,"first" ,"dense" ,"aver"]])

#전치 컬럼-로우변환

#print(df.transpose())

#누적 계산
#print(df["postcode"].expanding().sum())
#print(df["postcode"].expanding())

#내림차순 기준
#print(df.postcode.idxmax(axis=0))
#print(df.postcode.idxmin(axis=0))

#empty 추가
#print(df.empty)
#print(df.company.empty)

#검색
#print(df.isin([49732]))

#print(df.isin(["김성훈"]))

#print(df.isin([49732, 96822]))

#print(df.isin([49732, 96822, "서동현"]))

#기기 계산

#period = pd.period_range(start="2023-11-10 00:00:00", end="2023-11-10 02:30:00", freq="30T")
#period = pd.period_range(start="2023-11-10 00:00:00", end="2023-11-10 02:30:00", freq="30T")
#dt = {"col1":[1,2,3,4,5,6],"col2":period}
#idx = ["row1","row2","row3","row4","row5","row6"]
#pf = pd.DataFrame(data=dt, index=idx)
#print(pf)

#인덱스 시간 - 간격 생성

"""#i = pd.date_range("2023-11-10", periods=10, freq="1H")
i = pd.date_range("2023-11-10", periods=10, freq="3H")
df = pd.DataFrame({"col1":[1,2,3,4,5,6,7,8,9,10]}, index=i)
print(df)

print("\n-----------------------------\n")
#특정시간 찾기
print(df.at_time("09:00"))
print(df.at_time("03:00"))

print("\n-----------------------------\n")
"""
#범위 찾기

#df.between_time(start_time="12:00", end_time="00:00")
#df.between_time(start_time="03:00", end_time="09:00")

#X일 간격 생성 - 기간별 찾기

"""i = pd.date_range("2023-11-10", periods=10, freq="3D")
#i = pd.date_range("2023-11-10", periods=10, freq="5D")
df = pd.DataFrame({'col1':[1,2,3,4,5,6,7,8,9,10]}, index=i)
print(df)

#print(df.first("3D"))

print(df.first("5D"))

print(df.first("7D"))"""

"""
import FinanceDataReader as fdr

ksp = fdr.DataReader("KS11" , "2001")
print(ksp)
print("\n-----------------------------\n")
"""
#최고가
#res = ksp["High"].max()
#print(res)

#res = ksp["High"].idxmax()
#print(res)


#최저가
#res = ksp["Low"].min()
#print(res)

#최고가
#res = ksp["Volume"].nlargest(n=5)
#res = ksp["Volume"].nlargest(n=10)
#print(res)


#최저가
#res = ksp["Volume"].nsmallest(n=5)
#res = ksp["close"].nsmallest(n=5)
#res = ksp["close"].nlargest(n=5)
#print(res)

#kospi 3000 달성 최초일 찾기
#cond = ksp["Close"] >= 3000
#cond = ksp["Close"] >= 2000
#res= ksp[cond].index[0]
#print(res)

#위(shift) 값 참조, 처리

#res = ksp["Volume"] > ksp["Volume"].shift()
#print(res)

#res = ksp["up"] != ksp["up"].shift().cumsum()
#print(res)

"""ksp["up"] = ksp["Volume"] > ksp["Volume"].shift()
#print(ksp)

#res = ksp["up"] != ksp["up"].shift.cumsum()
#print(res)

ksp["grp"] = (ksp["up"] != ksp["up"].shift()).cumsum() 
#print(ksp)

#연속 증가값 확인

ksp["up_cnt"]=ksp["grp"].groupby(ksp["grp"].values).cumcount() + 1
#print(ksp)
print(ksp["up_cnt"].max())"""

# 변환

"""import pandas as pd 

target = "./data/apt.csv"

df = pd.read_csv(target, encoding="CP949")

df.to_csv("./data/conv_apt.csv", encoding="utf8")

print(df.head())"""
"""
import pandas as pd 

df = pd.read_csv("./data/conv_apt.csv", index_col=0)

print(df.head())
print("\n-----------------------------\n")

df = df.rename(columns={"분양가격(제곱미터)":"분양가"})
#print(df)
#print(df.dtypes)


df["분양가"] = df["분양가"].convert_dtypes()
print(df.dtypes)"""

# array변환

#arr = df.to_numpy()
#print(arr)
#print(arr[2])
#print(len(arr))

#print(df.describe())

"""print(df.transpose())
print("\n-----------------------------\n")
print(df.T.head())"""
