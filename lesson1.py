import time
start = time.perf_counter()
total = 0
for i in range(10_000_000):
    total = total + i
end = time.perf_counter()
print("Time:", round(end - start, 2), "seconds")
