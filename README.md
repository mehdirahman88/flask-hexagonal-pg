# Flask Hexagonal
A Flask RESTful project inspired by [Hexagonal Architecture](https://netflixtechblog.com/ready-for-changes-with-hexagonal-architecture-b315ec967749). 
The project will contain examples through various api implementations.


# Setup
## Environment
```
Python 3.9.6

# Create venv
python3.9 -m venv venv

source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```
## Environment Variables
```
FLASK_ENV                        # instance name
FLASK_APP                        # module containing application object
```
## Run Application:
```
source .flaskenv
flask run -h 0.0.0.0 -p 5500     # run application with development server
```

# Directory:
```angular2html
./src
├── main
│   ├── adapter ------------------ implementation of internal.port
│   ├── api ---------------------- implementation of api with framework. depends on service interface.
│   │   ├── local
│   │   │   └── controller
│   │   └── v1
│   │       └── controller
│   ├── config ------------------- basic default application config
│   └── internal
│       ├── model
│       ├── port ----------------- interface for service dependencies
│       │   └── repository
│       └── service -------------- interface and implementation of service/business logic
└── test


```


# Example Additional Package / Tools (If needed):
```
  - common
  - dto
  - mapper
  - middleware 
  - validator
  - util
  - helper
  - cli tool 
    - manager.py
```

# Note:
  - Be aware of python dependency issues
    - Flask, Flask-Apispec and Swagger
      - [Github flask-apispec issue](https://github.com/jmcarp/flask-apispec/issues/235)
      - [Flask and Flask-apispec issue thread link](https://stackoverflow.com/questions/73221330/attributeerror-module-flask-views-has-no-attribute-methodviewtype)
      - flask-apispec 0.11.0 breaks flask 2.x -> flask-apispec 0.11.2 fixes it -> flask-apispec 0.11.2 breaks swagger
      - Flask==2.1.3 (used)
      - flask-apispec 0.11.0 (used)
  - [Flask project changes](https://flask.palletsprojects.com/en/2.2.x/changes/)
  - [Browser blocks certain ports](https://stackoverflow.com/questions/4313403/why-do-browsers-block-some-ports/22622633#22622633)

# Resources:
  - More configurable queue based logger settings with multipurpose handlers
    - [Blog: How to use python logging queue handler with dict config](https://rob-blackbourn.medium.com/how-to-use-python-logging-queuehandler-with-dictconfig-1e8b1284e27a)
    - [Logging Extras: A collection of various python logging extensions](https://github.com/zobayer1/logging-extras)
  - Black Formatter
    - [Pycharm and Black Configuration](https://akshay-jain.medium.com/pycharm-black-with-formatting-on-auto-save-4797972cf5de)
      - Uncheck `Auto-save edited files to trigger the watcher` mentioned here
      - Check on-save action in the editor or run `black .`
  - Helpful Blogs/Repos
    - [Netflix Blog: Ready for changes with Hexagonal Architecture](https://netflixtechblog.com/ready-for-changes-with-hexagonal-architecture-b315ec967749)
    - [Repo: flask-restful-boilerplate](https://github.com/zobayer1/flask-restful-boilerplate)
    - [Blog: Hexagonal Architecture in Python](https://douwevandermeij.medium.com/hexagonal-architecture-in-python-7468c2606b63)
      - [Repo](https://github.com/douwevandermeij/voting-system)
    - [Hexagonal Architecture in Python using Flask and SqlAlchemy](https://alexgrover.me/posts/python-hexagonal-architecture)
      - [Repo](https://github.com/alex-grover/hexagonal-architecture-python)
    - [Repo: Python API example (SOLID & Hexagonal Arch.)](https://github.com/serfer2/flask-hexagonal-architecture-api)


