# create a python program that compares execution time of summing numb from 1 to 10 million (10000000) using normal function ,multi-threading and multi-processing using same concepts learned till now

import time
import threading
import multiprocessing

def sum_numbers(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total    

def normal_function():
    start_time = time.time()
    result = sum_numbers(10000000)
    end_time = time.time()
    print(f"Normal Function Result: {result}, Time taken: {end_time - start_time:.4f} seconds")

def thread_function(n, result, index):
    result[index] = sum_numbers(n)

def multi_threading():
    start_time = time.time()
    n = 10000000
    num_threads = 4
    threads = []
    results = [0] * num_threads

    for i in range(num_threads):
        thread = threading.Thread(target=thread_function, args=(n // num_threads, results, i))
        threads.append(thread)
        thread.start()
        for thread in threads:
            thread.join()

    total_result = sum(results)
    end_time = time.time()
    print(f"Multi-threading Result: {total_result}, Time taken: {end_time - start_time:.4f} seconds")

def multi_processing_function(n, result, index):
    result[index] = sum_numbers(n)
def multi_processing():
    start_time = time.time()
    n = 10000000
    num_processes = 4
    processes = []
    manager = multiprocessing.Manager()
    results = manager.list([0] * num_processes)

    for i in range(num_processes):
        process = multiprocessing.Process(target=multi_processing_function, args=(n // num_processes, results, i))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    total_result = sum(results)
    end_time = time.time()
    print(f"Multi-processing Result: {total_result}, Time taken: {end_time - start_time:.4f} seconds")

def main():
    print("Running Normal Function...")
    normal_function()
    
    print("\nRunning Multi-threading...")
    multi_threading()
    
    print("\nRunning Multi-processing...")
    multi_processing()

if __name__ == "__main__":
    main()