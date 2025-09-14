import time
import tracemalloc
import random
import json

# Generate sample data: list of items with 'price'

# Generator function to yield prices
def price_generator(items):
    return (item['price'] for item in items)

# Function to calculate total using generator
def total_with_generator(items):
    return sum(price_generator(items))

# Function to calculate total using loop
def total_with_loop(items):
    total = 0
    for item in items:
        total += item['price']
    return total

# Measure time and memory usage
def measure_performance(func, items):
    tracemalloc.start()
    start_time = time.perf_counter()
    result = func(items)
    end_time = time.perf_counter()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return {
        'result': result,
        'time': end_time - start_time,
        'memory_peak': peak / 1024  # in KB
    }

if __name__ == "__main__":

    with open("items.json", "r") as f:
        items = json.load(f)
    print(f"Loaded {len(items):,}".replace(",", ".") + " items from items.json")

    gen_perf = measure_performance(total_with_generator, items)
    loop_perf = measure_performance(total_with_loop, items)

    print(f"Generator - Total: {gen_perf['result']:.2f}, Time: {gen_perf['time']:.6f}s, Peak Memory: {gen_perf['memory_peak']:.2f}KB")
    print(f"Loop      - Total: {loop_perf['result']:.2f}, Time: {loop_perf['time']:.6f}s, Peak Memory: {loop_perf['memory_peak']:.2f}KB")