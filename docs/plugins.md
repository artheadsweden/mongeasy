# Mongeasy Plugin System

The Mongeasy library provides a robust and flexible platform for interacting with MongoDB databases. To further enhance its utility and versatility, Mongeasy offers a plugin system. This system allows developers to customize and extend the library's functionality according to their specific needs.

The motivation behind the plugin system is to provide a mechanism for developers to introduce new behaviors or modify existing ones without having to alter the core library code. By doing so, it promotes a modular approach where additional features or modifications can be encapsulated within individual plugins. This system fosters a more maintainable codebase, as plugins can be added, removed, or updated independently, without impacting the overall stability or functionality of the library.

The plugin system can be particularly beneficial in scenarios where customized behaviors or additional features are required. These might include logging operations, implementing custom data validation or transformation rules, handling errors in specific ways, or integrating with other systems or libraries.

In the following sections, we'll delve into more detail about the Mongeasy plugin system, including how to create a plugin, how to register it with the library, and the various hooks available for customization.

### Mongeasy Plugin Hooks

In Mongeasy, plugins are implemented as classes, and they interact with the library through a series of predefined hook points. A hook point is essentially an event during the lifecycle of the library's operation where a plugin can intervene and perform custom actions. The following are the hook points provided by Mongeasy, listed as method signatures in the plugin class:

1. `before_connect(self)`: This method is called before the connection to the MongoDB database is established.

2. `after_connect(self)`: This method is called after a successful connection to the MongoDB database is established.

3. `before_close(self)`: This method is called before closing the connection to the MongoDB database.

4. `after_close(self)`: This method is called after the connection to the MongoDB database has been closed.

5. `before_delete_document(self, *args, **kwargs)`: This method is called before a document is deleted from the database. The document that will be deleted is passed as an argument.

6. `after_delete_document(self, *args, **kwargs)`: This method is called after a document has been deleted from the database. The document that was deleted is passed as an argument.

7. `before_init_document(self, *args, **kwargs)`: This method is called before initializing a new document. The data used to initialize the document is passed as arguments.

8. `after_init_document(self, data)`: This method is called after a new document has been initialized. The newly initialized document is passed as an argument.

9. `before_query_document(self, cls, *args, **kwargs)`: This method is called before a query is made on the database. The class of the document to be queried and the query parameters are passed as arguments.

10. `after_query_document(self, cls, *args, **kwargs)`: This method is called after a query is made on the database. The class of the document queried and the result of the query are passed as arguments.

11. `before_save_document(self, *args, **kwargs)`: This method is called before a document is saved to the database. The document to be saved and the save parameters are passed as arguments.

12. `after_save_document(self, data)`: This method is called after a document has been saved to the database. The data of the saved document is passed as an argument.

13. `validate_document(self, *args, **kwargs)`: This method is called to validate a document before it is saved. The document and the validation parameters are passed as arguments.

14. `on_document_validation_error(self, *args, **kwargs)`: This method is called when a document fails validation. The document and the error information are passed as arguments.

These hook points allow a plugin to observe and intervene in the key operations of the Mongeasy library, providing the flexibility to extend and customize its behavior.

### Example Plugin
You can develop and use a local plugin by creating a plugin class and register it.

I see, thank you for providing the correct information.

Here's the corrected example:

Create your plugin class:

```python
class MyLoggingPlugin:
    def before_save_document(self, *args, **kwargs):
        print(f"before_save_plugin: before_save, data: {args}, {kwargs}")
            
    def after_save_document(self, data):
        print(f"after_save_plugin: after_save, data: {data}")
```

Now, let's register this plugin in the `mongeasy_conf.yml`:

```yaml
# mongeasy_conf.yml
db_config:
  uri: mongodb://localhost:27017
  database: mydatabase

plugins:
  - my_logging_plugin.MyLoggingPlugin
```

In the `plugins` section, you specify the Python import path to your plugin class. In this example, it is assumed that your `MyLoggingPlugin` class is located in a Python file named `my_logging_plugin.py` in the same directory as your `mongeasy_conf.yml`. If your plugin is located elsewhere, adjust the import path accordingly.

Once you have done this, the `MyLoggingPlugin` will be active when you start your application, and it will log information whenever a document is saved.

### Developing Distributable Plugins

If you have developed a plugin that you think would be useful for other users of Mongeasy, you can package it and distribute it via PyPI, the Python Package Index. This allows others to easily install your plugin using `pip`.

Here are the general steps you need to follow to package your plugin:

1. **Create a new Python project for your plugin.** You will need to create a new Python project directory for your plugin. This should include an `__init__.py` file and a separate Python file for each plugin class.

2. **Create a `setup.py` file.** This file is used by Python's packaging tools to install your plugin. It should specify your plugin's name, version, and any dependencies it has. Here's an example `setup.py` file:

    ```python
    from setuptools import setup, find_packages

    setup(
        name='your_plugin_name',
        version='0.1',
        packages=find_packages(),
        entry_points={
            'mongeasy.plugins': [
                'your_plugin_name = your_package.your_module:YourPluginClass',
            ],
        },
        install_requires=[
            'mongeasy',
            # any other dependencies your plugin has
        ],
    )
    ```

3. **Package your plugin.** Once you have your `setup.py` file, you can create a distributable package for your plugin using the following command: `python setup.py sdist bdist_wheel`. This will create a `.tar.gz` file and a `.whl` file in a `dist/` directory.

4. **Upload your plugin to PyPI.** You can upload your plugin to PyPI using the `twine` tool. First, install `twine` using `pip install twine`. Then, upload your plugin using `twine upload dist/*`.

Remember that your plugin class should include the necessary hook methods (e.g., `before_save_document(self, *args, **kwargs)`, `after_save_document(self, data)`, etc.), which will be automatically called by Mongeasy at the appropriate times.

Once your plugin is on PyPI, users can install it with pip (`pip install your-plugin-name`) and then add it to their `mongeasy_conf.yml` configuration file like so:

```yaml
plugins:
  - your_plugin_name.YourPluginClass
```

As always, when developing a plugin, remember to respect the privacy and security of the user's data.