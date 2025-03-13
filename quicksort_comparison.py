import random
import time
import matplotlib.pyplot as plt
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def randomized_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    # Choose a random pivot element
    pivot = random.choice(arr)
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return randomized_quick_sort(left) + middle + randomized_quick_sort(right)

def deterministic_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    # Choose the middle element as the pivot
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return deterministic_quick_sort(left) + middle + deterministic_quick_sort(right)

def measure_time(sort_function, arr, iterations=5):
    times = []
    for _ in range(iterations):
        test_arr = arr.copy()
        start_time = time.time()
        sort_function(test_arr)
        end_time = time.time()
        times.append(end_time - start_time)
    return sum(times) / len(times)

# Define array sizes for testing
sizes = [10_000, 50_000, 100_000, 500_000]
results_randomized = []
results_deterministic = []

# Perform tests for each array size
for size in sizes:
    test_array = [random.randint(0, 10**6) for _ in range(size)]
    random_time = measure_time(randomized_quick_sort, test_array)
    deterministic_time = measure_time(deterministic_quick_sort, test_array)

    results_randomized.append(random_time)
    results_deterministic.append(deterministic_time)

    print(Fore.YELLOW + f"Array size: {size}")
    print(Fore.GREEN + f"   Randomized QuickSort: {random_time:.4f} seconds")
    print(Fore.CYAN + f"   Deterministic QuickSort: {deterministic_time:.4f} seconds")

# Plot the results
plt.plot(
    sizes, results_randomized, label="Randomized QuickSort", marker="o", color="g"
)
plt.plot(
    sizes,
    results_deterministic,
    label="Deterministic QuickSort",
    marker="s",
    color="b",
)
plt.xlabel("Array size")
plt.ylabel("Average execution time (seconds)")
plt.title("QuickSort Comparison")
plt.legend()
plt.grid()
plt.show()

# Print summary table
print("\nSummary table of results:")
print("Array size | Randomized QuickSort | Deterministic QuickSort")
for size, random_time, deterministic_time in zip(sizes, results_randomized, results_deterministic):
    print(f"{size:15} | {random_time:.4f} seconds         | {deterministic_time:.4f} seconds")

# Analyze efficiency
if sum(results_randomized) < sum(results_deterministic):
    print("Randomized QuickSort was more efficient on average.")
elif sum(results_randomized) > sum(results_deterministic):
    print("Deterministic QuickSort was more efficient on average.")
else:
    print("Both algorithms showed equal efficiency on average.")