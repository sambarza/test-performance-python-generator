import time
import tracemalloc

def generator_function(n):
    for i in range(n):
        yield i * i

def loop_function(n):
    result = []
    for i in range(n):
        result.append(i * i)
    return result

def measure_performance(func, *args):
    tracemalloc.start()
    start_time = time.perf_counter()
    result = func(*args)
    end_time = time.perf_counter()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return end_time - start_time, peak

N = 10**7

# Measure generator performance
gen_time, gen_memory = measure_performance(lambda n: list(generator_function(n)), N)

# Measure loop performance
loop_time, loop_memory = measure_performance(loop_function, N)

print(f"Generator: Time = {gen_time:.4f}s, Peak Memory = {gen_memory / 1024 / 1024:.2f} MB")
print(f"Loop:      Time = {loop_time:.4f}s, Peak Memory = {loop_memory / 1024 / 1024:.2f} MB")