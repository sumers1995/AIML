import time
from multiprocessing import Process
from threading import Thread

def task(no):
    print(f"Starting task {no}")
    for i in range(10**8):
        result = 1
    print(f"Completed taks {no}")
    return

if __name__ == "__main__":
    start = time.perf_counter()
    threads = [Thread(target=task, args=[i]) for i in range(100)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    finish = time.perf_counter()
    print(f"Threading took {finish-start:.2f} seconds")

    start = time.perf_counter()
    processes = [Process(target=task, args=[i]) for i in range(10)]
    for p in processes:
        p.start()
    for p in processes:
        p.join()

    finish = time.perf_counter()
    print(f"Multiprocessing took {finish-start:.2f} seconds")
