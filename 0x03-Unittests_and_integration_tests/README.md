<p align="center">
<img src ="https://i.giphy.com/l0MYSpvx4pnsoMNz2.gif">
</p>

---

# Unittests and Integration Tests

## Resources

- [unittest — Unit testing framework](https://docs.python.org/3/library/unittest.html)
- [unittest.mock — mock object library](https://docs.python.org/3/library/unittest.mock.html)
- [How to mock a readonly property with mock?](https://stackoverflow.com/questions/16486667/how-to-mock-a-readonly-property-with-mock)
- [parameterized](https://pypi.org/project/parameterized/)
- [Memoization](https://en.wikipedia.org/wiki/Memoization)

## Requirements

- **[utils](https://intranet-projects-files.s3.amazonaws.com/webstack/utils.py)**: Contains general utility functions (`access_nested_map`, `get_json`, `memoize`) used by the GitHub organization client for common tasks like accessing nested maps, making HTTP requests, and memoizing methods.
- **[client](https://intranet-projects-files.s3.amazonaws.com/webstack/client.py)**: Defines the `GithubOrgClient` class, representing a GitHub organization client. Utilizes utility functions from `utils.py` for handling JSON requests, accessing nested maps, and memoization. Implements methods to retrieve organization information, get public repositories, and check if a repository has a specific license.
- **[fixtures](https://intranet-projects-files.s3.amazonaws.com/webstack/fixtures.py)**: Provides test fixtures in the form of sample data (`TEST_PAYLOAD`) for unit tests and integration tests. This data includes details of GitHub repositories and is used to test the functionality of the GitHub organization client.

---

## Execute Tests

- Execute your tests with:

```
python -m unittest path/to/test_file.py
```

---

## Tasks

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
