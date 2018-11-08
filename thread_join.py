from threading import *
import time

class myThread(Thread):
  def __init__(self, threadID, name, counter):
    Thread.__init__(self)
    self.threadID = threadID
    self.name = name
    self.counter = counter

  def run(self):
    print("Starting " + self.name)
    print_time(self.name, 1, 5)
    print("Exiting " + self.name)


def print_time(threadName, delay, counter):
  while counter:
    time.sleep(delay)
    print("%s: %s" % (threadName, time.ctime(time.time())))
    counter -= 1


#create new threads
thread1 = myThread(1, "Thread 1", 5)
thread2 = myThread(2, "Thread 2", 5)

#Start new Threads
thread2.start()
thread2.join()
print("Join is working")

thread1.start()
thread1.join()
print("Joimn is working")

print("Exiting main thread")
