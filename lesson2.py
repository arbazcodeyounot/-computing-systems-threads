import time

def job():                      # a recipe called "job"
    total = 0
    for i in range(10_000_000):
        total = total + i

start = time.perf_counter()
job()                           # cook dish 1
job()                           # cook dish 2
job()                           # cook dish 3
job()                           # cook dish 4
end = time.perf_counter()
print("1 worker, 4 jobs:", round(end - start, 2), "seconds")
