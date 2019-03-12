from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.views.generic.list import ListView
from prezzee.models import GiftCard


class GiftCardListView(ListView):
    model = GiftCard
    paginate_by = 100  # if pagination is desired

    def get_queryset(self):
        username = self.request.GET.get('username', 'brian')
        user = User.objects.get(username=username)
        new_context = GiftCard.objects.filter(user=user)
        return new_context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


def archive(request, gf_id, username):
    gf = GiftCard.objects.get(id=gf_id)
    gf.archived = True
    gf.save()
    return HttpResponseRedirect('/prezzee/?username=%s' % username)


def active(request, gf_id, username):
    gf = GiftCard.objects.get(id=gf_id)
    gf.archived = False
    gf.save()
    return HttpResponseRedirect('/prezzee/?username=%s' % username)
