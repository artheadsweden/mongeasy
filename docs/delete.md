## Deleting Documents

### Deleting the current document
When you have a document object that is already stored, you can delete it by calling the `delete` method.

```python
from mongeasy import create_document_class


User = create_document_class('User', 'users')

# Find one document with age 25
user = User.find({'age': 25}).first()

if user is None:
    print('No user found')
else:
    # Delete the user
    user.delete()
```

### Deleting Documents Based on a Query
You can delete all documents in a collection that match a query by calling the `delete` class method.

```python
from mongeasy import create_document_class


User = create_document_class('User', 'users')

# Delete all users with age 25
User.delete({'age': 25})


# Delete all users
User.delete()
```

