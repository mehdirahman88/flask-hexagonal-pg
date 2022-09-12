Additional Package (If needed):
 - common
 - dto
 - mapper
 - middleware
 - validator
 - util
 - helper

Directory (Initial):

```angular2html
./src
├── main
│   ├── adapter ------------------ implementations of internal.ports
│   ├── api ---------------------- implementations of api with framework
│   │   └── controller
│   └── internal
│       ├── model
│       ├── port ----------------- interfaces for the service dependencies
│       │   └── repository
│       └── service -------------- interfaces and implementations of service
└── tests

```
