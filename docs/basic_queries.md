## Basic Queries

### Find
Using the find method is the most basic way to query the database. The find method returns a ResultList object which can be used to iterate over the results. The ResultList object also has a `first` method which returns the first result.

```python
from mongeasy import create_document_class


User = create_document_class('User', 'users')

# Find all users
users = User.find()

# Find all users with age 25, using a dict
users = User.find({'age': 25})

# Find all users with age 25, using keyword arguments
users = User.find(age=25)

# Find all users with age 25 and name 'Alice'
users = User.find(age=25, name='Alice')

# Find all users with age 25 and name 'Alice', using a dict
users = User.find({'age': 25, 'name': 'Alice'})

# Find one user with age 25
user = User.find(age=25).first()

# Find one user with age 25, using a dict   
user = User.find({'age': 25}).first()
```

### Get by id
You can get a document by its id using the `get_by_id` method on the generated class.

```python
from mongeasy import create_document_class


User = create_document_class('User', 'users')

# Get a user by id
user = User.get_by_id('5f9c1c1c9c9c9c9c9c9c9c9c')
```

### Find in
You can find documents where a field is in a list of values using the `find_in` method on the generated class.

```python
from mongeasy import create_document_class


User = create_document_class('User', 'users')

# Find all users with age 25 or 30
users = User.find_in('age', [25, 30])
```

### Get all documents
You can get all documents using the `all` method on the generated class.

```python
from mongeasy import create_document_class


User = create_document_class('User', 'users')

# Get all users

users = User.all()
```

### Get all as and iterator
You can get all documents as an iterator using the `all_iter` method on the generated class.

```python
from mongeasy import create_document_class


User = create_document_class('User', 'users')

# Get all users as an iterator
for user in User.all_iter():
    print(user)
```

### Lazy Querying
The find method has a lazy flag which can be set to True to make the query lazy. This means that the query will not be executed until the results are iterated over. This can be useful if you want to add more conditions to the query after it has been created.

```python
from mongeasy import create_document_class


User = create_document_class('User', 'users')

# Create a lazy query
users = User.find(lazy=True)

# Add conditions to the query
users = User.find(lazy=True, age=25)
```




