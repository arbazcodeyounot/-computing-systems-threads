# Computing Systems – Mission 3: Do threads make a program faster?

A small Python experiment that runs 4 equal jobs in two ways:
- **1 worker:** the jobs run one after another (sequential)
- **4 workers:** each job gets its own thread (concurrent)

It tests two kinds of job:
- **(A) Heavy maths (CPU-bound):** adds up 10 million numbers
- **(B) Waiting (I/O-bound):** waits 1 second, like waiting for a download

Each test is repeated 3 times and the average is printed.

## Requirements
- Python 3 (tested with Python 3.14.7 on macOS 15.7.3, MacBook Air M4, run locally)

## How to run
1. Download `threads_experiment.py`
2. Open Terminal and go to the folder that contains it
3. Run:
4. 4. It takes about 20 seconds and prints the times for each test

## Files
| File | What it is |
| --- | --- |
| `threads_experiment.py` | The final experiment (the artefact) |
| `lesson1.py` | Times one maths job |
| `lesson2.py` | 4 maths jobs, 1 worker |
| `lesson3.py` | 4 maths jobs, 4 threads |
| `lesson4.py` | 4 waiting jobs, 1 worker vs 4 threads |

## My results (24 Nov 2026, Python GIL enabled)
| Test | 1 worker (avg) | 4 threads (avg) | Speed-up |
| --- | --- | --- | --- |
| (A) Heavy maths | 0.50 s | 0.52 s | 0.96x |
| (B) Waiting | 4.02 s | 1.01 s | 3.99x |

## What I found
The story in 4 sentences
You asked: if I give 4 jobs to 4 workers (threads) instead of 1 worker, will they finish faster?
You predicted: yes, faster in both cases.
You tested it with a Python program you built step by step on your own Mac.
You found: for waiting jobs, 4 threads were 4× faster. For maths jobs, they were no faster at all, because Python's GIL only lets one thread do maths at a time, even though your Mac has 10 cores.

Code written step by step with help from Claude (an AI tool); I ran every test myself on my own Mac.
