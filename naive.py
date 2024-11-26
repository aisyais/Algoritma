import random
import timeit

def generate_random_numbers(seed_value, count, start, end):
    random.seed(seed_value)
    return [random.randint(start, end) for _ in range(count)]

def optimized_bubble_sort(numbers):
    n = len(numbers)
    for i in range(n):
        swapped = False  
        for j in range(0, n-i-1):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
                swapped = True
  
        if not swapped:
            break


def analyze_sort_with_timeit(numbers):
    return timeit.timeit(lambda: optimized_bubble_sort(numbers[:]), number=1)


seed_value = 42
random_numbers = generate_random_numbers(seed_value, 50, 0, 100)

sorted_numbers = sorted(random_numbers)  
best_case_time = analyze_sort_with_timeit(sorted_numbers)


print("50 Bilangan Random Sebelum melalui Sorting:")
print(random_numbers)

print("\n50 Bilangan Setelah Bubble Sort:")
optimized_bubble_sort(random_numbers)
print(random_numbers)

print(f"\nWaktu Eksekusi Best Case (sudah terurut): {best_case_time:.10f} detik")
