## Mongeasy Query Class
Mongeasy aims to streamline your database querying process by providing a Query class. With this class, you can create database queries using Python-like syntax, making the process more intuitive and accessible.

### Query objects
Mongeasy's Query objects simplify the database querying process. Instead of using traditional MongoDB syntax, you can construct and execute your queries using more familiar Python syntax.

For instance, consider this MongoDB query:
```python
query = {'$or': [{'$or': [{'name': {'$eq': 'John'}}, {'age': {'$lt': 40}}]}, {'$and': [{'name': {'$eq': 'Jane'}}, {'age': {'$gt': 20}}]}]}
```

You can achieve the same result using the Query object:

```python
from mongeasy.core import Query

query = Query('(name == "John" or age < 40) or (name == "Jane" and age > 20)')
```

The resulting Query object can then be used in your database queries like so:

```python
from mongeasy import create_document_class
from mongeasy.core import Query

User = create_document_class('User', 'users')
query = Query('(name == "John" or age < 40) or (name == "Jane" and age > 20)')
result = User.find(query)
```

### Supported operators
Mongeasy Query objects support several operators, enhancing their flexibility and utility:

#### Comparison operators
* `==`: Equal
* `!=`: Not equal
* `<`: Less than
* `>`: Greater than
* `<=`: Less than or equal to
* `>=`: Greater than or equal to

Example:
```python
from mongeasy.core import Query

# Find all users older than 20
query = Query('age > 20')

# Find all users who are 25 years old
query = Query('age == 25')

# Find all users who are not 25 years old
query = Query('age != 25')

# Find all users aged 25 or younger
query = Query('age <= 25')
```

#### Logical operators
* `and`
* `or`
* `not`

Example:
```python
from mongeasy.core import Query

# Find all 25-year-old users named John
query = Query('age == 25 and name == "John"')

# Find all users who are 25 years old or named John
query = Query('age == 25 or name == "John"')

# Find all users who are not 25 years old
query = Query('not age == 25')
```

#### Element operators
* `in`
* `not in`

Example:
```python
from mongeasy.core import Query

# Find all users aged 25 or 30
query = Query('age in [25, 30]')

# Find all users who are not aged 25 or 30
query = Query('age not in [25, 30]')
```

You can also use the Query objects to access subdocuments or nested fields in your documents using the dot notation:

```python
query = Query('age > 25 and friends.age == 32')
```

For erroneous queries, an error will be raised, providing detailed information about the issue:

```python
try:
    query = Query("age <> 25")  # Invalid operator
except ValueError as e:
    print(e)
```

To ensure all functionalities work as expected, Mongeasy provides a suite of pytest tests covering all operators and several complex query scenarios.