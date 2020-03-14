from django.utils import timezone
from juntagrico.entity.member import Member
from juntagrico_polling.entity.polling import Poll
from juntagrico_polling.entity.polling import Vote


class PollingDao:

    @staticmethod
    def is_member_with_shares(user):
        member = Member.objects.get(user=user)
        allow_vote = False
        if member and member.is_cooperation_member == True:
            allow_vote = True
        return allow_vote

    @staticmethod
    def all_polls_ordered():
        return Poll.objects.order_by('display_order')

    @staticmethod
    def active_polls_ordered():
        return Poll.objects.filter(active=True).filter(close_date__gte=timezone.now()).order_by('display_order')

    @staticmethod
    def active_polls_menu_show():
        return Poll.objects.filter(active=True).filter(close_date__gte=timezone.now()).filter(add_menu_link=True)

    @staticmethod
    def votes_from_user(user):
        return Vote.objects.filter(user=user)

    @staticmethod
    def votes_for_poll(poll):
        return Vote.objects.filter(poll=poll)
