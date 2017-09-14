from firebase import firebase
import threading

firebase = firebase.FirebaseApplication('https://esp8266-31217.firebaseio.com', None)


class myThread (threading.Thread):
    def __init__(self, name, counter):
        threading.Thread.__init__(self)
        self.name = name
        self.counter = counter
    def run(self):
        firebase.put('data',self.name, self.counter)

# Tao cac thread moi
thread1 = myThread("Thread-1", 1)
thread2 = myThread("Thread-2", 2)

# Bat dau cac thread moi

thread2.start()

print "Ket thuc Main Thread"






