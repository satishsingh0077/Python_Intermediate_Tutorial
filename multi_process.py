# running multiple process 
from multiprocessing import Process
import os
import time

def square(n): #just creating a random program for demostration
    for i in range (n):
        print(i)
        i*i
        time.sleep(0.1)

# create a process.
# a process will take the argument as a function that it needs to run along with arguments
if __name__ == "__main__":
    # GET THE COUNT OF CPU CORES IN THE MACHINE
    cores = os.cpu_count()
    # creating a list to store all the processes that will be created
    processes = []

    for i in range(cores):
        p = Process(target=square,args=(10,)) # passing 100 as argument to square function in the form of a tuple
        processes.append(p)

    #statrting all the processes
    for proc in processes:
        proc.start()

    # join process: this means halt executuion untill all processes are done.
    for proc in processes:
        proc.join()

    # Do something when all process ends
    print("All processes are done")