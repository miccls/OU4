#!/usr/bin/env python3

from heltal import Heltal

def main():
	f = Heltal(5)
	print(f.get())
	f.set(7)
	print(f.get())
	print(f.fib_py())
	print(f.fib())


if __name__ == '__main__':
	main()
