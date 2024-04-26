# pynanny #

## Python requirements
Python requirements shall be put in `pyproject.toml`. Any requirements that are necessary to the functioning of the code shall be put in the section labeled `dependencies`. If there are dependencies that are only necessary for development of the code and not necessary for the functioning of this package when pip installed, those will go in the optional dependencies under the header `[project.optional-dependencies]`.

These optional dependencies work by allowing users to specify a bracket and string when pip installing. For example, the following will install all dependencies, including dev dependencies.
```bash
pip install -e .[all]
```

Any time a new dependency subset is added, this needs to be added to the `all` dependency.

If you get an error when pip installing, first, make sure that pip is upgraded with
```bash
pip install --upgrade pip
```

## Python code
All Python code shall be put under `src/pynanny/` and a dunder init (`__init__.py`) file shall be included in all Python subdirectories except for `src`.

## Docker
If this package does not need to build a docker image, feel free to remove the docker directory and the Makefile.

## Testing
Tests should be included for all additions to the code in order to maintain code integrity. Pytest is the testing package of choice and testing will fail if we do not cover 80% of the code.

## Type checking and linting
The primary linter we use is `ruff`. If using VS Code, it is strongly recommended to install the `ruff` extension so that code is formatted on save. If not in VS Code, `ruff` can also be used via command line.
```bash
ruff src/
```
The above command will list all issues in the code and display which are fixable by `ruff`. To fix them automatically, run
```bash
ruff src/ --fix-all
```

Type hints should be used in all function/method/class definitions. This allows for easier readability and debugging. To enforce types, we use a tool called `mypy`. This will look through the code and report type errors. To run `mypy`, use the following command
```bash
mypy src/
```
This will display a brief description of errors along with the file and line of the code.

## Pre-commit hooks
Pre-commit hooks check the code for various things when trying to commit code. To set this up, run
```bash
pre-commit install
```