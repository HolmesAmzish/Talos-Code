from wsgiref.simple_server import make_server

def run_server(environment, start_response):
    print('success!', environment)

    start_response("200 OK", [('Content-Type', 'text/html;charset=utf-8')])

    return [bytes('<h2>The page test is successful!</h2>', encoding="utf-8"),]

s = make_server('0.0.0.0', 8001, run_server)
# listening 0.0.0.0, if localhost, only this machine could visit the page

print("Serving on port 8001...")
s.serve_forever()