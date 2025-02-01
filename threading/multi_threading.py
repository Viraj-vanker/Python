import threading

def print_even():
    for i in range(0,10,2):
        print(f"even:{i}")
def print_odd():
    for i in range(1,10,2):
        print(f"odd:{i}")
t1=threading.Thread(target=print_even)
t2=threading.Thread(target=print_odd)

t1.start()
t1.join()
t2.start()