# Github Crawler

## Description

### Example 1
Input:
```shell
{
  "keywords": [
    "openstack",
    "nova",
    "css"
  ],
  "proxies": [
    "194.126.37.94:8080",
    "13.78.125.167:8080"
  ],
  "type": "Repositories"
}
```
Answer:
```json
[
  {
    "url": "https://github.com/atuldjadhav/DropBox-Cloud-Storage"
  }
]
```

### Example 2
Input:
```shell
{
  "keywords": [
    "python",
    "django-rest-framework",
    "jwt"
  ],
  "proxies": [
    "194.126.37.94:8080",
    "13.78.125.167:8080"
  ],
  "type": "Repositories"
}
```

Answer:
```json
[
  {
    "url": "https://github.com/GetBlimp/django-rest-framework-jwt"
  },
  {
    "url": "https://github.com/lock8/django-rest-framework-jwt-refresh-token"
  },
  {
    "url": "https://github.com/City-of-Helsinki/tunnistamo"
  },
  {
    "url": "https://github.com/chessbr/rest-jwt-permission"
  },
  {
    "url": "https://github.com/rishabhiitbhu/djangular"
  },
  {
    "url": "https://github.com/vaibhavkollipara/ChatroomApi"
  }
]
```

### Optional
Input:
```shell

```

Answer:
```json

```

## Deploy instructions


## Usage


### Example 1
* `python3 main.py example1.json`
* `python3 main.py example2.json`

* `python3 main.py example1.json --INFO`
* `python3 main.py example1.json --DEBUG`