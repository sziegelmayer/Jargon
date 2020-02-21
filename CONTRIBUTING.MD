# Contribute to Jargon

We welcome contributions via pull request. Please observe the following guidelines:

- If you use or modify code from another source, make sure you have permission to do so (check the license)
and under which circumstances (citation etc.)
- We use [numpy style docstrings](https://numpydoc.readthedocs.io/en/latest/format.html). Docstrings need not
include examples, but these are welcome. Please include citations in [square brackets] and cite at the bottom 
of the docstring. Make sure the docstring contains the following fields, where appropriate: `Arguments`, 
`Returns`, `Raises` and `Logs`. `Logs` is special since it is usually not included in numpy style and is used
if a function logs something to a file, e.g. with the `logging` module.
- Please follow [PEP-8 style](https://www.python.org/dev/peps/pep-0008/). We use [`black`](https://github.com/psf/black)
for formatting
- We use type-checked Python throughout. Please use [`mypy`](http://mypy-lang.org) for type checking
- Please try not to write any function without coverage. We use [`pytest`](https://docs.pytest.org/en/latest/). 
We realise some code cannot be covered, please use common sense in these cases.

If you have any question, please open an issue! 