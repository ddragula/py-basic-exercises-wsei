import numpy as np
import time
from math import cos, log
from multiprocessing import Pool
import functools


def measure_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        eval_time = time.time() - start_time
        print(f"Funkcja '{func.__name__}' wykonała się w czasie: {eval_time:.2f} sekundy")
        return result
    return wrapper


def f(x):
    return cos(x) + (log(x + 1))**2


def calculate_chunk(chunk):
    return [f(x) for x in chunk]


@measure_time
def calc_with_multiprocessing(x_values, processes=4):
    chunks = np.array_split(x_values, processes)

    with Pool(processes) as pool:
        results = pool.map(calculate_chunk, chunks)

    all_results = np.concatenate(results)

    return all_results


@measure_time
def calc_without_multiprocessing(x_values):
    return calculate_chunk(x_values)


def main():
    x_values = np.arange(1, 1e6, 0.01)

    print("Obliczenia z użyciem multiprocessingu...")
    calc_with_multiprocessing(x_values)

    print("Obliczenia bez użycia multiprocessingu...")
    calc_without_multiprocessing(x_values)


if __name__ == "__main__":
    main()
