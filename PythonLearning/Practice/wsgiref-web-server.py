from wsgiref.simple_server import make_server

def run_server():
    print('success!')

s = make_server('localhost', 8000, run_server)
s.serve_forever()