""" Python interface to the C++ Integer class """
import ctypes
lib = ctypes.cdll.LoadLibrary('./libheltal.so')

class Heltal(object):
	def __init__(self, val):
		lib.Heltal_new.argtypes = [ctypes.c_int]
		lib.Heltal_new.restype = ctypes.c_void_p
		lib.Heltal_get.argtypes = [ctypes.c_void_p]
		lib.Heltal_get.restype = ctypes.c_int
		lib.Heltal_set.argtypes = [ctypes.c_void_p,ctypes.c_int]
		lib.Heltal_delete.argtypes = [ctypes.c_void_p]
		self.obj = lib.Heltal_new(val)

	def _fib_py(self, n):
		if n <= 1:
			return n
		else: 
			return self._fib_py(n - 1) + self._fib_py(n - 2)

	def fib_py(self):
		return self._fib_py(lib.Heltal_get(self.obj))

	def fib(self):
		return lib.Heltal_fib(self.obj)

	def get(self):
		return lib.Heltal_get(self.obj)

	def set(self, val):
		lib.Heltal_set(self.obj, val)
        
	def __del__(self):
		return lib.Heltal_delete(self.obj)
