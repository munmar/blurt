from django.shortcuts import render

from .models import Post


# Create your views here.
def index(request):
    blurt_list = Post.objects.order_by("-pub_date")[:5]
    context = {
        "blurt_list": blurt_list,
    }
    return render(request, "blurt/index.html", context)
