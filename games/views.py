from django.shortcuts import render
from django.http import Http404
from .models import Games
from django.core.paginator import Paginator
# Create your views here.


def details(request, id):
    try:
        game = Games.objects.get(id=id)
    except Games.DoesNotExist:
        raise Http404

    otherGames = Paginator(Games.objects.filter(
        type=game.type).order_by("-date_added"), 5)
    page = request.GET.get('page')
    othersPage = otherGames.get_page(page)

    return render(request, "main/details.html", {
        "othersPage": othersPage,
        "game": game
    })
