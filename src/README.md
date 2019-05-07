# newrelic-infra layer

This layer Installs and configures the newrelic-infra agent with the nri-elasticsearch package

## Usage
  ```
    juju deploy cs:~rr-pdl/nri-elasticsearch
    juju config nri-elasticsearch license_key=<newrelic_key>
    juju relate nri-elasticsearch <application>
  ```
