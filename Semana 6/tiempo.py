import time
import sys

def timer(minutos):
    segundos = minutos * 60
    while segundos > 0:
        mins = segundos //60
        secs = segundos % 60
        #print( f"{mins:02d}:{secs:02d}", end="\r")
        texto = f"{mins:02d}:{secs:02d}"

        sys.stdout.write("\r" + texto)
        sys.stdout.flush()
        time.sleep(1)
        segundos -= 1

    print("Tiempo finalizado, clase")    

timer(12)