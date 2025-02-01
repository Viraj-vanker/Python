import threading

def say_hello():
    print("Hello from a thread!")
thread=threading.Thread(target=say_hello)
thread.start()