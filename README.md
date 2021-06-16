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

### Documentation:

```python
ccould.login()
```
Logs in to Confluent Cloud account enabling usage of ccloud.

```python
ccloud.logut()
```
Logs out from Confluent Cloud account.

```python
ccloud.list_envs()
```
Lists all available Confluent Cloud environments.

```python
ccloud.list_clusters()
```
Lists all available clusters.

```python
ccloud.use_env(name: str)
```
Start using environment by given name.

```python
ccloud.use_cluster(name: str)
```
Start using cluster by given name.

```python
ccloud.create_topic(
    name: str,
    cluster: str,
    number_of_partitions: int = 3,
    config: Optional[Dict] = None)
```
Creates topic with given name on a given cluster.
Number of partitions can be provided.
Config can be provided to fulfill the need of less used parameters: https://docs.confluent.io/ccloud-cli/current/command-reference/kafka/topic/ccloud_kafka_topic_create.html

```python
ccloud.delete_topic(name: str, cluster: str)
``` 
Deletes topic with given name on a given cluster.

```python
ccloud.create_service_account(name: str, description: str)
```
Creates a service account with a given name and description.

```python
ccloud.list_service_accounts()
```
Lists all available service accounts

```python
ccloud.delete_service_account(name: str)
```
Deletes a service account by name.

```python
ccloud.create_topic_acl(
    service_account: str,
    topic: str,
    operation: str,
    prefix: bool = False)
```
Creates an ACL for a service account to perform given operation a topic.
Operation might be e.g. `READ`, `WRITE`, `DESCRIBE`
Set `prefix=True` if you want to give access to a family of topics.

```python
ccloud.delete_topic_acl(
    service_account: str,
    topic: str,
    operation: str,
    prefix: bool = False)
```
Deletes operation's ACL for a service account to a topic.

```python
ccloud.create_consumer_group_acl(
    service_account: str,
    consumer_group: str,
    operation: str,
    prefix: bool = False)
```
Creates ACL for a consumer group like `create_topic_acl` for topic.

```python
ccloud.delete_consumer_group_acl(
    service_account: str,
    consumer_group: str,
    operation: str,
    prefix: bool = False)
```
Deletes operation's ACL for a service account to a consumer group.

[commit]: https://github.com/saucelabs/py-ccloud/commit/HEAD
[release]: https://github.com/saucelabs/py-ccloud/releases/latest

[commit badge]: https://img.shields.io/github/last-commit/saucelabs/py-ccloud.svg
[release badge]: https://img.shields.io/github/release/saucelabs/py-ccloud.svg

### Contributing

We would love to have outside contributors chiming in supporting us finishing this. Please have a look at our [contribution guidelines](https://github.com/saucelabs/py-ccloud/blob/master/CONTRUBUTING.md).
