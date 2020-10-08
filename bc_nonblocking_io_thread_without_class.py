import threading
import time
from subprocess import Popen, STDOUT, PIPE

p = Popen(['bc', '-i'], stdout=PIPE, stdin=PIPE, stderr=PIPE)

def read_thread(p): #Non Blocking IO
	while p.poll() is None: #To make sure the process is alive.
		print(p.stdout.readline().decode(), end="") #Blocking IO
	
t = threading.Thread(target=read_thread, args=(p,))
t.start()

while p.poll() is None: #To make sure the process is alive.
	query = input()
	if query == 'quit' or query == 'exit':
		p.communicate(query.encode(), timeout=1)
		if p.poll() is not None:
			break
	query = query + '\n'
	p.stdin.write(query.encode())
	p.stdin.flush()

