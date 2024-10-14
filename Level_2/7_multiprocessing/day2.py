from multiprocessing import Manager, Process, Lock
from random import random
from time import sleep

def add_to_list(lst: list[str]) -> list[str] :
    lst.append("kk")
    return lst

# work function
def task_with_lock(lock_obj: Lock, identifier: int, value: float):
    # acquire the lock_obj
    with lock_obj:
        print(f'>process {identifier} got the lock, sleeping for {value}')
        sleep(value)


def worker(lock_obj: Lock, shared_resource: list[int], pid: int):
    # Time delay to imitate work and make order more observable
    # random float value
    sleep(1 + random()*2)

    # Acquire and release the lock_obj using with statement
    with lock_obj:
        shared_resource.append(pid)

if __name__ == "__main__":
    print(f"invoking_with_empty_list={add_to_list([])}")
    manager = Manager()
    shared_list = manager.list()
    lock = manager.Lock()
    # List to keep track of processes
    processes = []

    # Number of processes you want to spawn
    num_processes = 5

    # Create and start processes, passing the process index
    for i in range(num_processes):
        process_id = i + 1  # Process ID starts at 1
        print(f"process_id={process_id}")
        process = Process(target=worker, args=(lock, shared_list, process_id))
        process.start()
        processes.append(process)

    # Ensure all processes finish execution
    for process in processes:
        process.join()

    print("All processes have finished their execution.")
    print("Shared list content:", list(shared_list))