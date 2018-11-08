from threading import *
import time

class MyClock(Thread):
  def __init__(self, h, m, s):
    Thread.__init__(self)
    self.h = h
    self.m = m
    self.s = s

  def run(self):
    while True:
      for self.h in range(self.h, 12):
        for self.m in range(self.m, 60):
          for self.s in range(self.s, 60):
            print(self.h, ":", self.m, ":", self.s)
            time.sleep(1)
          self.s = 0
        self.m = 0
      self.h = 0

ob = MyClock(1,1,1)
ob.start()
      

    
