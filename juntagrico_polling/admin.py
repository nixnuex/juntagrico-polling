from django.contrib import admin

from juntagrico_polling.entity.polling import Poll
from juntagrico_polling.entity.polling import Vote


class PollAdmin(admin.ModelAdmin):
    list_display = ('id','title','close_date')
    search_fields = ('id','title','close_date')

class VoteAdmin(admin.ModelAdmin):
    list_display = ('user', 'poll', 'choice')
    search_fields = ('user', 'poll', 'choice')

admin.site.register(Poll, PollAdmin)
admin.site.register(Vote, VoteAdmin)
