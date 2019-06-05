import time
import winsound

def my_timer(sec):
    for i in range(sec):
        print(sec-i,end=" \r")
        time.sleep(1)
    print('time up! \r')
    winsound.Beep(1200,400)
    winsound.Beep(800,200)
    winsound.Beep(800,200)
    winsound.Beep(1600,1000)
    
def sport_record():
    a = [bool(int(i)) for i in bin(11138134124)[2:]][0:30]
    b = [bool(int(i)) for i in bin(331242803114)[2:]][0:30]
    c = [bool(int(i)) for i in bin(12435240231)[2:]][0:30]
    d = [bool(int(i)) for i in bin(95466114871)[2:]][0:30]
    e = [bool(int(i)) for i in bin(98765432103)[2:]][0:30]
    return a,b,c,d,e