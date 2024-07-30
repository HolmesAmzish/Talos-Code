from wsgiref.simple_server import make_server

def book(environ, start_response):
    print("book page")
    start_response("200 OK", [('Content-Type', 'text/html;charset=utf-8')])
    return [bytes('<h2>Book page</h2>', encoding="utf-8")]

def clothes(environ, start_response):
    print("clothes page")
    start_response("200 OK", [('Content-Type', 'text/html;charset=utf-8')])
    return [bytes('<h2>Clothes page</h2>', encoding="utf-8")]

def url_dispatcher():
    urls = {
        '/book': book,
        '/clothes': clothes,
    }
    return urls

def run_server(environ, start_response):
    print('success', environ)

    urls_list = url_dispatcher()  # get all urls
    request_url = environ.get("PATH_INFO")
    print('request url', request_url)

    if request_url in urls_list:
        func = urls_list[request_url]
        return func(environ, start_response)
    else:
        start_response("404 Not Found", [('Content-Type', 'text/html;charset=utf-8')])
        return [bytes('<center><h2>Page not found</h2></center>', encoding="utf-8")]

s = make_server('0.0.0.0', 8000, run_server)
print("Serving on port 8000...")
s.serve_forever()
