import threading

def print_message():
    print("This is a thread message.")

t=threading.Thread(target=print_message)

t.start()

t.join()
print("Thread has finished. Main program continue.")