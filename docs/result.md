## The ResultList Class
Queries that return multiple documents return a ResultList object. This object can be used to iterate over the results.

The class is based on a normal python list, so you can use all the normal list methods on it. In addition, it has a a number of convenience methods.

```python
from mongeasy import create_document_class


User = create_document_class('User', 'users')

# Find all users
users = User.find()

# Get the first user
first_user = users.first()

# Get the last user
last_user = users.last()

# Sort the users by age
users.sort(lambda user: user.age)

# Sort the users by age, descending
users.sort(lambda user: user.age, reverse=True)

# Group the users by age, will result in a dict with age as key and a list of users as value
users.group_by(lambda user: user.age)

# Get a random user
random_user = users.random()

# Filter the users by age
users.filter(lambda user: user.age > 25)

# Use map to increase the age of all users by 1
users.map(lambda user: user.age + 1)

# Use reduce to get the sum of all ages
sum_of_ages = users.reduce(lambda user, total: user.age + total, 0)
```



