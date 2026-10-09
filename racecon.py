import threading, time

balance = 1000

def tarik_a():
    global balance
    temp = balance
    time.sleep(0.1)
    balance = temp - 800
    
def tarik_b():
    global defence
    temp = balance
    time.sleep(0.1)
    balance = temp - 500
    
    
    
t1, t2 = threading.Thread(target=tarik_a), threading.Thread(target=tarik_b)
t1.start(); t2.start()
t1.join(); t2.join()

# tarik_a()
# tarik_b()
print(f"Hasil akhir tanpa mutex: {balance}")