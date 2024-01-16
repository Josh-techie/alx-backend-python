![ALX Logo](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2019/12/ee85b9f67c384e29525b.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%252F20240116%252Fus-east-1%252Fs3%252Faws4_request&X-Amz-Date=20240116T141406Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=0eabbd25da7801c3ed65349e242265ecdb19cbdec3a5ef9303b819cfe2c84abe)

# Project: 0x02. Python - Async Comprehension

## Overview

This project explores asynchronous programming in Python with a focus on asynchronous generators, async comprehensions, and type-annotated generators. Understand how to write asynchronous generators, use async comprehensions, and effectively type-annotate generators in Python.

## Learning Objectives

Upon completion of this project, you will achieve proficiency in the following areas:

- Writing asynchronous generators.
- Utilizing async comprehensions for efficient asynchronous programming.
- Type-annotating generators for improved code readability and maintenance.

## Resources

To successfully navigate through this project, refer to the following resources:

- [PEP 530 – Asynchronous Comprehensions](https://www.python.org/dev/peps/pep-0530/)
- [What’s New in Python: Asynchronous Comprehensions / Generators](https://docs.python.org/3/whatsnew/3.6.html#pep-530-asynchronous-comprehensions)
- [Type-hints for generators](https://docs.python.org/3/library/typing.html#typing.Generator)

## Tasks

### 0. Async Generator

Write a coroutine called `async_generator` that loops 10 times, asynchronously waiting 1 second each time, and then yields a random number between 0 and 10. Use the `random` module.

The implementation for this task can be found in the file [0-async_generator.py](https://github.com/Josh-techie/alx-backend-python/blob/master/0x02-python_async_comprehension/0-async_generator.py).

### 1. Async Comprehensions

Import `async_generator` from the previous task and write a coroutine, `async_comprehension`, that collects 10 random numbers using an async comprehension over `async_generator`. Return the 10 random numbers.

For the implementation of this task, please refer to the file [1-async_comprehension.py](https://github.com/Josh-techie/alx-backend-python/blob/master/0x02-python_async_comprehension/1-async_comprehension.py).

### 2. Run time for four parallel comprehensions

Import `async_comprehension` from the previous file and write a `measure_runtime` coroutine that will execute `async_comprehension` four times in parallel using `asyncio.gather`. Measure the total runtime and return it.

You can find the implementation of this task in the file [2-measure_runtime.py](https://github.com/Josh-techie/alx-backend-python/blob/master/0x02-python_async_comprehension/2-measure_runtime.py).

## Author

- More about me on: [Josh-techie](https://github.com/Josh-techie)
