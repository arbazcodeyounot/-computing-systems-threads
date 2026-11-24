# Mission 3 – Can multiple threads make a program faster?
# Runs two kinds of job, 4 times each, with 1 worker and with 4 workers (threads).
import sys
import time
import threading

JOBS = 4        # number of jobs, and number of threads in the threaded version
REPEATS = 3     # repeat every test 3 times and take the average

def maths_job():                     # (A) CPU-bound: keeps a core busy calculating
    total = 0
    for i in range(10_000_000):
        total = total + i

def waiting_job():                   # (B) I/O-bound: just waits, like a download
    time.sleep(1)

def one_worker(job):                 # do the jobs one after another, return the time
    start = time.perf_counter()
    for n in range(JOBS):
        job()
    return time.perf_counter() - start

def four_workers(job):               # give each job its own thread, return the time
    start = time.perf_counter()
    workers = []
    for n in range(JOBS):
        t = threading.Thread(target=job)
        t.start()
        workers.append(t)
    for t in workers:
        t.join()
    return time.perf_counter() - start

print("Python", sys.version.split()[0], "| GIL enabled:", sys._is_gil_enabled())
print()

for name, job in [("(A) Heavy maths", maths_job), ("(B) Waiting", waiting_job)]:
    times_one = []
    times_four = []
    for r in range(REPEATS):
        times_one.append(one_worker(job))
        times_four.append(four_workers(job))
    avg_one = sum(times_one) / REPEATS
    avg_four = sum(times_four) / REPEATS
    print(name)
    print("  1 worker  runs:", [round(t, 2) for t in times_one], "average:", round(avg_one, 2), "s")
    print("  4 workers runs:", [round(t, 2) for t in times_four], "average:", round(avg_four, 2), "s")
    print("  Speed-up:", round(avg_one / avg_four, 2), "x")
    print()
