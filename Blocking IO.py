import threading
import time 
from  subprocess import Popen, STDOUT, PIPE 
p = Popen(['bc'],stdout=PIPE, stdin=PIPE, shell=True)

while p.poll() is None: # Check if Process is alive 
        print("Tell Something DUde: ...I am blocking The execution :( ") #Blocking IO
        print(p.stdout.readline())
        print("Code is here")
