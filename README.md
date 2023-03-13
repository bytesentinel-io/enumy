# Enumy
The problem with Python's "Enum" module is that it is not a reasonable way to restrict variables to a predefined set of values.

## Installation
```shell
pip install --user enumy
```

## First start
```python
from enumy import Enumy

test = Enumy(("Value 1", "Value 2"), str)
test = "Value 2"        # Working
test = 123              # Exception
```