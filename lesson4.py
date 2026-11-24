import time
import threading

def job():
    time.sleep(1)                  # wait 1 second (like waiting for a download)

# --- 1 worker, 4 jobs one after another ---
start = time.perf_counter()
for n in range(4):
    job()
end = time.perf_counter()
print("1 worker, 4 waiting jobs:", round(end - start, 2), "seconds")

# --- 4 workers, 4 jobs at the same time ---
start = time.perf_counter()
workers = []
for n in range(4):
    t = threading.Thread(target=job)
    t.start()
    workers.append(t)
for t in workers:
    t.join()
end = time.perf_counter()
print("4 workers, 4 waiting jobs:", round(end - start, 2), "seconds")
