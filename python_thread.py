import time
from threading import *

# thread always go in run method by default when initialised


class Demo(Thread):
  def __init__(self):
    print("Thread started")
    Thread.__init__(self) #Thread firing its constructor

  def run(self):
    for x in range(1,11):
      print(x)
      time.sleep(1)


ob = Demo()
ob.start() #starting thread


