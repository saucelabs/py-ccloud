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

Login and execute action:
```python
import ccloud
ccloud.login()
ccloud.list_clusters()
ccloud.create_topic("myTopic", "myCluster")
```

[commit]: https://github.com/saucelabs/py-ccloud/commit/HEAD
[release]: https://github.com/saucelabs/py-ccloud/releases/latest

[commit badge]: https://img.shields.io/github/last-commit/saucelabs/py-ccloud.svg
[release badge]: https://img.shields.io/github/release/saucelabs/py-ccloud.svg

## Contributing

We would love to have outside contributors chiming in supporting us finishing this. Please have a look at our [contribution guidelines](https://github.com/saucelabs/py-ccloud/blob/master/CONTRUBUTING.md).
