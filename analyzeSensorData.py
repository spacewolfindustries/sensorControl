import sys
import os
import matplotlib.pyplot as plt

baseFileName = sys.argv[0].split(".")[0]
outFileName = baseFileName + "_humidityPlot.pdf"


figureTitle = "Sensor Data " + os.getcwd().split('_')[0].split('/')[-1]
fig, ax = plt.subplots()
ax.title.set_text(figureTitle)


print(sys.argv[0])
for n in sys.argv[1:]:
    dataLabel = n.split('_')[-1].split('.')[0]
    with open(n) as f:

        timeArray = []
        humidityArray = []

        for line in f:
            line = line.replace("]", '')
            line = line.replace("[", '')
            line = line.replace("'", '')
            dataArray = line.split(',')

            time = float(dataArray[0])/1000
            humidity = float(dataArray[1])

            timeArray.append(time)
            humidityArray.append(humidity)

        print(dataLabel)
        ax.plot(timeArray, humidityArray, label=dataLabel)


baseFileName = sys.argv[0].split(".")[0]
outFileName = baseFileName + "_humidityPlot.pdf"
plt.legend(bbox_to_anchor=(1.0, 1.0), loc=1)
print(outFileName)
fig.savefig(outFileName)
