from socketIO_client import SocketIO, LoggingNamespace
import tty
import sys
import termios
import json
import time


orig_settings = termios.tcgetattr(sys.stdin)

tty.setraw(sys.stdin)


with SocketIO('https://inclusive-inputs.herokuapp.com', 443, LoggingNamespace, verify=False) as socketIO:
	x=0
	while x != chr(27):
		x=sys.stdin.read(1)[0]
		print("You pressed", x)
		payload = {
			'type': 'keypress',
			'value': ord(x),
			'clientid': 'makey',
			'timestamp': time.time()
		}
		socketIO.emit('keypress', payload)
		print 'emitted'
		socketIO.wait(seconds=1)
		print 'done waiting'

termios.tcsetattr(sys.stdin, termios.TCSADRAIN, orig_settings)
