import serial


arduinoData = serial.Serial('/dev/ttyACM0',9600)

count = 0
flag = 1
zerocount = 0
prev = 0

while (flag == 1) :
    while (arduinoData.inWaiting() == 0) :
        pass
    f = open('datavalue1.txt','ab')
    Data = arduinoData.readline()
    datarow = Data.split(",")
    count = count+1
    Data1 = float(datarow[0])
    if (prev != 0) and (Data1 == 0.00):
        zerocount = zerocount+1
    
    if count >5:
        
        f.write(Data)
        print(Data)
        f.close()
        #print("closed")
        prev = Data1 +prev
    if zerocount == 5
        flag = 0




    
