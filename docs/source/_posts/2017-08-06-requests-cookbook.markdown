---
layout: post
title: "requests cookbook"
date: 2017-08-06 23:17:25 -0700
comments: true
categories: 
- Python
---

`requests` module is a simple HTTP client library in Python.

<!-- more -->

### Example: BART parking

The problem is discussed [here](http://tdongsi.github.io/blog/2016/10/30/automated-downloading-bart-parking-permits/).
The `requests`'s code snippets can be found [here](https://github.com/tdongsi/bart-parking/blob/develop/python/bart.py).

Featuring:

* Login with CSRF protection (with POST)
* Cookie retrieval and usage
* Binary download and saved to file.

``` python Different payload for POST
# POST /bart/users/login/ HTTP/1.1
# Content-Type: application/x-www-form-urlencoded
HEADERS = {"Referer": "https://www.select-a-spot.com/bart/"}
params = {"username": username,
            "password": password,
            "csrfmiddlewaretoken": r.cookies["csrftoken"],
            "login": "Login"}
r = s.post("https://www.select-a-spot.com/bart/users/login/", headers=HEADERS, data=params, allow_redirects=False)

# POST /kafka/topic HTTP/1.1
# Content-Type: application/json
my_data = {'name': IOT_TOPIC, 'type': '/types/com.prod.emp'}
my_header = {'Accept': 'application/json', 'Content-Type': 'application/json'}

logger.info('POST: %s', TOPIC_ENDPOINT)
r = s.post(TOPIC_ENDPOINT, headers=my_header, data=json.dumps(my_data), cert=KAFKA_CERTS)
```

Note that `json.dumps` is required for POST-ing JSON data. The typical service response:

``` plain Error message
"exception":"org.springframework.http.converter.HttpMessageNotReadableException","message":"Bad Request"
```

### SSL authentication

You can specify your certificate and private key in `cert=(my_cert, my_key)` as a method parameter.
The certificate authority can be optionally specified (`s.verify = MY_CA`) or not (`s.verify = False`).

``` python SSL authentication
def test_kafka(my_cert, my_key):
    """ Top level function to test_kafka.

    :param my_cert: path to certificate.
    :param my_key: path to private key corresponding to the certificate.
    :return:
    """

    ZOOKEEPER_EP = 'https://kafka-prd.corp.net:9090'
    IOT_NAMESPACE = 'test'
    MY_CA = 'download/ca.crt'

    s = requests.Session()
    s.verify = MY_CA

    def test_namespace():
        """ Test querying kafka namespace.

        Basically: curl -k -E ./kafka.p12:password "https://kafka.prd:9090/namespaces/test"
        """
        NAMESPACE_PATH = '/namespaces'
        endpoint = ZOOKEEPER_EP + NAMESPACE_PATH + '/' + IOT_NAMESPACE

        logger.info('GET: %s', endpoint)
        r = s.get(endpoint, cert=(my_cert, my_key))

        logger.debug("Response: %s", r.text)
        data = json.loads(r.text)
        # print json.dumps(data, indent=4)
        # Print namespace
        logger.info("ID: %s", data['id'])
        pass

    test_namespace()
```
### Unit testing

You can do unit testing by using `requests-mock` package.

``` plain Installation
# Only required for Python 2. Mock is part of Python 3.
pip install -U mock

pip install requests-mock
```

``` python Example of mocking
    @requests_mock.mock()    
    def test_get_env_status(self, m):
        #Test status code 400 returns False
        m.get(self.status_endpoint, status_code=404)
        with mock.patch.dict(os.environ,{'username':'mytempuser', 'password':'temppass'}):
            self.assertEquals(FlowSnakeEnvironment.get_env_status(self.fsenv_name), None)
```

#### References

* [PDF doc](https://media.readthedocs.org/pdf/requests-mock/latest/requests-mock.pdf)