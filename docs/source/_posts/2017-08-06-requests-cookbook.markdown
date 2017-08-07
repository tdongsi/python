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

### SSL authentication

``` python SSL authentication
def test_kafka(my_cert, my_key):
    """ Top level function to test_kafka.

    :param my_cert: path to certificate.
    :param my_key: path to private key corresponding to the certificate.
    :return:
    """

    ZOOKEEPER_EP = 'https://kafka-prd.corp.net:9090'
    IOT_NAMESPACE = 'test'
    SALESFORCE_CA = 'download/ca.crt'

    s = requests.Session()
    s.verify = SALESFORCE_CA

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
