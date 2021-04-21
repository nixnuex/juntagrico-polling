from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required, permission_required
from juntagrico_polling.entity.polling import Poll
from juntagrico_polling.entity.polling import Vote
from juntagrico_polling.dao.pollingdao import PollingDao


@login_required
def poll_list(request):
    allowed_to_vote = user_allowed_to_vote(request.user)
    if allowed_to_vote:
        active_polls = PollingDao.active_polls_ordered()
        user_votes = PollingDao.votes_from_user(request.user)
        for thispoll in active_polls:
            vote = user_votes.filter(poll=thispoll)
            if vote:
                vote = vote.get()
                thispoll.choice = vote.choice
            else:
                thispoll.choice = None
        renderdict = {
            'polls': active_polls,
            'allowed_to_vote': True,
        }
    return render(request, "jp/polling.html", renderdict)


def submit_vote(request, poll_id=None, choice=None):
    allowed_to_vote = user_allowed_to_vote(request.user)
    redirect_url = reverse('polling:list')
    if allowed_to_vote and poll_id is not None and 0 <= choice <= 2:
        try:
            poll_selected = PollingDao.active_polls_ordered().get(id=poll_id)
            if poll_selected and \
                    (choice <= 1 or poll_selected.allow_abstention):
                Vote.objects.update_or_create(
                    user=request.user, poll=poll_selected,
                    defaults={'choice': choice})
                redirect_url += '#poll_' + str(poll_id)
                return redirect(redirect_url)
        except Poll.DoesNotExist:
            pass
    return redirect(redirect_url)


def user_allowed_to_vote(user):
    allowed_to_vote = PollingDao.is_member_with_shares(user)
    return allowed_to_vote


@permission_required('juntagrico_polling.can_see_poll_results')
def results(request):
    polls = PollingDao.all_polls_ordered()
    for thispoll in polls:
        user_votes = PollingDao.votes_for_poll(thispoll)
        thispoll.yes = sum(vote.choice == 1 for vote in user_votes)
        thispoll.no = sum(vote.choice == 0 for vote in user_votes)
        thispoll.abstention = sum(vote.choice == 2 for vote in user_votes)
        thispoll.votes = user_votes.count()
    renderdict = {
        'polls': polls,
    }
    return render(request, "jp/results.html", renderdict)
