import threading, time

def fungsi_a():
    print("Fungsi A Statement 1")
    time.sleep(1)
    print("Fungsi A Statement 2")
    time.sleep(1)
    print("Fungsi A Statement 3")
    time.sleep(1)
    print("Fungsi A Statement 4")
    time.sleep(1)
    print("Fungsi A Statement 5")
    time.sleep(1)
    print("Fungsi A Statement 6")
    
def fungsi_b():
    print("Fungsi B Statement 1")
    time.sleep(1)
    print("Fungsi B Statement 2")
    time.sleep(1)
    print("Fungsi B Statement 3")
    time.sleep(1)
    print("Fungsi B Statement 4")
    time.sleep(1)
    print("Fungsi B Statement 5")
    time.sleep(1)
    print("Fungsi B Statement 6")
    

print("\n tanpa multi threading")
fungsi_a()
fungsi_b()

print("\n \n  dengan multi threading")
t1 = threading.Thread(target=fungsi_a)
t2 = threading.Thread(target=fungsi_b)

t1.start(); t2.start()
t1.join(); t2.join()