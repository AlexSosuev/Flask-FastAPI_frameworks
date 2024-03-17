# Задание №7
# * Напишите программу на Python, которая будет находить сумму элементов массива из 1000000 целых чисел.
# * Пример массива: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...]
# * Массив должен быть заполнен случайными целыми числами от 1 до 100.
# * При решении задачи нужно использовать асинхронность.
# * В каждом решении нужно вывести время выполнения вычислений.

import random
import asyncio
import time

async def calculate_sum(arr):
    return sum(arr)

async def async_sum(arr):
    chunk_size = len(arr) // 4
    chunks = [arr[i * chunk_size: (i + 1) * chunk_size] for i in range(4)]

    start_time = time.time()

    loop = asyncio.get_running_loop()
    tasks = []
    for chunk in chunks:
        task = loop.run_in_executor(None, calculate_sum, chunk)
        tasks.append(task)

    total_sum = 0
    for task in tasks:
        result = await task
        total_sum += await result

    return total_sum, time.time() - start_time

if __name__ == '__main__':

    array = [random.randint(1, 100) for _ in range(1_000_000)]
    total_sum, execution_time = asyncio.run(async_sum(array))

    print(f"Асинхронность. Сумма элементов массива: {total_sum}, \nВремя выполнения: {execution_time:.5f} секунд")
    