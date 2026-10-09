import threading, time

def fungsi_a():
    for i in range(1, 6):
        print(f"Fungsi A - Iterasi {i}")
        time.sleep(0.1)

def fungsi_b():
    for i in range(1, 6):
        print(f"Fungsi B - Iterasi {i}")
        time.sleep(0.1)
        
t1 = threading.Thread(target=fungsi_a)
t2 = threading.Thread(target=fungsi_b)

t1.start(); t1.join()
t2.start(); t2.join()