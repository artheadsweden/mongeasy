## Creating New Documents
The class we get from the `create_document_class` function can be used to create new documents. We can either use keyword arguments or pass a dict.

```python
from mongeasy import create_document_class


User = create_document_class('User', 'users')

# Create a document using keyword arguments
user1 = User(name='Alice', age=25)

# Create a document using a dict
user2 = User({'name': 'Bob', 'age': 30})
```

## Saving Documents
To save a document to the database, we can use the `save` method on the document.

```python
from mongeasy import create_document_class


User = create_document_class('User', 'users')

# Create a document using keyword arguments
user1 = User(name='Alice', age=25)
user1.save()
```	