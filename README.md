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
[Write 1–2 sentences in your own words: when did threads help, when didn't they, and why?]

Code written step by step with help from Claude (an AI tool); I ran every test myself on my own Mac.
