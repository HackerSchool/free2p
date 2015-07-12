from http.server import BaseHTTPRequestHandler, HTTPServer

HOST_NAME = ''
PORT_NUMBER = 80

wc_busy = False
def isWCBusy():
	global wc_busy

	wc_busy = not wc_busy
	return wc_busy

class RequestHandler(BaseHTTPRequestHandler):
	def do_HEAD(s):
		print("HEAD")
		pass

	def do_GET(s):
		"""Respond to a GET request"""
		s.send_response(200)
		if s.path == "/occupation":
			s.send_header("Content-type", "text/plain")
			s.end_headers()
			if isWCBusy() == True:
				s.wfile.write(bytes("busy", "UTF-8"))
			else:
				s.wfile.write(bytes("free", "UTF-8"))

		#if s.path == "/":
		if s.path.endswith(("/", ".html", ".js")):
			s.end_headers()
			s.wfile.write(bytes(open(s.path[1:]).read(), "UTF-8"))


if __name__ == '__main__':
	httpd = HTTPServer((HOST_NAME, PORT_NUMBER), RequestHandler)

	try:
		httpd.serve_forever()
	except KeyboardInterrupt:
		pass
	httpd.server_close()
