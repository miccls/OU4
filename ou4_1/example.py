# Parallel programming and multithreading.

from time import perf_counter as pc
from time import sleep
import concurrent.futures as future

def runner(k):
    sleep(1)
    print("Walla")



if __name__ == "__main__":
    start= pc()
    with future.ProcessPoolExecutor() as ex:
        p = [5, 4, 3, 2, 1, 3, 4, 5, 6, 8,8]
        results= ex.map(runner, p)
        for r in results:
            print(r)
    end= pc()
    print(f"Process took{round(end-start,2)}seconds")