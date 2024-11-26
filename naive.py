import random
import time


def generate_random_numbers(seed_value, count, start, end):
    random.seed(seed_value)
    return [random.randint(start, end) for _ in range(count)]

def bubble_sort(numbers):
    n = len(numbers)
    for i in range(n):
        for j in range(0, n-i-1):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]


def analyze_sort(numbers):
    start_time = time.time()
    bubble_sort(numbers)
    end_time = time.time()
    return end_time - start_time

seed_value = 42
random_numbers = generate_random_numbers(seed_value, 50, 0, 100)


sorted_numbers = sorted(random_numbers)
best_case_time = analyze_sort(sorted_numbers)

# Output hasil
print("50 Bilangan Random sebelum melalui sorting:")
print(random_numbers)

print("\n50 Bilangan Setelah Bubble Sort:")
print(sorted_numbers)

print(f"\nWaktu Eksekusi Best Case: {best_case_time:.6f} detik")
