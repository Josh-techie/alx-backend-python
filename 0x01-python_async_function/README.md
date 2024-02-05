<p align="center">
<img src ="https://www.bing.com/images/blob?bcid=qMKCkrTVyaMGAiOH6KN5u4zeA2Bv.....3o">
</p>

---

# Python - Async

- This project delves into the realm of asynchronous programming in Python, specifically focusing on the async and await syntax, executing async programs with asyncio, running concurrent coroutines, creating asyncio tasks, and utilizing the random module. Explore the intricacies of asynchronous I/O and gain practical experience in building efficient and concurrent Python applications.

---

## Resources

To successfully navigate through this project, make sure to read or watch the following resources:

- [Async IO in Python: A Complete Walkthrough](https://realpython.com/async-io-python/)
- [asyncio - Asynchronous I/O](https://docs.python.org/3/library/asyncio.html)
- [random.uniform](https://docs.python.org/3/library/random.html#random.uniform)

## Tasks

### 0. The basics of async

Implement an asynchronous coroutine, `wait_random`, that takes an integer argument `max_delay` (default value: 10). This coroutine should wait for a random delay between 0 and `max_delay` (inclusive and as a float) seconds and return the delay.

Please find the implementation of this task in the file [0-basic_async_syntax.py](https://github.com/Josh-techie/alx-backend-python/blob/master/0x01-python_async_function/0-basic_async_syntax.py).

### 1. Let's execute multiple coroutines at the same time with async

Import `wait_random` from the previous file and create an async routine, `wait_n`, that takes two integer arguments `n` and `max_delay`. Spawn `wait_random` `n` times with the specified `max_delay` and return the list of delays in ascending order.

For the implementation of this task, please refer to the file [1-concurrent_coroutines.py](https://github.com/Josh-techie/alx-backend-python/blob/master/0x01-python_async_function/1-concurrent_coroutines.py).

### 2. Measure the runtime

Import the `wait_n` function into `2-measure_runtime.py` and create a `measure_time` function that measures the total execution time for `wait_n(n, max_delay)` and returns `total_time / n`. Use the `time` module to measure the approximate elapsed time.

You can find the implementation of this task in the file [2-measure_runtime.py](https://github.com/Josh-techie/alx-backend-python/blob/master/0x01-python_async_function/2-measure_runtime.py).

### 3. Tasks

Import `wait_random` from `0-basic_async_syntax` and write a function, `task_wait_random`, that takes an integer `max_delay` and returns an asyncio.Task.

The implementation for this task can be found in the file [3-tasks.py](https://github.com/Josh-techie/alx-backend-python/blob/master/0x01-python_async_function/3-tasks.py).

### 4. Tasks

Take the code from `wait_n` and create a new function, `task_wait_n`. The code is nearly identical to `wait_n`, except `task_wait_random` is being called.

You can reference the implementation for this task in the file [4-tasks.py](https://github.com/Josh-techie/alx-backend-python/blob/master/0x01-python_async_function/4-tasks.py).

---

## Author:

- [`@Josh-techie`]() | Software Engineer Student

  > Reach out to me if you need any help or have any questions.

  <a href="mailto:youssef.abouyahia@e-polytechnique.ma">
  	<img alt="Feel free to contact me" src="https://img.shields.io/badge/-Ask_me_anything-blue?style=flat&logo=Gmail&logoColor=white&link=mailto:youssef.abouyahia@e-polytechnique.ma&color=3d85c6" />
  </a>
  <span> | </span>
    <a href="https://www.linkedin.com/in/youssef-abouyahia/">
        <img alt="Linkedin Profile" src="https://img.shields.io/badge/-Linkedin-0072b1?style=flat&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/youssef-abouyahia/" />
    </a>
    <span> | </span>
    <a href="https://twitter.com/JoesephAb">
        <img alt="Twitter Profile" src="https://img.shields.io/badge/-Twitter-0072b1?style=flat&logo=Twitter&logoColor=white&link=https://twitter.com/JoesephAb&color=1DA1F2" />
    </a>
