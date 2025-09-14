# Copilot Instructions for AI Coding Agents

## Project Overview
This repository benchmarks Python generator patterns versus traditional loops for performance and memory usage. It contains two main scripts:
- `main.py`: Compares generator vs loop for squaring numbers.
- `main_sum.py`: Compares generator vs loop for summing prices in a large list of dicts.

## Architecture & Patterns
- **Single-file scripts**: Each script is self-contained and executable directly.
- **Performance Measurement**: Both scripts use `tracemalloc` and `time.perf_counter()` to measure execution time and peak memory usage.
- **Generator vs Loop**: The core comparison is between generator expressions/functions and explicit for-loops for large data processing.
- **Data Generation**: `main_sum.py` uses a helper to generate millions of dicts with random prices for realistic benchmarking.

## Key Conventions
- **Entry Point**: Use `if __name__ == "__main__":` for script execution.
- **Function Naming**: Functions are named for clarity (e.g., `measure_performance`, `total_with_generator`).
- **No external dependencies**: Only Python standard library modules (`time`, `tracemalloc`, `random`).
- **Large N values**: Scripts use large data sizes (e.g., `10_000_000`) to stress test performance.

## Developer Workflows
- **Run benchmarks**: Execute scripts directly:
  - `python main.py`
  - `python main_sum.py`
- **Modify N for faster tests**: Reduce `N` or item count for quick iterations.
- **Debugging**: Add print statements or use Python debuggers as needed; scripts are simple and linear.
- **Virtual Environment**: `.venv/` is present; activate before running if dependencies are added.

## Examples
- To compare generator vs loop for squaring numbers:
  ```bash
  python main.py
  ```
- To compare generator vs loop for summing prices:
  ```bash
  python main_sum.py
  ```

## Extending
- Add new benchmark scripts for other patterns in new files.
- Follow the function naming and measurement conventions for consistency.

## References
- Key files: `main.py`, `main_sum.py`
- No README or prior agent instructions found; this file is authoritative.

---
**Feedback:** If any workflow, convention, or architectural aspect is unclear or missing, please specify so it can be improved for future AI agents.
