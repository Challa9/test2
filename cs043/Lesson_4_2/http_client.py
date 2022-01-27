import socket
import wsgiref.simple_server

"""
request = 'GET /CScourses/03b1_minimal.html HTTP/1.1\r\nHost: indstudy1.org\r\n\r\n'
sock = socket.create_connection(('50.87.178.13', 80))
sock.sendall(request.encode(encoding='utf-8'))
data = sock.recv(1000)
sock.close()
print(data.decode(encoding='utf-8'))

print("request: ", request)"""


# make a request
def http_get(host, page):
    sock = socket.create_connection((host, 80))
    sock.sendall(('GET ' + page + ' HTTP/1.1\r\nHost: ' + host + '\r\n\r\n').encode())
    print(sock.recv(1000).decode())
    sock.close()


def application(environ, start_response):
    headers = [('Content-Type', 'text/plain; charset=utf-8')]
    start_response('200 OK', headers)
    return ['Hello World!'.encode()]


httpd = wsgiref.simple_server.make_server('', 8000, application)
httpd.serve_forever()
