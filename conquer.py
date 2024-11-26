import random
import timeit


def generate_random_numbers(seed_value, count, start, end):
    random.seed(seed_value)
    return [random.randint(start, end) for _ in range(count)]

def merge_sort(numbers):
    if len(numbers) > 1:
        mid = len(numbers) // 2 
        left_half = numbers[:mid]
        right_half = numbers[mid:]

       
        merge_sort(left_half)
        merge_sort(right_half)

  
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                numbers[k] = left_half[i]
                i += 1
            else:
                numbers[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            numbers[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            numbers[k] = right_half[j]
            j += 1
            k += 1


def analyze_sort_with_timeit(numbers):
    return timeit.timeit(lambda: merge_sort(numbers[:]), number=1)


seed_value = 42
random_numbers = generate_random_numbers(seed_value, 50, 0, 100)


sorted_numbers = sorted(random_numbers)
best_case_time = analyze_sort_with_timeit(sorted_numbers)


print("50 Bilangan Random Awal:")
print(random_numbers)

print("\n50 Bilangan Setelah Merge Sort:")
merge_sort(random_numbers[:])
print(random_numbers)

print(f"\nWaktu Eksekusi Best Case (sudah terurut): {best_case_time:.10f} detik")
