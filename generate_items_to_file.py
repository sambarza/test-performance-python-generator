import random
import pickle

def generate_items(n):
    rand_uniform = random.uniform
    return [{'name': f'item{i}', 'price': rand_uniform(1, 100)} for i in range(n)]

if __name__ == "__main__":
    N = 100_000_000
    items = generate_items(N)
    with open("items.pickle", "wb") as f:
        pickle.dump(items, f)
    print(f"Generated {N} items and saved to items.pickle")
