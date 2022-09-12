# Flask Hexagonal
A Flask RESTful project inspired by [Hexagonal Architecture](https://netflixtechblog.com/ready-for-changes-with-hexagonal-architecture-b315ec967749). The project contains examples through various api implementations.


# Setup
## Environment
```
Python 3.8.9

# Create venv
python3.8 -m venv venv

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


# Additional:
  - More configurable queue based logger settings with multipurpose handlers
  

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
  
TODO:

- distribution and packaging (wheel)
- setup for environment specific case
- code test
- code coverage
- code linting



