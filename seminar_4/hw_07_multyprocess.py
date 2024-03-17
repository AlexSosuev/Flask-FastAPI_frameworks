# Задание №7
# * Напишите программу на Python, которая будет находить сумму элементов массива из 1000000 целых чисел.
# * Пример массива: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...]
# * Массив должен быть заполнен случайными целыми числами от 1 до 100.
# * При решении задачи нужно использовать многопроцессорность.
# * В каждом решении нужно вывести время выполнения вычислений.

import random
import multiprocessing
import time

def calculate_and_queue(arr, results):
    result = sum(arr)
    results.put(result)

def multiprocess_sum(arr):
    chunk_size = len(arr) // multiprocessing.cpu_count()
    chunks = [arr[i * chunk_size: (i + 1) * chunk_size] for i in range(multiprocessing.cpu_count())]
    processes = []

    start_time = time.time()

    results = multiprocessing.Queue()

    for chunk in chunks:
        process = multiprocessing.Process(target=calculate_and_queue, args=(chunk, results))
        process.start()
        processes.append(process)
    
    for process in processes:
        process.join()

    total_sum = 0
    while not results.empty():
        total_sum += results.get()

    return total_sum, time.time() - start_time

if __name__ == '__main__':
    array = [random.randint(1, 100) for _ in range(1_000_000)]

    total_sum, execution_time = multiprocess_sum(array)
    print(f"Многопроцессорность. Сумма элементов массива: {total_sum}, \nВремя выполнения: {execution_time:.5f} секунд")
  