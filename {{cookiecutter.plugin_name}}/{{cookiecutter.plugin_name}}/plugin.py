import climmob.plugins as plugins
import climmob.plugins.utilities as u
#from .views import MyPublicView, MyPrivateView
import sys
import os


class {{ cookiecutter.plugin_name }}(plugins.SingletonPlugin):
    plugins.implements(plugins.IRoutes)
    plugins.implements(plugins.IConfig)
    plugins.implements(plugins.ITranslation)

    def before_mapping(self, config):
        # We don't add any routes before the host application
        return []

    def after_mapping(self, config):
        # We add here a new route /json that returns a JSON
        custom_map = []
        """custom_map = [
            u.addRoute(
                "plugin_mypublicview", "/mypublicview", MyPublicView, "json"
            ),
            u.addRoute(
                "plugin_myprivateview",
                "/user/{userid}/myprivateview",
                MyPrivateView,
                "private.jinja2",
            ),
        ]"""

        return custom_map

    def update_config(self, config):
        # We add here the templates of the plugin to the config
        u.addTemplatesDirectory(config, "templates")

    def get_translation_directory(self):
        module = sys.modules["{{ cookiecutter.plugin_name }}"]
        return os.path.join(os.path.dirname(module.__file__), "locale")

    def get_translation_domain(self):
        return "{{ cookiecutter.plugin_name }}"
