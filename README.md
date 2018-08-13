# Github Crawler

## Requirements
For the purpous of this task it is required to have BeautifulSoup 4 for Python 3 installed.

* `apt-get install python3-bs4`


## Description
This project includes both the main GitHub Crawler and the Extra information specified as optional. 


### Expected results: Example 1

Keep in mind the input can be different when executing since the proxies can be different. To change the input, change the file example1.json.
```shell
{
  "keywords": [
    "openstack",
    "nova",
    "css"
  ],
  "proxies": [
    "202.91.71.162:32260",
    "190.121.231.243:53281"
  ],
  "type": "Repositories"
}
```
The extras will also be appearing in the output so the final expected answer would be:
```json
[
  {
    "url": "https://github.com/atuldjadhav/DropBox-Cloud-Storage", 
    "extra": {
      "owner": "atuldjadhav",
      "language_stats": {
        "CSS": "52.0%", 
        "JavaScript": "47.2%", 
        "HTML": "0.8%"
      } 
    }
  }
]
```

### Expected results: Example 2

Keep in mind the input can be different when executing since the proxies can be different. To change the input, change the file example2.json.
```shell
{
  "keywords": [
    "python",
    "django-rest-framework",
    "jwt"
  ],
  "proxies": [
    "202.91.71.162:32260",
    "191.252.196.133:8080"
  ],
  "type": "Repositories"
}
```

The extras will also be appearing in the output so the final expected answer would be:
```json
[
  {
    "url": "https://github.com/GetBlimp/django-rest-framework-jwt",
    "extra": {
      "owner": "GetBlimp"},
      "language_stats": {
        "Python": "100.0%"
      } 
  }, 
  {
    "url": "https://github.com/lock8/django-rest-framework-jwt-refresh-token",
    "extra": {
      "owner": "lock8"}, 
      "language_stats": {
        "Python": "96.6%", 
        "Makefile": "3.4%"
      } 
  }, 
  {
    "url": "https://github.com/pyaf/djangular",
    "extra": {
      "owner": "pyaf"}, 
      "language_stats": {
        "JavaScript": "99.0%", 
        "Other": "1.0%"
      } 
  }, 
  {
    "url": "https://github.com/City-of-Helsinki/tunnistamo",
    "extra": {
      "owner": "City-of-Helsinki"}, 
      "language_stats": {
        "HTML": "1.6%", 
        "Python": "97.3%", 
        "CSS": "1.1%"
      }
  },
  {
    "url": "https://github.com/chessbr/rest-jwt-permission",
    "extra": {
      "owner": "chessbr"}, 
      "language_stats": {
        "Python": "100.0%"
      }
  }, 
  {
    "url": "https://github.com/Firok/RestApp",
    "extra": {
      "owner": "Firok"}, 
      "language_stats": {
        "HTML": "2.3%", 
        "Python": "97.7%"
      }
  }, 
  {
    "url": "https://github.com/vaibhavkollipara/ChatroomApi",
    "extra": {
      "owner": "vaibhavkollipara"}, 
      "language_stats": {
        "Python": "100.0%"
      }
  }, 
  {
    "url": "https://github.com/Foxfix/api_client",
    "extra": {
      "owner": "Foxfix"}, 
      "language_stats": {
        "HTML": "3.1%", 
        "Python": "96.9%"
      } 
  }
]
```

## Important


* The speed and performance of the Crawler might be affected by the proxy and the conention conditions to it.
* If a proxy fails to connect several times it might be needed to check the availavility or change the proxy.
* You can change search keywords, proxies and types supported in the json example files ("Repositories", "Wikis", "Issues").
* Extra information will only be shown for the repositories, so the expected output will be diferent than the previously shown.

## Usage

Given an example file (ie. example1.json) a normal command line to execute the program would be:

* `python3 main.py example1.json`

For the user to be able to se specifically each step the crawler is taking and error handling, "--INFO" is expected to be used at the end of the command line.

* `python3 main.py example1.json --INFO`