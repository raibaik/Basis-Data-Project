#Pengulangan while
from memory_profiler import profile
import time

@profile
def my_func():
            startTime = time.time()

            i = 1

            while i <= 10:
                        print(i)
                        i = i + 1

            endTime = time.time()
            print('Duration: {}'.format(endTime - startTime))


if __name__ == '__main__':
            my_func()