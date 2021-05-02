#!/usr/bin/env python3

from heltal import Heltal
from time import perf_counter as pc
from matplotlib import pyplot as plt
# For the splitting over two cores
import concurrent.futures as future

def time_fibb(method, rng):
	lst = []
	f = Heltal(rng[0])
	for n in rng:
		start = pc()
		method(f)
		lst.append(pc() - start)
		f.set(n + 1)
	return lst

def main():
	# Time comparison for C++ and Python
	f = Heltal(30)
	# Dictionary to keep track of data.
	rng = [i for i in range(30, 45)]

	with future.ProcessPoolExecutor() as ex:
		p1 = ex.submit(time_fibb, Heltal.fib, rng)
		p2 = ex.submit(time_fibb, Heltal.fib_py, rng)
		cpp_time = p1.result()
		python_time = p2.result()


	fig, ax = plt.subplots()
	ax.plot(rng, cpp_time, color = 'green', label = "C++")
	ax.plot(rng, python_time, color = 'blue', label = "Python")
	ax.legend()
	plt.show()
	plt.savefig("fib_plt.png")



if __name__ == '__main__':
	main()
