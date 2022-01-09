from numba import njit, jit
import numpy as np
import time
import random

def func(input_list):
    output_list = []
    for item in input_list:
        if item % 2 == 0:
            output_list.append(2)
        else:
            output_list.append(1)
    return output_list

@njit
def func1(input_list):
    output_list = np.zeros_like(input_list)
    for ii, item in enumerate(input_list):
        if item % 2 == 0:
            output_list[ii] = 2
        else:
            output_list[ii] = 1
    return output_list

p = time.perf_counter()
func(np.arange(1000))
print(f"Took {time.perf_counter() - p} seconds")

p = time.perf_counter()
func1(np.arange(1000))
print(f"Took {time.perf_counter() - p} seconds")

p = time.perf_counter()
func(np.arange(1000))
print(f"Took {time.perf_counter() - p} seconds")

p = time.perf_counter()
func1(np.arange(1000))
print(f"Took {time.perf_counter() - p} seconds")




'''
def monte_carlo_pi(nsamples):
    acc = 0
    for i in range(nsamples):
        x = random.random()
        y = random.random()
        if (x**2 + y**2) < 1.0:
            acc += 1
    return 4.0 * acc / nsamples

def monte_carlo_pi_jit(nsamples):
    acc = 0
    for i in range(nsamples):
        x = random.random()
        y = random.random()
        if (x**2 + y**2) < 1.0:
            acc += 1
    return 4.0 * acc / nsamples
monte_carlo_pi_jit = jit()(monte_carlo_pi)

s = time.perf_counter()
#func(np.arange(1000))
print(monte_carlo_pi(10000))
print(f"Took {time.perf_counter() - s} seconds")

p = time.perf_counter()
#func1(np.arange(1000))
print(monte_carlo_pi_jit(10000))
print(f"Took {time.perf_counter() - p} seconds")

s = time.perf_counter()
#func(np.arange(1000))
print(monte_carlo_pi(10000))
print(f"Took {time.perf_counter() - s} seconds")

p = time.perf_counter()
#func1(np.arange(1000))
print(monte_carlo_pi_jit(10000))
print(f"Took {time.perf_counter() - p} seconds")
'''