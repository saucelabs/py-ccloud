# py-ccloud

![Language](https://img.shields.io/badge/language-python-green.svg)
[![Latest Release][release badge]][release]
[![Last Commit][commit badge]][commit]

Simple Python library wrapping the Confluent Cloud CLI

### Installation

```bash
pip install py-ccloud
```

### Usage example

Setup your Confluent Cloud credentials in environment variables:
```bash
export CCLOUD_EMAIL=...
export CCLOUD_PASSWORD=...
```

Login and execute action, e.g:
```python
import ccloud

ccloud.login()
ccloud.list_clusters()
ccloud.create_topic("myTopic", "myCluster")
```
