import time
import random
import threading
import queue
Nombrefilosofos = ['Anaximenes','Heráclito','Democrito','Pitágoras','Sócrates']  #Nombre de los filosofos griegos
queue = queue.Queue(maxsize=len(Nombrefilosofos))  #Establece el límite superior del número de elementos que pueden ser colocados en la cola
Ycom = [] #Para saber si filosofo ya fue elejido

class filosofo():
    def apetito():  
        for j in range(len(Nombrefilosofos)):  #se repetira la cantidad de filosofos
            bandera = True 
            while bandera:  #Mientras se repita el random seguira ejecutandose
                item = random.randint(0,len(Nombrefilosofos)-1) #se genera el random para obtener el nuevo valor posible
                if not item in Ycom:       #Para saber si el filosofo no existe en las posiciones de los que que ya comieron
                    Ycom.append(item)      #Si el filoso no existe en la lsita de los que ya comieron se agrega
                    bandera = False                    #Para que termine el ciclo while y comienze de nuevo hasta obtener todos los valores
            queue.put(item)                         #inserta el filosofo a la cola

    def comer():
        for i in range(len(Nombrefilosofos)):   #Para que termine hasta que el contador sea menor a la cantidad que hay de filosofos
            item = queue.get()                  #Se obtiene el dato del filosofo que esta en cola
            time.sleep(random.randint(2,3))  #Tiempo en espera antes de comer
            print("Filosofo",Nombrefilosofos[item], " esta comiendo \n")  
            time.sleep(random.randint(3,4))  #Tiempo en espera para despues terminar de comer
            print("Filosofo ", Nombrefilosofos[item]," termino de comer\n")
            queue.task_done()   #avisa que la tarea a finalizado

if __name__ == "__main__":
    filosofo()
    threading_filosofo = threading.Thread(target=filosofo.apetito)
    threading_comer = threading.Thread(target=filosofo.comer)
    threading_filosofo.start()
    threading_comer.start()