#타이타닉 정보
"""
import pandas as pd 
tr = pd.read_csv("data/train.csv")

#print(tr)
print("\n--------------------------------\n")
#print(tr.head())


res= tr.isnull().sum()
print(res)"""
"""
#숭선지
print("\n--------------------------------\n")

res= pd.crosstab(tr["Embarked"], tr["Survived"])
#print(res)

res.columns.map({0:"Dead", 1:"Alive"})
#print(res)

#연령
print("\n--------------------------------\n")

res= pd.crosstab(tr["Age"], tr["Survived"])
#print(res)

res.columns = res.columns.map({0:"Dead", 1:"Alive"})
#print(res)


#passenger class
print("\n--------------------------------\n")
res= pd.crosstab(tr["Pclass"], tr["Survived"])
#print(res)

#성별별
res= pd.crosstab(tr["Sex"], tr["Survived"])
#print(res)

#Allen, Mr, William Henry
tr["Title"]= tr.Name.str.extract(" ([A-Za-z]+)\.")
res= tr["Title"].value_counts()
#print(res)

tr["Title"] = tr["Title"].replace(["Capt", "Col", "Countess", "Don","Dona", "Dr", "Jonkheer", "Lady","Major", "Rev", "Sir"], "Other")
tr["Title"] = tr["Title"].replace("Mlle", "Miss")
tr["Title"] = tr["Title"].replace("Mme", "Mrs")
tr["Title"] = tr["Title"].replace("Ms", "Miss")
res= tr["Title"].value_counts()
#print(res)

#print(tr["Age"].isnull())
#print(tr["Age"].isnull(),sum())


meanAge = tr[["Title" , "Age"]].groupby(["Title"]).mean()
#print(meanAge)
#print(tr["Age"].head(20))


print("\n--------------------------------\n")

for index, row in meanAge.iterrows():
    nullIndex = tr[(tr.Title == index) & (tr.Age.isnull())].index
    # print(nullIndex, index, row[0])
    tr.loc[nullIndex, "Age"] = row[0]
    
#print(tr["Age"].isnull())
#print(tr["Age"].isnull(),sum())

tr["AgeCate"] = pd.qcut(tr.Age, 8, labels=range(1, 9))
#print(tr.head())

print("\n--------------------------------\n")

#print(tr.dtypes)

tr.AgeCate = tr.AgeCate.astype(int)
#print(tr.head())
#print(tr.dtypes)

tr.Cabin.fillna("N", inplace=True)

tr["CabinCate"] = tr["Cabin"].str.slice(start=0, stop=1)
#print(tr["CabinCate"].value_counts())


# 객실

tr["CabinCate"] = tr["CabinCate"].map({ "N": 0, "C": 1, "B": 2, "D": 3, "E": 4, "A": 5, "F": 6, "G": 7, "T": 8 })
#tr.CabinCate = tr.CabinCate.astype
#print(tr.dtypes)
#print(tr)
#print(tr["CabinCate"].value_counts())

#방번호별 생존자

res = pd.crosstab(tr["CabinCate"], tr["Survived"])
#print(res)


#요금컬럼 별 구간 구분
#print(tr.Fare)

print("\n--------------------------------\n")

#print(tr["Fare"]. value_counts())

tr["FareCate"] = pd.qcut(tr.Fare, 8, labels=range(1, 9))
#tr["FareCate"] = pd.qcut(tr.Fare, 5, labels=range(1, 6))
#tr.FareCate = tr.FareCate.astype(int)
#print(tr["CabinCate"].value_counts())


# 요금 구간별 생존자

res = pd.crosstab(tr["FareCate"], tr["Survived"])
#print(res)
"""

#아이리스 정보 처리

"""
import pandas as pd 
df = pd.read_csv("./data/Iris.csv", index_col="Id")

print(df.head())


df.rename(columns={
    "SepalLengthCm": "꽃받침길이",
    "SepalWidthCm": "꽃받침너비",
    "PetalLengthCm": "꽃잎길이",
    "PetalWidthCm": "꽃잎너비", 
    "Species": "품종"},
    inplace=True
)"""

"""
ir = df.rename(columns={
    "SepalLengthCm": "꽃받침길이",
    "SepalWidthCm": "꽃받침너비",
    "PetalLengthCm": "꽃잎길이",
    "PetalWidthCm": "꽃잎너비", 
    "Species": "품종"},
)

#print(ir.head())

print("\n--------------------------------\n")


res = ir.iloc[:, [0, 1, 4]]
#print(res)


ir["품종"] = ir["품종"].str[5:]
#print(ir)


res= ir.groupby("품종").mean()
#print(res)

res= ir["품종"].value_counts()
#print(res)"""


import matplotlib.pyplot as plt

#기본 사용 y
#value = [1, 2, 3, 4]
#value = [2, 4, 5, 7, 10]
#res = plt.plot(value)
#plt.show()



#두축 설정하기

#x_value = [2, 3, 6, 7, 10]
#y_value = [1, 4, 5, 8, 9]

#plt.plot(x_value, y_value)
#plt.plot([2, 4, 6, 8, 10],[1, 3, 5, 7, 9])
#plt.show()

#딕셔너리 사용, 두축 지정 구성

#dic_val = {"x_data": [2,3,6,7,10], "y_data": [1,4,5,8,9]}

#plt.plot("x_data", "y_data", data=dic_val)

#plt.show()


#dic_val = {"x_data": [2,3,6,7,10], "y_data": [1,4,5,8,9]}

#plt.plot("x_data", "y_data", data=dic_val)

#plt.xlabel("ttttt")
#plt.ylabel("y_data")
#plt.show()

#레이블 여백 위치 조절
"""
dic_val = {"x_data": [2,3,6,7,10], "y_data": [1,4,5,8,9]}

plt.plot("x_data", "y_data", data=dic_val)

#plt.xlabel("x_data", labelpad=15)
#plt.ylabel("y_data", labelpad=50)

plt.xlabel("x_data", labelpad=10, loc="right")
plt.ylabel("y_data", labelpad=50, loc= "bottom")

plt.show()
"""


"""plt.xlabel("x_data", loc="right")
plt.ylabel("y_data", loc="top")

plt.show()
"""

#다중데이터 출력
"""dic_val = {"x_data": [2,3,6,7,10], "y_data": [1,4,5,8,9]}
dic1_val = {"x1_data": [1,3,5,7,9], "y1_data": [2,4,6,8,10]}

plt.plot("x_data", "y_data", data=dic_val)
plt.plot("x1_data", "y1_data", data=dic1_val)

plt.xlabel("x_data")
plt.ylabel("y_data")
plt.show()
"""


#라벨 출력

"""dic_val = {"x_data": [2,3,6,7,10], "y_data": [1,4,5,8,9]}

plt.plot("x_data", "y_data", data=dic_val, label="PData(km)")
plt.xlabel("x_data")
plt.ylabel("y_data")
plt.legend()
plt.show()"""

#라벨 위치 조절

"""dic_val = {"x_data": [2,3,6,7,10], "y_data": [1,4,5,8,9]}

plt.plot("x_data", "y_data", data=dic_val, label="PData(km)")
plt.xlabel("x_data")
plt.ylabel("y_data")

#plt.legend()
#plt.legend(loc=(1, 1))
#plt.legend(loc="lower right")

plt.legend(loc = "lower right")
plt.legend(loc = "center right")
plt.legend(loc = "upper right")
plt.legend(loc = "lower left")
plt.legend(loc = "upper center")"""


#라벨 설정

"""dic_val = {"x_data": [2,3,6,7,10], "y_data": [1,4,5,8,9]}
dic1_val = {"x1_data": [1,3,5,7,9], "y1_data": [2,4,6,8,10]}

plt.plot("x_data", "y_data", data=dic_val)
plt.plot("x1_data", "y1_data", data=dic1_val)

plt.xlabel("x_data")
plt.ylabel("y_data")


#col조절
#plt.legend(ncol =1)
plt.legend(ncol =2)
plt.show()


# 폰트 조절
#plt.legend(ncol=2, fontsize=10)
plt.legend(ncol=2, fontsize=20)

#테두리 설정
#plt.legend(ncol=2, fontsize=10, frameon=True)
plt.legend(ncol=2, fontsize=10, frameon=False)

#테두리 음영
plt.legend(ncol=2, fontsize=10, shadow=True)
"""

dic_val = {"x_data": [2,3,6,7,10], "y_data": [1,4,5,8,9]}

"""plt.plot("x_data", "y_data", data=dic_val)
plt.xlabel("x_data")
plt.ylabel("y_data")
"""
#plt.xlim()
#plt.ylim()



#축 범위 출력

"""x_min, x_max = plt.xlim()
y_min, y_max = plt.ylim()
plt.xlim(x_min , x_max)
plt.ylim(y_min , y_max)

"""
# 축 계산
#plt.xlim(x_min - 0.6, x_max)
#plt.ylim(y_min - 0.6, y_max)


#축 범위 지정
#plt.xlim([0, 10])
#plt.ylim([0, 10])

#plt.xlim([0, 50])
#plt.ylim([0, 50])




#두축 값 동시 확인
#plt.axis([0, 10, 0, 10])
#plt.axis([-5, 10, -5, 10])
#plt.axis([0, 50, 0, 50])
#plt.axis([0, 20, 0, 50])

#x_min, x_max, ymin, ymax = plt.axis()
#print(x_min, x_max, ymin, ymax)
#plt.axis([x_min, x_max, ymin, ymax])


#축 출력 옵션 지정

#plt.axis("square")
#plt.axis("scaled")
#plt.axis("of")
#plt.axis("on")
#plt.axis("auto")
#plt.axis("equal")

#선 스타일 설정
import matplotlib.pyplot as plt

#plt.plot([2,3,6,7,10], [1,4,5,8,9], "-", label="PData(km)")

#plt.plot([2,3,6,7,10], [1,4,5,8,9], "-", label="PData(km)")
#plt.plot([2,3,6,7,10], [1,4,5,8,9], "--", label="PData(km)")
#plt.plot([2,3,6,7,10], [1,4,5,8,9], ":", label="PData(km)")
#plt.plot([2,3,6,7,10], [1,4,5,8,9], ".", label="PData(km)")
#plt.plot([2,3,6,7,10], [1,4,5,8,9], ",", label="PData(km)")
#plt.plot([2,3,6,7,10], [1,4,5,8,9], ".-", label="PData(km)")
#plt.plot([2,3,6,7,10], [1,4,5,8,9], ".--", label="PData(km)")


#plt.plot([2,3,6,7,10], [1,4,5,8,9], linestle = "solid" , label = "PData(km)")
#plt.plot([2,3,6,7,10], [1,4,5,8,9], linestle = "solid" , label = "PData(km)")
#plt.plot([2,3,6,7,10], [1,4,5,8,9], linestle = "dashed" , label = "PData(km)")
#plt.plot([2,3,6,7,10], [1,4,5,8,9], linestle = "dotted" , label = "PData(km)")
#plt.plot([2,3,6,7,10], [1,4,5,8,9], linestle = "dashdot" , label = "PData(km)")

#solid 픽셀 크기 간격
#plt.plot([2,3,6,7,10], [1,4,5,8,9], linestle = (0,(1, 0)) , label="PData(km)")
#plt.plot([2,3,6,7,10], [1,4,5,8,9], linestle = (0,(4, 2)) , label="PData(km)")
#plt.plot([2,3,6,7,10], [1,4,5,8,9], linestle = (0,(10, 1)) , llabel="PData(km)")

#색
#plt.plot([1,3,5,7,9], [2,4,6,8,10], "-", color="r", label="Value(m)")
#plt.plot([1,3,5,7,9], [2,4,6,8,10], "-", color="g", label="Value(m)")
#plt.plot([1,3,5,7,9], [2,4,6,8,10], "-", color="b", label="Value(m)")
#plt.plot([1,3,5,7,9], [2,4,6,8,10], "-", color="red", label="Value(m)")
#plt.plot([1,3,5,7,9], [2,4,6,8,10], "-", color="lime", label="Value(m)")
#plt.plot([1,3,5,7,9], [2,4,6,8,10], "-", color="C1", label="Value(m)")
#plt.plot([1,3,5,7,9], [2,4,6,8,10], "-", color="C2", label="Value(m)")
#plt.plot([1,3,5,7,9], [2,4,6,8,10], "-", color="#75FA8D", label="Value(m)")


#스타일

#plt.plot([1,3,5,7,9], [2,4,6,8,10], linestyle="solid", linewidth=10,coloer= "C6", label="Value(m)")
#plt.plot([1,3,5,7,9], [2,4,6,8,10], linestyle="solid", linewidth=5,coloer= "C6", label="Value(m)")
#plt.plot([1,3,5,7,9], [2,4,6,8,10], linestyle="solid", linewidth=10, solid_capstyle="round",coloer= "C6", label="Value(m)")
#plt.plot([1,3,5,7,9], [2,4,6,8,10], linestyle="solid", linewidth=5, solid_capstyle="round",coloer= "C6", label="Value(m)")
#plt.plot([1,3,5,7,9], [2,4,6,8,10], linestyle="dashed", linewidth=10,coloer= "C6", label="Value(m)")
#plt.plot([1,3,5,7,9], [2,4,6,8,10], linestyle="dashed", linewidth=5,coloer= "C6", label="Value(m)")
#plt.plot([1,3,5,7,9], [2,4,6,8,10], linestyle="dashed", linewidth=10, dash_capstyle="butt",coloer= "C6", label="Value(m)")
#plt.plot([1,3,5,7,9], [2,4,6,8,10], linestyle="dashed", linewidth=5, dash_capstyle="butt",coloer= "C6", label="Value(m)")


#마커 지정


#plt.plot([2,3,6,7,10], [1,4,5,8,9], "cd", label="PData(km)")
#plt.plot([2,3,6,7,10], [1,4,5,8,9], "bo", label="PData(km)")

#plt.plot([2,3,6,7,10], [1,4,5,8,9], "go", label="PData(km)")
#plt.plot([2,3,6,7,10], [1,4,5,8,9], "co--", label="PData(km)")
#plt.plot([2,3,6,7,10], [1,4,5,8,9], "kd-", label="PData(km)")


#plt.plot([2,3,6,7,10], [1,4,5,8,9], marker="H", label="PData(km)")
#plt.plot([2,3,6,7,10], [1,4,5,8,9], marker="D", label="PData(km)")
#plt.plot([2,3,6,7,10], [1,4,5,8,9], marker="x", label="PData(km)")
#plt.plot([2,3,6,7,10], [1,4,5,8,9], marker=11, label="PData(km)")
#plt.plot([2,3,6,7,10], [1,4,5,8,9], marker="s", label="PData(km)")
#plt.plot([2,3,6,7,10], [1,4,5,8,9], marker="$test$", label="PData(km)")
#plt.plot([2,3,6,7,10], [1,4,5,8,9], marker="$t$", label="PData(km)")

#그래프 영역 채우기

"""xdata = [2, 3, 6, 7, 10]
ydata = [1, 4, 5, 8, 9]
y1data = [2, 4, 6, 8, 10]

plt.plot(xdata, ydata)
plt.xlabel("x_data")
plt.xlabel("y_data")"""


#새로 축 채우기

#plt.fill_between(xdata[1:4], ydata[1:4], alpha=0.5)
#plt.fill_between(xdata[:4], ydata[:4], alpha=0.5)
#plt.fill_between(xdata[2:4], ydata[2:4], alpha=0.5)
#plt.fill_between(xdata[1:3], ydata[1:3], alpha=0.5)
#plt.fill_between(xdata[1:3], ydata[1:3], alpha=0.3)

#가로 축 채우기
#plt.fill_betweenx(ydata[1:3], xdata[1:3], alpha=0.3)
#plt.fill_betweenx(ydata[:4], xdata[:4], alpha=0.3)
#plt.fill_betweenx(ydata[2:4], xdata[2:4], alpha=0.3)

"""plt.plot(xdata, y1data)
"""

#두 선간의 영역 채우기 

#plt.fill_between(xdata[1:4], ydata[1:4], y1data[1:4], alpha=0.5)
#plt.fill_between(xdata[1:3], ydata[1:3], y1data[1:3], alpha=0.5)
#plt.fill_between(xdata[:4], ydata[:4], y1data[:4],coloer= "C5", alpha=0.5)

#영역 채우기

#plt.fill([2.9, 2.9, 7.1, 7.1], [2.5, 5.0, 8.5, 6.0], alpha=0.5)
#plt.fill([1.9, 1.9, 3.1, 3.1], [0.5, 2.5, 5.5, 3.1], alpha=0.5)




"""dic_val= {"x_data:"[2,3,6,7,10], "y_data"[1,4,5,8,9]} 
dic_val= {"x1_data:"[1,3,5,7,9], "y1_data"[2,4,6,8,10]} 

plt.plot("x_data", "y_data", data=dic_val, ladel ="PData(km)")
plt.plot("x1_data", "y1_data", data=dic_val, ladel ="Value(m)")

"""
#plt.xlabel("x-data")
#plt.xlabel("y-data")



#plt.grid()

#plt.grid(axis="x")
#plt.grid(axis="y")

#plt.grid(axis="y", color="g", alpha=0.5, linestyle="-")
#plt.grid(axis="y", color="g", alpha=0.5, linestyle="--")
#plt.grid(axis="y", color="g", alpha=0.5, linestyle="-.")

#눈금표시

#plt.xticks()
#plt.yticks()

#plt.xticks([0,1,2,3,4,5,6,7,8,9,10])
#plt.yticks([0,1,2,3,4,5,6,7,8,9,10])

#plt.xticks([1,3,5,7,9,11])
#plt.yticks([2,4,6,8,10,12])

#plt.xticks([1,2,3,4,5,6,7,8,9,10], labels=["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"])
#plt.yticks([0,1,2,3,4,5,6,7,8,9,10,11], labels=["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])

#plt.tick_params(axis="x", direction="in")
#plt.tick_params(axis="x", direction="out")
#plt.tick_params(axis="y", direction="in")


#막대그래프 그리기

x_years = ['2020', '2021', '2022']
y_data = [100, 400, 900]
clr = ["r", "lime", "b"]

#plt.bar(x_years, y_data)



#색지정
#plt.bar(x_years, y_data, color="g")
#plt.bar(x_years, y_data, color="C7")
#plt.bar(x_years, y_data, color="#57ADCC")

#개별 색 지정
#plt.bar(x_years, y_data, color=clr)

#너비 설정
#plt.bar(x_years, y_data, color=clr, width=2)
#plt.bar(x_years, y_data, color=clr, width=0.5)
#plt.bar(x_years, y_data, color=clr, width=0.1)

#위치 선정
#plt.bar(x_years, y_data, color=clr, align="edge", width=0.5)
#plt.bar(x_years, y_data, color=clr, align="center", width=0.5)

#테두리
#plt.bar(x_years, y_data, color=clr, align="center", edgecolor="black", width=0.5)
#plt.bar(x_years, y_data, color=clr, align="center", edgecolor="black", linewidth=2, width=0.5)

#축 설정

#plt.yticks([100, 200, 300, 400, 500 , 600, 900])

#수평 그래프 그리기

#plt.barh(x_years, y_data)

#옵션 나열

#plt.barh(x_years, y_data, color=clr, align="center", edgecolor="black", linewidth=3, height=0.3)



#산점도 그래프 그리기


plt.show()
