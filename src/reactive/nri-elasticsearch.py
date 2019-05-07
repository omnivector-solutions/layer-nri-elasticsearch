from charms import (
    apt
)

from charmhelpers.core.hookenv import (
    config,
    status_set,
)

from charms.reactive import (
    when,
    when_not,
    hook,
    set_flag,
    clear_flag,
)

from charmhelpers.core.host import (
    service_restart,
)

from charmhelpers.core.templating import (
    render
)

import os


TEMPLATE_FILE = "elasticsearch-config.tmpl"
CONFIG_FILE = "/etc/newrelic-infra/integrations.d/elasticsearch-config.yml"


@when('newrelic-infra.ready')
@when_not('nri-elasticsearch.configured')
def configure():
    render(source=TEMPLATE_FILE,
           target=CONFIG_FILE,
           context={
               'command': config('command'),
               'cluster_environment': config('cluster_environment'),
               'config_path': config('config_path'),
               'hostname': config('hostname'),
               'local_hostname': config('local_hostname'),
               'username': config('username'),
               'password': config('password'),
               'port': config('port'),
               'timeout': config('timeout'),
               'indices_regex': config('indices_regex'),
               'collect_indices': config('collect_indices'),
               'collect_primaries': config('collect_primaries'),
           })
    set_flag('nri-elasticsearch.configured')

    service_restart('newrelic-infra')
    status_set('active', "nri-elasticsearch ready")


@when('config.changed')
def reconfigure():
    clear_flag('nri-elasticsearch.configured')


@when('nri-elasticsearch.configured')
def verify_config_exists():
    if not os.path.isfile(CONFIG_FILE):
        clear_flag('nri-elasticsearch.configured')


@hook('stop')
def uninstall():
    status_set('maintenance', "Removing nri-elasticsearch")

    if os.path.isfile(CONFIG_FILE):
        os.remove(CONFIG_FILE)

    apt.purge(['nri-elasticsearch'])
