from menus.base import Menu, NavigationNode
from menus.menu_pool import menu_pool
from django.utils.translation import ugettext_lazy as _

class TestMenu(Menu):

    def get_nodes(self, request):
        nodes = []
        n = NavigationNode(_('sample root page'), "/", 1)
        n2 = NavigationNode(_('sample my profile page'), "/hello/world/", 2, 1)
        nodes.append(n)
        nodes.append(n2)
        return nodes

menu_pool.register_menu(TestMenu)
