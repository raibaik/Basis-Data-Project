
from memory_profiler import profile
import time

@profile
def my_func():
            startTime = time.time()

            i = 10

            for i in range (10):
                        print(i+1)
                        i = i + 1

            endTime = time.time()
            print('Duration: {}'.format(endTime - startTime))


if __name__ == '__main__':
            my_func()