# Enumy
The problem with Python's "Enum" module is that it is not a reasonable way to restrict variables to a predefined set of values.

## Installation
```shell
pip install --user enumy
```

## Special methods
### `check_type`
Check if a variable matches a certain data type.

### `check_value`
Check if a value is present in the allowed values.

## Example
```python
from enumy import Enumy

test = Enumy(("Value 1", "Value 2"), str)
test = "Value 2"        # Working
test = 123              # Exception
```