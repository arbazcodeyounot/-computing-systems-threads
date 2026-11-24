import time
import threading

def job():
    total = 0
    for i in range(10_000_000):
        total = total + i

start = time.perf_counter()
workers = []
for n in range(4):                           # repeat 4 times:
    t = threading.Thread(target=job)         #   hire a worker and give it the recipe
    t.start()                                #   tell the worker to start cooking
    workers.append(t)                        #   write the worker on our list
for t in workers:
    t.join()                                 # wait until every worker has finished
end = time.perf_counter()
print("4 workers, 4 jobs:", round(end - start, 2), "seconds")
