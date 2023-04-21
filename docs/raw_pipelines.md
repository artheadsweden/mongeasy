## Raw Aggregation Pipelines
We can also access MongoDB's powerful aggregation pipeline. This is a way to do complex queries on the database, and is very powerful. You can read more about it in the [MongoDB documentation](https://docs.mongodb.com/manual/aggregation/).

To use the aggregation pipeline, you can use the `aggregate_raw` method. This method takes a list of aggregation stages, and returns a pymongo cursor object. This object can be used to iterate over the results, or to use the pymongo API to do more advanced queries.

```python
from mongeasy import create_document_class


User = create_document_class('User', 'users')

# Find all documents that have the age 25, group them by name, and sort them by count
users = User.aggregate_raw([
    {'$match': {'age': {'$eq': 25}}},
    {'$group': {'_id': '$name', 'count': {'$sum': 1}}},
    {'$sort': {'count': -1}}
])
```