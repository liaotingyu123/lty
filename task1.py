
import matplotlib.pyplot as plt
import csv
import numpy
import math

with open('FlightPath.csv',encoding='utf-8') as f:
    with open('LIDARPoints.csv', encoding='utf-8-sig') as fp:
        # 创建阅读器（调用csv.reader()将前面存储的文件对象最为实参传给它）
        reader = csv.reader(f)
        # 调用了next()
        # 一次，所以这边只调用了文件的第一行，并将头文件存储在header中
        header = next(reader)
        reader1 = csv.reader(fp)
        next(reader1)
        # 存飞机路径第一列数据
        row1 = []
        # 存飞机路径第二列数据
        row2 = []
        #存放经过处理的数据
        x1 = []
        y1 = []

        k =0
        #
        for i in reader:
            if(k%2==0):
                r1 = float(i[0]) * 1000
                row1.append(r1)
                r2 = float(i[1]) * 1000
                row2.append(r2)
            #墙
            #将数据以列读出，分别放在列表 angle、distance中
                for j in reader1:
                    if(j[1]=='533'):
                        break
                    if(j[1]=='534'):
                        break
                    angle = float(j[0])
                    distance = float(j[1])
                    #sin cos的参数值是弧度
                    #将极坐标数据转化为直角坐标系下表示的数据，并将得到的数据存放在列表x1和y1中
                    x = r1+numpy.cos(angle/180*math.pi)*distance
                    x1.append(x)
                    y = r2-numpy.sin(angle/180*math.pi)*distance
                    y1.append(y)
                #指向性
            k=k+1

    #绘图

    fig = plt.figure(dpi=128, figsize=(10, 6))
    plt.plot(row1, row2, c='blue', linestyle='-', marker='.')
    plt.scatter(x1, y1, c='red',linestyle='none',maker='.')
    plt.title("Flight",fontsize=12)
    plt.show()
