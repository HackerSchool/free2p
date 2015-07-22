from socketserver import ThreadingMixIn
from http.server import BaseHTTPRequestHandler, HTTPServer
import threading
import RPi.GPIO as GPIO
from os import path

HOST_NAME = ''
PORT_NUMBER = 8080
PATH = path.dirname(path.abspath(__file__)) + "/"

def sensorEvent(channel):
	global wc_busy 
	wc_busy = GPIO.input(17)	

def isWCBusy():
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

		if s.path.endswith(("/", ".html", "css", ".js", ".png")):
			if s.path == "/":
				s.path = "/index.html"
			elif s.path.endswith((".png", ".js")):
				s.send_header("Cache-Control", "max-age=86400, must-revalidate")
			s.end_headers()
			f = open(PATH + s.path[1:], 'rb')
			s.wfile.write(f.read())
			f.close()

class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
	pass

if __name__ == '__main__':
        global wc_busy
        try:
                GPIO.setmode(GPIO.BCM)
                GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)             
                GPIO.add_event_detect(17, GPIO.BOTH, callback=sensorEvent)
                wc_busy = GPIO.input(17)
                
                httpd = ThreadedHTTPServer((HOST_NAME, PORT_NUMBER), RequestHandler)

                try:
                        httpd.serve_forever()
                except KeyboardInterrupt:
                        pass
                httpd.server_close()
        finally:
                GPIO.cleanup()
