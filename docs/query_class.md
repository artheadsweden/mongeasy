## Mongeasy Query Class
It should be easy to query the database, and Mongeasy provides a query class to make it easy to query the database using python syntax.

### Query objects
To simplify queries to the database you can use the mongeasy query object. You construct it and make your query using normal python syntax.

Instead of using a mongodb query like this
```python
query = {'$or': [{'$or': [{'name': {'$eq': 'John'}}, {'age': {'$lt': 40}}]}, {'$and': [{'name': {'$eq': 'Jane'}}, {'age': {'$gt': 20}}]}]}
```

you can accomplish the same thing by using the Query object

```python
from mongeasy.core import Query


query = Query('(name == "John" or age < 40) or (name == "Jane" and age > 20)')
```

The query can then be used in your queries like this:

```python
from mongeasy import create_document_class
from mongeasy.core import Query


User = create_document_class('User', 'users')
query = Query('(name == "John" or age < 40) or (name == "Jane" and age > 20)')
result = User.find(query)
```

### Supported operators
Query objects support the following operators:

#### Comparison operators
* Equal
* Not equal
* Less than
* Greater than
* Less than or equal to
* Greater than or equal to

Example:
```python
from mongeasy.core import Query

# Find all users with age 25
query = Query('age > 20')

# Find all users with age 25
query = Query('age == 25')

# Find all users with age not 25
query = Query('age != 25')

# Find all users with age less than or eqaul to 25
query = Query('age <= 25')
```

#### Logical operators
* and
* or
* not

Example:
```python
from mongeasy.core import Query

# Find all users with age 25 and name John
query = Query('age == 25 and name == "John"')

# Find all users with age 25 or name John
query = Query('age == 25 or name == "John"')

# Find all users with age not 25
query = Query('not age == 25')
```

#### Element operators
* in
* not in

Example:
```python
from mongeasy.core import Query

# Find all users with age 25 or 30
query = Query('age in [25, 30]')

# Find all users with age not 25 or 30
query = Query('age not in [25, 30]')
```

#### Existence operators
* exists

Example:
```python
from mongeasy.core import Query

# Find all users with a field age
query = Query('exists(age)')
```

#### In string operators
* in

Example:
```python
from mongeasy.core import Query

# Find all users 'oh' in name, like 'John' or 'Mohammed'
query = Query('"oh" in name')
```
