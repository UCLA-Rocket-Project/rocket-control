import serialHandler
import TCPServer


serialPorts = serialHandler.RIGHT_PORTS

print('''
          ___      .______       _______     _______.     ______  _______   __    __  
         /   \     |   _  \     |   ____|   /       |    /      ||       \ |  |  |  | 
        /  ^  \    |  |_)  |    |  |__     |   (----`   |  ,----'|  .--.  ||  |__|  | 
       /  /_\  \   |      /     |   __|     \   \       |  |     |  |  |  ||   __   | 
      /  _____  \  |  |\  \----.|  |____.----)   |      |  `----.|  '--'  ||  |  |  | 
     /__/     \__\ | _| `._____||_______|_______/        \______||_______/ |__|  |__| 
''')
print("\n")

for port in serialPorts:
    result = serialHandler.getHandler().connect(port, timeout=0, wait=2)
    if result:
        print("main *> Successfully connected to device at port {}".format(port))
    else:
        print("main *> Error connecting to device at port {}".format(port))


serverThread = TCPServer.getServerThread('0.0.0.0', 9999)
serverThread.daemon = True


try:
    serverThread.start()
    print("main *> Started server")
    print("\n")
    serverThread.join()
except:
    print("\n\n")
    print("main *> Stopped server")
    print("main *> EXITING CDH")

