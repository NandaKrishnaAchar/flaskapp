from flask import Flask
import socket

app = Flask(__name__)

import socket
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
print("Your Computer Name is:" + hostname)
print("Your Computer IP Address is:" + IPAddr)

@app.route('/')
def hello_world():
  hn=socket.gethostname()
  ip=socket.gethostbyname(hn)
  return 'Hello from Flask22!'+ip


if __name__ == '__main__':
  app.run()
