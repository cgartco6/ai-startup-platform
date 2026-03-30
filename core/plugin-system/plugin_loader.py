import importlib

class PluginLoader:

    def load(self, plugin_name):

        module = importlib.import_module(plugin_name)

        return module.Plugin()
