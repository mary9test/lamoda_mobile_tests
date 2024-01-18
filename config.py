import os
from appium.options.android import UiAutomator2Options
from pydantic import BaseModel
from lamoda_mobile_tests_framework.utils import helpers


class Settings(BaseModel):
    context: str
    login: str = os.getenv('USER_NAME')
    password: str = os.getenv('ACCESS_KEY')
    remote_url: str = os.getenv('BROWSER_URL')
    udid: str = os.getenv('UDID')
    app: str = os.getenv('APP')
    platformVersion: str = os.getenv('PLATFORM_VERSION')
    deviceName: str = os.getenv('DEVICE_NAME')
    projectName: str = os.getenv('PROJECT_NAME')
    buildName: str = os.getenv('BUILD_NAME')
    sessionName: str = os.getenv('SESSION_NAME')

    def to_driver_options(self, context):
        options = UiAutomator2Options()

        if context == 'local_emulator':
            options.set_capability('app', helpers.abs_path(self.app))
            options.set_capability('udid', self.udid)

        if context == 'bstack':
            options.set_capability('app', self.app)
            options.set_capability('platformVersion', self.platformVersion)
            options.set_capability('deviceName', self.deviceName)
            options.set_capability(
                'bstack:options', {
                    'buildName': self.buildName,
                    'sessionName': self.sessionName,
                    'userName': self.login,
                    'accessKey': self.password,
                },
            )

        return options


settings = Settings(context='bstack')
