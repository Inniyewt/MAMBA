import datetime as dt
import time
import serial
# ser = serial.Serial('COM9',115200)
# print(ser.name)
# data = str(ser.readline())
data = '+RCV=2,50,4005.25,8812.18,194.40,88.48,25.10,98.99'
while data:
    
    # data = str(ser.readline())
    
    data = data[9:]
    dataList = data.split(',')
    dataDict = {}
    dataDict['lat'] = dataList[0]
    dataDict['long'] = dataList[1]
    dataDict['alt'] = dataList[2]
    dataDict['temp'] = dataList[3] 
    dataDict['hum'] = dataList[4]
    dataDict['pres'] = dataList[5]

    
    lat = dataDict['lat']
    lat = str(float(lat[:2]) + float(lat[2:])/60)
    longi = dataDict['long']
    longi = '-' + str(float(longi[:3]) + float(longi[3:])/60)
    GPSurl = 'https://www.google.com/maps/search/?api=1&query=' + lat + ',' + longi
    with open('D:\Documents\School Documents\Comp Lit 2\GPS_Positions.txt', 'a') as outfile:
        outfile.write(dt.time() + ">>>" + lat + "," + longi + "," + data[26:] + '\n')
    print(GPSurl)
    time.sleep(0.2)