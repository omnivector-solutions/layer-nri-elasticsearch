# nri-elasticsearch

This charm Installs and configures the newrelic-infra agent alongside the
nri-elasticsearch host integration.


## Usage
To deploy this charm, configure the `license_key` and relate to an application exposing
the `juju-info` provides endpoint.

```bash
juju deploy cs:~omnivector/nri-elasticsearch --config license_key=<newrelic_key>
juju relate nri-elasticsearch <application>
```

This charm will set a blocked status in the case the `license_key` is not set.

To configure the `license_key` following deployment use `juju config`.
```bash
juju config nri-elasticsearch license_key=<newrelic_key>
```

To remove the `newrelic-infra` agent and `nri-elasticsearch` host integration, simply remove the `elasticsearch-nri` application or unit.


#### License
* AGPLv3 (see `LICENSE` file in this directory).
