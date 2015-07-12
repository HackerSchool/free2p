from http.server import BaseHTTPRequestHandler, HTTPServer
import RPi.GPIO as GPIO

HOST_NAME = ''
PORT_NUMBER = 80

wc_busy = False
def isWCBusy():
	return GPIO.input(17)

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
		if s.path.endswith(("/", ".html", "css", ".js")):
			if s.path == "/":
				s.path = "/index.html"
			s.end_headers()
			s.wfile.write(bytes(open(s.path[1:]).read(), "UTF-8"))


if __name__ == '__main__':
        try:
                GPIO.setmode(GPIO.BCM)
                GPIO.setup(17, GPIO.IN)
                
                httpd = HTTPServer((HOST_NAME, PORT_NUMBER), RequestHandler)

                try:
                        httpd.serve_forever()
                except KeyboardInterrupt:
                        pass
                httpd.server_close()
        finally:
                GPIO.cleanup()
