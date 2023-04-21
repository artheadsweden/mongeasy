## Connection

Connection to the database should be easy, and therefor Mongeasy will try to connect to the database for you. If you have the connection information in a configfile or set as environment variables, Mongeasy will use that information to connect to the database. You can also manually handle connection to the database, if needed.

Mongeasy will also let you use connection pooling, retrying and other features of the pymongo library.

### Connection using configfile
You can use a configfile to store the connection information. Create a file called `mongeasy_config.yml` and place it in your project root folder.

For example, if you have a MongoDB instance running on your local machine, the contents of the file should be:

```bash
db_config:
  uri: mongodb://localhost:27017
  database: mydatabase
```
You can also provide a username and password to the connection string:

```bash
db_config:
  uri: mongodb://username:password@localhost:27017
  database: mydatabase
```

### Connection using environment variables
You can, as an alternative method, define your connection information using environment variables. Just set these two:

```bash
MONGOEASY_CONNECTION_STRING=mongodb://localhost:27017/
MONGOEASY_DATABASE_NAME=mydatabase
```

Just as with the configfile, you can also provide a username and password to the connection string:

```bash
MONGOEASY_CONNECTION_STRING=mongodb://username:password@localhost:27017/
MONGOEASY_DATABASE_NAME=mydatabase
```

## Automatic connection
If any of these two options are used, Mongeasy will automatically connect to the database when you use the library. 
