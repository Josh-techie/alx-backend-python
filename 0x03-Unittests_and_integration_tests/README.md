<p align="center">
<img src ="https://i.giphy.com/l0MYSpvx4pnsoMNz2.gif">
</p>

---

# Unittests and Integration Tests

- This project serves as a practical exploration of testing methodologies, the project mostly covers unit testing and integration testing, emphasizing the significance of distinguishing between the two. The tasks include `parameterized` `unit tests`, `mock HTTP calls`, `memoization`, and `property mocking`, providing a comprehensive understanding of practical testing patterns.

---

## Resources

- [unittest — Unit testing framework](https://docs.python.org/3/library/unittest.html)
- [unittest.mock — mock object library](https://docs.python.org/3/library/unittest.mock.html)
- [How to mock a readonly property with mock?](https://stackoverflow.com/questions/16486667/how-to-mock-a-readonly-property-with-mock)
- [parameterized](https://pypi.org/project/parameterized/)
- [Memoization](https://en.wikipedia.org/wiki/Memoization)

---

## Requirements

- **[utils](https://intranet-projects-files.s3.amazonaws.com/webstack/utils.py)**: Contains general utility functions (`access_nested_map`, `get_json`, `memoize`) used by the GitHub organization client for common tasks like accessing nested maps, making HTTP requests, and memoizing methods.
- **[client](https://intranet-projects-files.s3.amazonaws.com/webstack/client.py)**: Defines the `GithubOrgClient` class, representing a GitHub organization client. Utilizes utility functions from `utils.py` for handling JSON requests, accessing nested maps, and memoization. Implements methods to retrieve organization information, get public repositories, and check if a repository has a specific license.
- **[fixtures](https://intranet-projects-files.s3.amazonaws.com/webstack/fixtures.py)**: Provides test fixtures in the form of sample data (`TEST_PAYLOAD`) for unit tests and integration tests. This data includes details of GitHub repositories and is used to test the functionality of the GitHub organization client.

> Anyway you'll find them in the repo, but feel free to download the files if the links still work otherwise just clone them from the repo 😁.

---

## Execute Tests

- Execute your tests with:

```
python -m unittest path/to/test_file.py
```

---

## Tasks

0. **Parameterize a unit test:**

   - **Description:** Implement `TestAccessNestedMap.test_access_nested_map_exception` to test the exception handling in the `access_nested_map` function. Ensure that the test covers scenarios where the function should raise a `KeyError` and verify that it behaves as expected.
   - **File:** [test_utils.py](./test_utils.py)

1. **Use the assertRaises context manager to test KeyError:**

   - **Description:** Use the `assertRaises` context manager to test that a `KeyError` is raised for specific inputs. Use `@parameterized.expand` to parametrize the test.
   - **File:** [test_utils.py](./test_utils.py)

2. **Mock HTTP calls:**

   - **Description:** Implement `TestGetJson.test_get_json` to test that `utils.get_json` returns the expected result. Ensure that the output of `get_json` is equal to `test_payload`.
   - **File:** [test_utils.py](./test_utils.py)

3. **Test Memoize:**

   - **Description:** Implement `TestMemoize.test_memoize` to test the `@memoize` decorator. Mock the `a_method` method using `unittest.mock.patch` and ensure that `a_property` returns the correct result and that `a_method` is only called once.
   - **File:** [test_utils.py](./test_utils.py)

4. **Parameterize and patch as decorators:**

   - **Description:** Implement `TestGithubOrgClient.test_org` to test that `GithubOrgClient.org` returns the correct value. Use `@patch` as a decorator to ensure `get_json` is called once with the expected argument without actually executing it. Parametrize the test with different org examples.
   - **File:** [test_client.py](./test_client.py)

5. **Mocking a property:**

   - **Description:** Implement `TestGithubOrgClient.test_public_repos_url` to unit-test `GithubOrgClient._public_repos_url`. Use `patch` as a context manager to mock `GithubOrgClient.org` and make it return a known payload. Test that the result of `_public_repos_url` is as expected based on the mocked payload.
   - **File:** [test_client.py](./test_client.py)

6. **More patching:**

   - **Description:** Implement `TestGithubOrgClient.test_public_repos` to unit-test `GithubOrgClient.public_repos`. Test that the list of repos is what you expect from the chosen payload. Also, ensure that the mocked property and the mocked `get_json` were called once.
   - **File:** [test_client.py](./test_client.py)

7. **Parameterize:**

   - **Description:** Implement `TestGithubOrgClient.test_has_license` to unit-test `GithubOrgClient.has_license`. Parametrize the test with different inputs and expected returned values.
   - **File:** [test_client.py](./test_client.py)

8. **Integration test: fixtures:**
   - **Description:** Create `TestIntegrationGithubOrgClient` to perform an integration test for `GithubOrgClient.public_repos`. Use `@parameterized_class` to parameterize the class with fixtures from `fixtures.py`. Mock `requests.get` and return example payloads from fixtures.
   - **File:** [test_client.py](./test_client.py)

### Advanced Task

9. **Integration test**
   - **Description:** Implement the `TestIntegrationGithubOrgClient` class to perform an integration test for the `GithubOrgClient.public_repos` method. This integration test will ensure that the method returns the expected results based on the provided fixtures.
   - **File:** [test_client.py](./test_client.py)

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
