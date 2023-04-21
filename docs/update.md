## Updating Documents
When you have a document object that is already stored, you can update it by changing the attributes and then calling the `save` method.

```python
from mongeasy import create_document_class


User = create_document_class('User', 'users')

# Find one document with age 25
user = User.find({'age': 25}).first()

if user is None:
    print('No user found')
else:
    # Update the age of the user
    user.age = 26
    user.save()
```
