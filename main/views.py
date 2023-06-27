from django.shortcuts import render
from games.models import Games
from clips.models import Clips
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.


# https://localhost:8000
def index(request):
    p = Paginator(Games.objects.all().order_by('-date_added'), 15)
    p2 = Paginator(Clips.objects.all().order_by("-date_uploaded"), 12)

    page = request.GET.get('page')
    venus = p.get_page(page)
    venus2 = p2.get_page(page)
    return render(request, "main/main.html", {
        "games": venus,
        "clips": venus2
    })
