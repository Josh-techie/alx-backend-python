<p align="center">
<img src ="https://th.bing.com/th/id/OIP.Ij5B6XuK_xIzchpQrtOqBgAAAA?rs=1&pid=ImgDetMain">
</p>

---

# Python - Async Comprehension

- This project explores asynchronous programming in Python with a focus on asynchronous generators, async comprehensions, and type-annotated generators. Understand how to write asynchronous generators, use async comprehensions, and effectively type-annotate generators in Python.

---

## Resources

- [PEP 530 – Asynchronous Comprehensions](https://www.python.org/dev/peps/pep-0530/)
- [What’s New in Python: Asynchronous Comprehensions / Generators](https://docs.python.org/3/whatsnew/3.6.html#pep-530-asynchronous-comprehensions)
- [Type-hints for generators](https://docs.python.org/3/library/typing.html#typing.Generator)

---

## Tasks

0. **Async Generator**

   - **Task:** Write a coroutine called `async_generator` that loops 10 times, asynchronously waiting 1 second each time, and then yields a random number between 0 and 10. Use the `random` module.

   - **File:** [0-async_generator.py](./0-async_generator.py)

1. **Async Comprehensions**

   - **Task:** Import `async_generator` from the previous task and write a coroutine, `async_comprehension`, that collects 10 random numbers using an async comprehension over `async_generator`. Return the 10 random numbers.

   - **File:** [1-async_comprehension.py](./1-async_comprehension.py)

2. **Run time for Four Parallel Comprehensions**

   - **Task:** Import `async_comprehension` from the previous file and write a `measure_runtime` coroutine that will execute `async_comprehension` four times in parallel using `asyncio.gather`. Measure the total runtime and return it.

   - **File:** [2-measure_runtime.py](./2-measure_runtime.py)

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
