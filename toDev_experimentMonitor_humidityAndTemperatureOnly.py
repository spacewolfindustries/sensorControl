# import necessary packages
import serial
import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
from drawnow import *

style.use("dark_background")

timeArray = []
humidityArray = []
temperatureArray = []
# wArray = []
# xArray = []
# yArray = []
# zArray = []

"""humidity and temp"""


def add(x, y):
    return x + y


def makeFigure():
    plt.title("Live Sensor Data")
    plt.plot(timeArray, temperatureArray, 'r-')
    plt.plot(timeArray, humidityArray, 'b-')

    # ax1 = fig.add_subplot(211)
    # ax1.plot(timeArray, temperatureArray)
    # ax2 = fig.add_subplot(212)
    # ax2.plot(timeArray, humidityArray)


def writeData(fileName, dataArray):
    myFile = open(fileName, "a")
    myFile.write(str(dataArray))
    myFile.write('\n')
    myFile.close()


PATH_OUT = "/Users/spacewolf/Desktop/humidityData.txt"
DATA_FILE = open(PATH_OUT, 'w').close()


arduinoSerialData = serial.Serial('/dev/cu.usbmodem1421', 9600)
plt.ion()


while(True):

    if(arduinoSerialData.inWaiting() > 0):

        arduinoData = arduinoSerialData.readline().decode().strip()
        dataArray = arduinoData.split(',')
        if(len(dataArray) == 3):
            writeData(PATH_OUT, dataArray)

            time = float(dataArray[0]) / 1000
            humidity = float(dataArray[1])
            temperature = float(dataArray[2])
            # w = float(dataArray[3])
            # x = float(dataArray[4])
            # y = float(dataArray[5])
            # z = float(dataArray[6])

            timeArray.append(time)
            humidityArray.append(humidity)
            temperatureArray.append(temperature)
            # wArray.append(w)
            # xArray.append(x)
            # yArray.append(y)
            # zArray.append(z)

            drawnow(makeFigure)
            plt.pause(0.000001)

print('hello')
