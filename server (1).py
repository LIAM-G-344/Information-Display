#----- A simple TCP based server program in Python using send() function -----
from signal import signal, SIGTERM, SIGHUP, pause
from rpi_lcd import LCD
import socket
import time
from datetime import date

lcd = LCD()
rpt = ("1")
# operating on IPv4 addressing scheme
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
#bind and listen
serverSocket.bind(("0.0.0.0",9090));
serverSocket.listen();
while rpt == '1':
    try:
        print("attemting to get reception")

        serverSocket.settimeout(3)
        (clientConnected, clientAddress) = serverSocket.accept();
        print("Accepted a connection request from %s:%s"%(clientAddress[0], clientAddress[1]));

        #data2FromClient = clientConnected.recv(1024)
        dataFromClient = clientConnected.recv(1024)
        data_1 = (dataFromClient.decode())
        #data_2 = (data2FromClient.decode())
        #print(data_2)
        lcd.text(data_1, 1)

        serverSocket.settimeout(3)
        (clientConnected, clientAddress) = serverSocket.accept();
        print("Accepted a connection request from %s:%s"%(clientAddress[0], clientAddress[1]));
        dataFromClient = clientConnected.recv(1024)
        data_2 = (dataFromClient.decode())
        lcd.text(data_2, 2)
        
    except socket.timeout:
        import time
        from datetime import date

        today = date.today()
        now = time.localtime()
        time = time.strftime("%H:%M EST",now)
        d4 = today.strftime("%b-%d-%Y")
        lcd.text(time,1)
        lcd.text(d4,2)


