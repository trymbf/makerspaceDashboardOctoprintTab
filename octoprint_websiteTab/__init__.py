import octoprint.plugin

class WebsiteTabPlugin(octoprint.plugin.StartupPlugin,
                       octoprint.plugin.TemplatePlugin,
                       octoprint.plugin.SettingsPlugin,
                       octoprint.plugin.AssetPlugin,
                       octoprint.plugin.SimpleApiPlugin,
                       octoprint.plugin.RestartNeedingPlugin):
    
    def on_after_startup(self):
        self._logger.info("Website (more: %s)" % self._settings.get(["url"]) + "tabname: " + self._settings.get(["tabname"]))

    def get_settings_defaults(self):
        return dict(url="https://en.wikipedia.org/wiki/3D_printing", tabname = "Website")
    
    def get_template_configs(self):
        return [
            dict(type="tab", custom_bindings=False, name=self._settings.get(["tabname"])),
            dict(type="settings", custom_bindings=False)
        ]

    def get_assets(self):
        return dict(
            js=["js/websiteTab.js"],
            css=["css/websiteTab.css"]
        )

    def on_settings_save(self, data):
        old_url = self._settings.get(["url"])
        octoprint.plugin.SettingsPlugin.on_settings_save(self, data)
        new_url = self._settings.get(["url"])
        
        if old_url != new_url:
            self._plugin_manager.send_plugin_message(self._identifier, dict(type="info", autoClose=True, msg="Site reload required for URL change to take effect."))
            self._plugin_manager.send_plugin_message(self._identifier, dict(type="client:reload"))

__plugin_name__ = "Website Tab"
__plugin_pythoncompat__ = ">=3.7,<4"
__plugin_implementation__ = WebsiteTabPlugin()
