import serial

ser1 = serial.Serial('COM3', baudrate=9600, timeout=1)  # Adjust COM port for Arduino 1
ser2 = serial.Serial('COM4', baudrate=9600, timeout=1)  # Adjust COM port for Arduino 2

def obradipodatke():
    line1 = ser1.readline().decode('utf-8').strip()
    line2 = ser2.readline().decode('utf-8').strip()

    try:
        parts1 = line1.split()
        x1 = int(parts1[1])
        y1 = int(parts1[3])
        z1 = int(parts1[5])
        print(f"Gyro1: X={x1} Y={y1} Z={z1}")
    except:
        print("Gyro1: No valid data")

    try:
        parts2 = line2.split()
        x2 = int(parts2[1])
        y2 = int(parts2[3])
        z2 = int(parts2[5])
        print(f"Gyro2: X={x2} Y={y2} Z={z2}")
    except:
        print("Gyro2: No valid data")
    
    HIGHV = 2000 #EKSPERIMENATALNO UTVRDITI
    LOWV = -2000
    kontrola1 = ""
    kontrola2 = ""
    if(x1 > HIGHV):
        kontrola1 = "gore"
    if(x1 < LOWV):
        kontrola1 = "dole"
    if(y1 > HIGHV):
        kontrola1 = "levo"
    if(y1 < LOWV):
        kontrola1 = "desno"
    if(x2 > HIGHV):
        kontrola2 = "gore"
    if(x2 < LOWV):
        kontrola2 = "dole"
    if(y2 > HIGHV):
        kontrola2 = "levo"
    if(y2 < LOWV):
        kontrola2 = "desno"
    return kontrola1, kontrola2
