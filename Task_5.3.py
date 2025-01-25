import timeit

# Алгоритм Боєра-Мура
def boyer_moore(text, pattern):
    m, n = len(pattern), len(text)
    if m > n:
        return -1

    bad_char_shift = {chr(i): m for i in range(256)}
    for i in range(m-1):
        bad_char_shift[pattern[i]] = m - i - 1

    i = m - 1
    while i < n:
        j = m - 1
        while j >= 0 and pattern[j] == text[i]:
            i -= 1
            j -= 1
        if j < 0:
            return i + 1 
        i += bad_char_shift.get(text[i], m)
    return -1 

# Алгоритм Кнута-Морріса-Пратта (KMP)
def kmp(text, pattern):
    m, n = len(pattern), len(text)
    if m > n:
        return -1

    lps = [0] * m
    j = 0
    for i in range(1, m):
        while j > 0 and pattern[i] != pattern[j]:
            j = lps[j-1]
        if pattern[i] == pattern[j]:
            j += 1
        lps[i] = j

    i = j = 0
    while i < n:
        if text[i] == pattern[j]:
            i += 1
            j += 1
            if j == m:
                return i - j
        else:
            if j > 0:
                j = lps[j-1]
            else:
                i += 1
    return -1

# Алгоритм Рабіна-Карпа
def rabin_karp(text, pattern):
    m, n = len(pattern), len(text)
    if m > n:
        return -1
    
    d = 256
    q = 101
    h_pattern = 0
    h_text = 0
    h = 1

    for i in range(m-1):
        h = (h * d) % q

    for i in range(m):
        h_pattern = (d * h_pattern + ord(pattern[i])) % q
        h_text = (d * h_text + ord(text[i])) % q

    for i in range(n - m + 1):
        if h_pattern == h_text:
            if text[i:i+m] == pattern:
                return i
        if i < n - m:
            h_text = (d * (h_text - ord(text[i]) * h) + ord(text[i + m])) % q
            if h_text < 0:
                h_text += q
    return -1

def read_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except UnicodeDecodeError:
        with open(file_path, 'r', encoding='windows-1251') as file:
            return file.read()

def measure_time(text, pattern):
    algorithms = {
        "Боєр-Мур": boyer_moore,
        "Кнут-Морріс-Пратт": kmp,
        "Рабін-Карп": rabin_karp
    }
    results = {}
    for name, algo in algorithms.items():
        time_taken = timeit.timeit(lambda: algo(text, pattern), number=10)
        results[name] = time_taken
    return results

article1_text = read_file("article1.txt")
article2_text = read_file("article2.txt")

existing_substring = "існуючий підрядок"
non_existing_substring = "вигаданий підрядок" 

existing_results = measure_time(article1_text, existing_substring)
non_existing_results = measure_time(article1_text, non_existing_substring)

existing_results = measure_time(article2_text, existing_substring)
non_existing_results = measure_time(article2_text, non_existing_substring)

print("Час виконання для існуючого підрядка:")
for algo, time_taken in existing_results.items():
    print(f"{algo}: {time_taken:.6f} секунд")

print("\nЧас виконання для вигаданого підрядка:")
for algo, time_taken in non_existing_results.items():
    print(f"{algo}: {time_taken:.6f} секунд")
