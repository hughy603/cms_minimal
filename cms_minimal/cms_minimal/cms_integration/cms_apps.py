from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _


class Apphook(CMSApp):
    app_name = "cms_integration"
    name = _("Cms Integration")

    #def get_urls(self, page=None, language=None, **kwargs):
    #    return ["polls.urls"]

apphook_pool.register(Apphook)  # register the application
