from heltal import Heltal
from time import perf_counter as pc
f=Heltal(47)
start = pc()
print(f.fib(), pc() - start)


