# webAPPWithMongoDB
Building a flask based application with mongoDB as backend data base.

# Set Up
##### 1. MongoDB
##### 2. Flask
    2.1 Flask-MongoEngine {for handling MongoDB in an object-oriented way}
    2.2 Flask-Bcrypt {for encrypting passwords}
    2.3 Flask-RESTful {for building REST APIs}
    2.4 Flask-JWT-Extended {for authentication and authorization}
##### 3. Postman
    Sampling data and using GET, PUT, POST, DELETE requests


## 1. MongoDB
### Intro to MongoDB:
  Choosing the right type of database for your project is incredibly important. A traditional SQL database stores information in tables. This is in contrast to a noSQL database. MongoDB is a noSQL database which stores data in JSON format. As opposed to tables, JSON forms a tree data structure. The individual records are known as ‘documents.’ (I would recommend staring at the Pokemon JSON data above until you are convinced that it is a tree instead of a table.)

### Installation and starting a server:
  You can get the free version of MongoDB at https://www.mongodb.com/download-center/community

### Default Installation Options
  The defaults are fine for now. Compass is optional, we won’t be using it in this tutorial. Wherever you install MongoDB and your database, make sure to remember the location.

    Launch Server: C:\Program Files\MongoDB\Server\4.2\bin\mongod.exe

  Leave your server running in the background, you can now access your database from the mongo shell or as we will see later, also from python. This is an unsecured server, and  later we will add authorization.

    Launch Mongo Shell: C:\Program Files\MongoDB\Server\4.2\bin\mongo.exe

  I would recommend looking at the MongoDB documentation as you play around https://docs.mongodb.com/manual/reference/mongo-shell/

### Basic Excersice:
  Let’s insert a few records (documents) into our database. (You can copy and then use right-click to paste these into the mongo command shell.)

    use test_db
    db.meals.insert({"name": "Mystery Pie", "description": "Not even the baker knows what's inside..."})
    db.meals.insert({"name": "Apple Pie", "description": "A delicious, home-made apple pie. Best served on a window sill in the summer."})

  The ‘use’ will select a db (or create one), and you may notice that the records we inserted are in JSON format. Also, mongo will automatically create the collection if it doesn’t exist. Above, our collection is called ’meals’.

  Verify that everything worked by pasting each of the following into mongo.

    show databases
    show collections
    db.meals.find()
    db.meals.find({"name": "Apple Pie"})

  Using db.<collection>.find() will return all of the data, and we can filter by passing JSON as a parameter into the find() method.

  Every item you add will have a unique ObjectId. This will become handy later for referencing items from other collections, such as users.Play around with making databases, collections, and documents. You now have the very basics of running a database.
  
  


For security, set up admin credentials to your database. (Maybe don’t make your password as “password”)

    use admin
    db.createUser(
      {
        user: "admin",
        pwd: "password",
        roles: [ { role: "userAdminAnyDatabase", db: "admin" }, "readWriteAnyDatabase" ]
      }
    )
    db.adminCommand( { shutdown: 1 } )

The last command will shut down our server. To launch the server with authentication enabled, run this from the terminal instead.

    mongod --auth

With this server running, you won’t be able to do anything without authenticating first. You can test this by relaunching mongo.exe and trying to access some data. Enter the following into the mongo shell to sign in and gain access.

    use admin
    db.auth("admin", "password")
We now have our secured database server, so it’s time to start building the API.


## 2. Flask

#### What Is A Web API?
   A Web API (Application Programming Interface) allows you to serve data over the web, typically in JSON or XML format. Generally, this is done by exposing endpoints to make requests.
   Flask is a light-weight web framework. With Flask, you get to pick-and-choose what components and extension needed for your site. I like this aspect since the modular nature allows you to build everything up, without too much clutter.

  The main Flask extensions we will use are Flask MongoEngine and Flask RESTful. The first will let us build Classes as templates for our data and the latter is designed for building an API, and makes the process simpler.

  Additionally, we will use JWT-Extended and BCrypt, but I will cover those later.

  Create a clean virtual environment and get Flask.
  
  Install required packages:
  
    pip install Flask
    pip install flask-mongoengine
    pip install flask-bcrypt
    pip install flask-restful
    pip install flask-jwt-extended
  
#### JWT Token:  
  Authentication allows users to log in before accessing the data. We have two routes included, one for singing up and another for logging in. The SignUpApi Class is the same as a POST request to the User model, except it doesn’t require prior authentication (since the user hasn’t signed up yet).

A couple of notes about the coding of these classes:

  * The post() method is static since the class has no special context, such as requiring JSON Web Tokens. 
 
  * The get, post, put, and delete return type is Response, this is a class that Flask inherits from Werkzeug, but it isn’t necessary to understand the underlying mechanics. It just handles HTTP communication stuff. Flask takes care of this when you pass a dictionary object into flask.jsonify. Feel free to see the documentation for more info.
  
  * If the asterisks in Users() is new to you, don’t worry it is just a concise way of passing arguments into a Class or method using a dictionary.
  
  * The LoginApi checks the given password to see if it matches and then creates web tokens if successful. These tokens allow a user to continue using the API without the need to login for each request. A refresh token is generated, but not used in this tutorial. This would allow a user to continue their session after the token expires.

### Note:
   Make sure mongoDB is running and change the login details, DB name, authentication_source and JWT_SECRET_KEY in default_config in app.py file.
   
        # default mongodb configuration
        default_config = {
                'MONGODB_SETTINGS': {
                            'db': 'test_db',
                            'host': 'localhost',
                            'port': 27017,
                            'username': 'admin',
                            'password': 'password',
                            'authentication_source': 'admin'
                            },
                'JWT_SECRET_KEY': 'changeThisKeyFirst'}

### Run app.py

  web application will be hosted on localhost

  
