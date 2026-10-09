import numpy as np
import pickle

def generate_items(n):
    prices = np.random.uniform(1, 100, n)
    return [{'name': f'item{i}', 'price': float(prices[i])} for i in range(n)]

if __name__ == "__main__":
    N = 1_000_000
    items = generate_items(N)
    print(f"Generated {N} items")
    with open("items.pickle", "wb") as f:
        pickle.dump(items, f)
    print(f"Saved to items.pickle")
