# Enumy
The problem with Python's "Enum" module is that it is not a reasonable way to restrict variables to a predefined set of values.

Latest version: `v1.0.2`

## Installation
```shell
pip install --user enumy
```

## Special methods
### `check_type`
Check if a variable matches a certain data type.

```python
var.check_type(str)
```

### `check_value`
Check if a value is present in the allowed values.

```python
text = "ByteSentinel"
var.check_value(text)
```

## Example
```python
from enumy import Enumy

test = Enumy(("Value 1", "Value 2"), str)
test = "Value 2"        # Working
test = 123              # Exception
```