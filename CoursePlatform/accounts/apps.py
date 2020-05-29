from django.apps import AppConfig


class AccountsConfig(AppConfig):
    """
    App configurations for Accounts app
    """
    name = 'accounts'

    def ready(self):
        """
        Imports signals.py to activate signals when it is needed
        :return:
        """
        import accounts.signals
