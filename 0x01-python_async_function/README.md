# Project: 0x01. Python - Async

## Overview

This project delves into the realm of asynchronous programming in Python, specifically focusing on the async and await syntax, executing async programs with asyncio, running concurrent coroutines, creating asyncio tasks, and utilizing the random module. Explore the intricacies of asynchronous I/O and gain practical experience in building efficient and concurrent Python applications.

## Learning Objectives

By completing this project, you will gain proficiency in the following areas:

- Understanding and implementing async and await syntax.
- Executing async programs using asyncio.
- Running concurrent coroutines for enhanced performance.
- Creating asyncio tasks for efficient asynchronous operations.
- Harnessing the power of the random module in asynchronous programming.

## Resources

To successfully navigate through this project, make sure to read or watch the following resources:

- [Async IO in Python: A Complete Walkthrough](https://realpython.com/async-io-python/)
- [asyncio - Asynchronous I/O](https://docs.python.org/3/library/asyncio.html)
- [random.uniform](https://docs.python.org/3/library/random.html#random.uniform)

## Tasks

### 0. The basics of async

Implement an asynchronous coroutine, `wait_random`, that takes an integer argument `max_delay` (default value: 10). This coroutine should wait for a random delay between 0 and `max_delay` (inclusive and as a float) seconds and return the delay.

Please find the implementation of this task in the file [0-basic_async_syntax.py](<Link to file in repository>).

### 1. Let's execute multiple coroutines at the same time with async

Import `wait_random` from the previous file and create an async routine, `wait_n`, that takes two integer arguments `n` and `max_delay`. Spawn `wait_random` `n` times with the specified `max_delay` and return the list of delays in ascending order.

For the implementation of this task, please refer to the file [1-concurrent_coroutines.py](<Link to file in repository>).

### 2. Measure the runtime

Import the `wait_n` function into `2-measure_runtime.py` and create a `measure_time` function that measures the total execution time for `wait_n(n, max_delay)` and returns `total_time / n`. Use the `time` module to measure the approximate elapsed time.

You can find the implementation of this task in the file [2-measure_runtime.py](<Link to file in repository>).

### 3. Tasks

Import `wait_random` from `0-basic_async_syntax` and write a function, `task_wait_random`, that takes an integer `max_delay` and returns an asyncio.Task.

The implementation for this task can be found in the file [3-tasks.py](<Link to file in repository>).

### 4. Tasks

Take the code from `wait_n` and create a new function, `task_wait_n`. The code is nearly identical to `wait_n`, except `task_wait_random` is being called.

You can reference the implementation for this task in the file [4-tasks.py](<Link to file in repository>).

## Author

- More about me on: [Josh-techie](https://github.com/Josh-techie)
