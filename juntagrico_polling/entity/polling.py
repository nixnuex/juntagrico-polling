from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.models import User


class Poll(models.Model):
    '''
    Public poll definition
    '''
    title = models.CharField(_('Title'), max_length=100, blank=False)
    question = models.TextField(_('Question'), max_length=500, blank=False)
    description = models.TextField(_('Description'), max_length=1000, blank=True, default='')
    open_date = models.DateTimeField(_('Open Date'))
    close_date = models.DateTimeField(_('Close Date'))
    display_order = models.IntegerField(_('Display Order'), null=False, default=0)
    active = models.BooleanField(_('Active'), default=True)
    add_menu_link = models.BooleanField(_('Add Link to Main Menu'), default=True)

    class Meta:
        permissions = (('can_see_poll_results', _('Can see poll results')),)

class Vote(models.Model):
    '''
    Single vote by a member
    '''
    YES = 1
    NO = 0
    ABSTENTION = 2
    CHOICE = (
        (YES, _('Yes')),
        (NO, _('No')),
        (ABSTENTION, _('ABSTENTION')),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    poll = models.ForeignKey(Poll, on_delete=models.PROTECT)
    choice = models.PositiveSmallIntegerField(choices=CHOICE)
    last_update = models.DateTimeField(_('Last Update'), auto_now=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'poll'], name='unique user vote')
        ]
