ser1 = serial.Serial('COM3', baudrate=9600, timeout=1)  # Adjust COM port
ser2 = serial.Serial('COM4', baudrate=9600, timeout=1)  # Adjust COM port
def read_serial_data(ser):
    line = ser.readline().decode('utf-8').strip()
    return line.split(',')

def obradipodatke():

    # Read data from both Arduinos
    data1 = read_serial_data(ser1)
    data2 = read_serial_data(ser2)
    x1 = data1[0]
    y1 = data1[1]
    z1 = data1[2]
    x2 = data2[0]
    y2 = data2[1]
    z2 = data2[2]
    HIGHV = 2000 #EKSPERIMENATALNO UTVRDITI
    LOWV = -2000
    kontrola1 = ""
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
