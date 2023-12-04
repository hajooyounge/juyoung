#선 스타일 설정
import matplotlib.pyplot as plt

plt.plot([2,3,6,7,10], [1,4,5,8,9], "-", label="PData(km)")

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

#plt.show()
