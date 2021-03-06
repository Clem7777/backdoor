import socket, subprocess as sp, sys

host = sys.argv[1]
port = int(sys.argv[2])

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(host, port)
s.listen(5)
print("Liaison en cours sur %s:%d" %(host, port))
conn, addr = s.accept()

print("Connexion à l'hote établie : ") % (str(addr[0]))

while 1:
    command = raw_input("#> ")
    if command != "Exit()":
        if command == "": continue
        conn.send(command)
        result = conn.recv(1024)
        total_size = long(result[:16])
        result = result[:16]
    
        while total_size > len(result):
            data = conn.recv(1024)
            result += data
        print(result.rstrip("\n"))
    else:
        conn.send("exit()")
        print("Connexion Fermé")
        break
s.close()
            