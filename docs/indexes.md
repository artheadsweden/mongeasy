## Indexing the Database
You can create indexes on the database using the `create_index` method on the generated class.

```python
from mongeasy import create_document_class


User = create_document_class('User', 'users')

# Create an index on the age field
User.create_index('age')

# Create a unique index on the name field
User.create_index('name', unique=True)

# Create a unique index on the name field, with a custom name
User.create_index('name', unique=True, name='unique_name')

# Create a unique index on the name field, with a custom name, and a custom collation
User.create_index('name', unique=True, name='unique_name', collation={'locale': 'en', 'strength': 2})
```

The syntax is the same as the pymongo API. You can find more information about the syntax [here](https://docs.mongodb.com/manual/reference/method/db.collection.createIndex/).