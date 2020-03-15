from django import template

from juntagrico_polling.dao.pollingdao import PollingDao

register = template.Library()


@register.simple_tag
def user_menu():
    return PollingDao.active_polls_menu_show()
