from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from juntagrico.views import get_menu_dict
from juntagrico_polling.entity.polling import Poll
from juntagrico_polling.entity.polling import Vote
from juntagrico_polling.dao.pollingdao import PollingDao


@login_required
def poll(request, poll_id=None, choice=None):
    renderdict = get_menu_dict(request)
    allowed_to_vote = PollingDao.is_member_with_shares(request.user)
    if allowed_to_vote:
        if poll_id is not None and 0 <= choice <= 2:
            submit_vote(request.user, poll_id, choice)

        active_polls = PollingDao.active_polls_ordered()
        user_votes = PollingDao.votes_from_user(request.user)
        for thispoll in active_polls:
            vote = user_votes.filter(poll=thispoll)
            if vote:
                vote = vote.get()
                thispoll.choice = vote.choice
            else:
                thispoll.choice = None
        renderdict.update({
            'polls': active_polls,
            'allowed_to_vote': True,
        })
    return render(request, "jp/polling.html", renderdict)


def submit_vote(user, poll_id, choice):
    if 0 <= choice <= 2:
        try:
            poll_selected = PollingDao.active_polls_ordered().get(id=poll_id)
            if poll_selected and \
                    (choice <= 1 or poll_selected.allow_abstention):
                Vote.objects.update_or_create(
                    user=user, poll=poll_selected, defaults={'choice': choice})
        except Poll.DoesNotExist:
            pass


@permission_required('juntagrico_polling.can_see_poll_results')
def results(request):
    polls = PollingDao.all_polls_ordered()
    for thispoll in polls:
        user_votes = PollingDao.votes_for_poll(thispoll)
        thispoll.yes = sum(vote.choice == 1 for vote in user_votes)
        thispoll.no = sum(vote.choice == 0 for vote in user_votes)
        thispoll.abstention = sum(vote.choice == 2 for vote in user_votes)
        thispoll.votes = user_votes.count()
    renderdict = get_menu_dict(request)
    renderdict.update({
        'polls': polls,
    })
    return render(request, "jp/results.html", renderdict)
