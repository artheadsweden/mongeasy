## Creating a new Document Class
When working with schemaless database, like MongoDB, there is not really a need for a schema. You can just store the data as it is used in your application. This is why Mongeasy does not require you to define a schema for your documents. 

You will need a class to represent your documents. This is where Mongeasy comes in. You can use the `create_document_class` factory function to create a class that can be used to store documents in a collection.

This class will give you access to the database specific methods, like `save`, `find`, `all` and `delete`.

To create a document class you will use the `create_document_class` factory function like this:

```python
from mongeasy import create_document_class


User = create_document_class('User', 'users')
```

The first argument is the name the class will get and the second argument is the name of the collection to use. If the collection does not exist it will be created when you use the class to store documents.

The collection name is optional. If you do not provide a collection name, the class name, in lowercase and pluralized, will be used.

If you don't want, you will not need to assign it to a class variable as in the example above, as the generated class is injected into the current namespace:

```python
from mongeasy import create_document_class


create_document_class('User', 'users')
```

The class `User` exist from this point in the code.

### Adding Base Classes
You can add base classes to the generated class. This can be useful if you want to add methods to the class. The base classes will be added to the generated class in the order they are provided.

```python
from mongeasy import create_document_class


class UserBase:
    def say_hello(self):
        print(f'Hello, my name is {self.name}')

User = create_document_class('User', 'users', base_classes=(UserBase, ))
```

This will add the `say_hello` method to the generated class.

This can be useful if you, for example, use a library like flask-login to handle user authentication. You can add the `UserMixin` class from flask-login to the generated class to get access to the methods it provides.

```python
from mongeasy import create_document_class
from flask_login import UserMixin


User = create_document_class('User', 'users', base_classes=(UserMixin, ))
```

### Adding Methods
You can add methods to the generated class. This can be useful if you want to add methods to the class. The methods will be added to the generated class in the order they are provided.

```python
from mongeasy import create_document_class


def say_hello(self):
    print(f'Hello, my name is {self.name}')

User = create_document_class('User', 'users')
User.say_hello = say_hello
```

In the case of working with flask-login, you can have a setup like this:

```python
from flask import Flask
from flask_login import UserMixin, LoginManager
from mongeasy import create_document_class
from bson import ObjectId

login_manager = LoginManager()
# Create User class with mongeasy and UserMixin from flask_login as a base class
User = create_document_class('User', 'users', base_classes=(UserMixin,))
def get_id(self):
    return str(self._id)
# Add get_id method to User class
User.get_id = get_id


def create_app():
    app = Flask(__name__)
   # Define the user loader function for Flask-Login
    @login_manager.user_loader
    def load_user(user_id):
        # Load the user object from the database using the user_id
        user_id = ObjectId(user_id)
        user = User.find(_id=user_id).first()
        return user

    return app

```