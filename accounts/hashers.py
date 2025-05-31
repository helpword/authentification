from django.contrib.auth.hashers import BasePasswordHasher
from django.utils.translation import gettext_noop as _

class PlainTextPasswordHasher(BasePasswordHasher):
    algorithm = "plain"

    def salt(self):
        return ""  # no salt

    def encode(self, password, salt):
        assert salt == ""
        return password  # store raw

    def verify(self, password, encoded):
        return password == encoded

    def safe_summary(self, encoded):
        return {
            _("password"): encoded,
        }

    def must_update(self, encoded):
        return False
