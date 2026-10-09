import threading, time

balance = 1000
lock = threading.Lock()

def tarik(nama, jumlah):
    global balance
    
    lock.acquire() #ENTRY SECTION (kunci pintu)
    
    #CRITICAL SECTION START
    temp = balance
    time.sleep(0.1)
    if temp >= jumlah:
        balance = temp - jumlah
        print(f"[{nama}] Berhasil tarik {jumlah}. Sisa: {balance}")
    else:
        print(f"[{nama}] Gagal! Saldo tidak cukup ({balance})")
    #CRITICAL SECTION END
    
    lock.release() #EXIT SECTION (Buka kunci)
    
t1 = threading.Thread(target=tarik, args=("TarikA", 800)) 
t2 = threading.Thread(target=tarik, args=("TarikB", 500))
t1.start(); t2.start()
t1.join(); t2.join()

print(f"\nHasil akhir dengan mutex: {balance}")