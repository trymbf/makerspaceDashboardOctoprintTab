import octoprint.plugin

class MakerspaceDashboardPlugin(octoprint.plugin.StartupPlugin,
                       octoprint.plugin.TemplatePlugin,
                       octoprint.plugin.SettingsPlugin,
                       octoprint.plugin.AssetPlugin):
    def on_after_startup(self):
        self._logger.info("Dashboard (more: %s)" % self._settings.get(["url"]))

    def get_settings_defaults(self):
        return dict(url="https://tbf3d.com/db")
    
    def get_template_configs(self):
        return [dict(type="settings", custom_bindings=False)]

    def get_assets(self):
        return dict(
            js=["js/makerspaceDashboard.js"],
            css=["css/makerspaceDashboard.css"]
        )

__plugin_name__ = "Makerspace Dashboard Tab"
__plugin_pythoncompat__ = ">=3.7,<4"
__plugin_implementation__ = MakerspaceDashboardPlugin()
