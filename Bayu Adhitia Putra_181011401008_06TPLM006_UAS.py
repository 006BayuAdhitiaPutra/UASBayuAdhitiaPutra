import CameraClient
import StreaServer
import threading
import time
receiving = StreamingServer('192.168.0.17',9999)
sending = StreamingServer('192.168.0.172',9999)
x= threading.Thread(target = receiving.start_server)
t1.start()
time.sleep(10)
x2 = threading.Thread(target=sending.start_stream)
t2.start()
while input("")!="Stop":
    continue
receiving.stop_server()
senidng.stop_stream() 
