# SuperFastPython.com
# example of running a function in another process
from multiprocessing import (
    Process, Lock
)
from random import random
from time import sleep


# a custom function that blocks for a moment
def task():
    # block for a moment
    sleep(1)
    # display a message
    print('This is from another process')

def task_with_args(name: str):
    # block for a moment
    sleep(1)
    # display a message
    print(f'Hello, {name}! This is from another process')


# custom process class with args
class CustomProcess(Process):

    def __init__(self, name: str = 'CustomProcess'):
        # call the parent constructor, order is important
        super().__init__()
        self.name = name # name will be different if the order is changed

    # override the run function
    def run(self):
        # block for a moment
        sleep(1)
        # display a message
        print(f'Hello, {self.name}! This is from Custom process')

# entry point
if __name__ == '__main__':
    # create a process
    process = Process(target=task)
    # run the process
    process.start()

    # create a process with arguments
    process2 = Process(target=task_with_args, args=('John',))
    # run the process
    process2.start()

    # wait for the process to finish
    print('Waiting for the process 1 & 2')
    process.join()
    process2.join()

    # create the process
    process = CustomProcess(name = 'John')
    # start the process
    process.start()
    process.join()
