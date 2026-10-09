import time
import tracemalloc
import random
import json
import pickle
import pandas as pd

# Generate sample data: list of items with 'price'

# Generator function to yield prices
def price_generator(items):
    return (item['price'] for item in items)

# Function to calculate total using generator
def total_with_generator(items):
    return sum(price_generator(items))

# Function to calculate total using pandas
def total_with_pandas(df):
    return df['price'].sum()

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

    with open("items.pickle", "rb") as f:
        items = pickle.load(f)
    print(f"Loaded {len(items):,}".replace(",", ".") + " items from items.pickle")

    gen_perf = measure_performance(total_with_generator, items)
    print(f"Generator - Total: {gen_perf['result']:.2f}, Time: {gen_perf['time']:.6f}s, Peak Memory: {gen_perf['memory_peak']:.2f}KB")

    loop_perf = measure_performance(total_with_loop, items)
    print(f"Loop      - Total: {loop_perf['result']:.2f}, Time: {loop_perf['time']:.6f}s, Peak Memory: {loop_perf['memory_peak']:.2f}KB")

    df_creation_perf = measure_performance(pd.DataFrame, items)

    df = df_creation_perf['result']
    print(f"DataFrame created Time: {df_creation_perf['time']:.6f}s, Peak Memory: {df_creation_perf['memory_peak']:.2f}KB")

    pandas_perf = measure_performance(total_with_pandas, df)
    print(f"Pandas    - Total: {pandas_perf['result']:.2f}, Time: {pandas_perf['time']:.6f}s, Peak Memory: {pandas_perf['memory_peak']:.2f}KB")
