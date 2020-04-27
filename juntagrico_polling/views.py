from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from juntagrico.views import get_menu_dict
from juntagrico_polling.entity.polling import Vote
from juntagrico_polling.dao.pollingdao import PollingDao


@login_required
def poll(request, poll_id=None, choice=None):
    renderdict = get_menu_dict(request)
    if PollingDao.is_member_with_shares(request.user):
        if poll_id is not None and choice is not None and 0 <= choice <= 2:
            poll = PollingDao.active_polls_ordered().get(id=poll_id)
            if poll and (choice <= 1 or poll.allow_abstention):
                Vote.objects.update_or_create(
                    user=request.user, poll=poll, defaults={'choice': choice})

        polls = PollingDao.active_polls_ordered()
        user_votes = PollingDao.votes_from_user(request.user)
        for thispoll in polls:
            vote = user_votes.filter(poll=thispoll)
            if vote:
                vote = vote.get()
                thispoll.choice = vote.choice
            else:
                thispoll.choice = None
        renderdict.update({
            'polls': polls,
        })
    else:
        renderdict.update({
            'forbidden_to_vote': True,
        })
    return render(request, "jp/polling.html", renderdict)


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
