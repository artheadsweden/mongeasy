## Raw Queries
At times, the built in methods are not enough. In these cases, you can use the raw pymongo API. This is done by using the `find_raw` method. This method will return a pymongo cursor object. This object can be used to iterate over the results, or to use the pymongo API to do more advanced queries.

```python
from mongeasy import create_document_class


User = create_document_class('User', 'users')

# Find all documents
users = User.find_raw()

# Find all documents with age 25
users = User.find_raw({'age': {'$eq': 25}})

# Find all documents with age 25 and name 'Alice'
users = User.find_raw({'age': {'$eq': 25}, 'name': {'$eq': 'Alice'}})
```

The query syntax is the same as the pymongo API. You can find more information about the query syntax [here](https://docs.mongodb.com/manual/tutorial/query-documents/).
