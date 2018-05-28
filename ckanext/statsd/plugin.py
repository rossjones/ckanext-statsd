import statsd
from wsgi_statsd import StatsdTimingMiddleware

import ckan.plugins as p
import ckan.plugins.toolkit as toolkit


class StatsdPlugin(p.SingletonPlugin):
    p.implements(p.IConfigurer)
    p.implements(p.IMiddleware)
    p.implements(p.IDomainObjectModification)

    PREFIX = ""
    HOST = ""
    POST = ""
    LOG_TIMES = True

    # IConfigurer
    def update_config(self, config):
        StatsdPlugin.PREFIX = config.get('ckanext.statsd.prefix', '')
        StatsdPlugin.HOST = config.get('ckanext.statsd.host', '')
        StatsdPlugin.PORT = config.get('ckanext.statsd.port', 8125)
        StatsdPlugin.LOG_TIMES = toolkit.asbool(config.get('ckanext.statsd.logtimes', True))

        self.client =statsd.StatsClient(
            host=StatsdPlugin.HOST, port=StatsdPlugin.PORT,
            prefix=StatsdPlugin.PREFIX, ipv6=False
        )

    def make_middleware(self, app, config):
        if not StatsdPlugin.LOG_TIMES or not StatsdPlugin.HOST:
            return app

        application = StatsdTimingMiddleware(app, self.client)
        return application

    def notify(self, entity, operation):
        key = 'ckan.dataset.{}'.format(operation)
        self.client.incr(key, count=1)
