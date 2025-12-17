import time
import multiprocessing

def task(no) -> int:
    print(f"Performing task {no}")
    result = 0
    for i in range(10**10):
        result += i
    print(f"Finished task {no}")
    return result

if __name__ == "__main__":
    start = time.perf_counter()

    # for i in range(10):
    #     task(i)

    processes = [multiprocessing.Process(target=task, args=[i]) for i in range(4)]

    for process in processes:
        process.start()

    for process in processes:
        process.join()

    finish = time.perf_counter()
    print(f"Time taken: {finish-start:.2f} seconds")