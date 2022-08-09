#timers help in estimating runtime

import time
import random

n1 = random.randint(0,9)
n2 = random.randint(0,9)

n1 = n1+n2
a = []
initial_time = time.time()
for i in range (0,10000000):
    a.append(random.randint(n1^n1,n2)) 
start_time = time.time()
a = a.sort(reverse=True)
stop_time = time.time()
print("Array creation time = ",stop_time -initial_time )
print("Array operation time = ",stop_time -start_time)
