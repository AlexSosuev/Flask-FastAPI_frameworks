# Задание №7
# * Напишите программу на Python, которая будет находить сумму элементов массива из 1000000 целых чисел.
# * Пример массива: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...]
# * Массив должен быть заполнен случайными целыми числами от 1 до 100.
# * При решении задачи нужно использовать многопоточность.
# * В каждом решении нужно вывести время выполнения вычислений.

import random
import time
import threading
import os

def sum_array(arr, result):
    partial_sum = sum(arr)
    result.append(partial_sum)

def multithreaded_sum(arr):
    start_time = time.time()

    result = []
    num_threads = os.cpu_count() 
    threads = []

    for _ in range(num_threads):
        thread = threading.Thread(target=sum_array, args=(arr, result))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return sum(result), time.time() - start_time


if __name__ == '__main__':
    arr = [random.randint(1, 100) for _ in range(1000000)]
    result, lead_time = multithreaded_sum(arr)
    print(f"Многопоточность. Сумма элементов массива: {result}, \nВремя выполнения: {lead_time:.5f} секунд")