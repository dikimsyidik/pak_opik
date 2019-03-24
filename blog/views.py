from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import PostModel,Komentar
from admin_wedbook.models import Profil


def post_model_create_view(request):
    form = PostModelForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        obj = form.save(commit=False)
        #print(obj.title)
        obj.save()
        messages.success(request, "Created a new blog post!")
        context = {
            "form": PostModelForm()
        }
        #return HttpResponseRedirect("/blog/{num}".format(num=obj.id))

    template = "blog/WriteThread.html"
    return render(request, template, context)

#@login_required
def post_model_update_view(request, id=None):
    obj = get_object_or_404(PostModel, id=id)
    form = PostModelForm(request.POST or None, instance=obj)
    context = {
        "form": form
    }
    if form.is_valid():
        obj = form.save(commit=False)
        #print(obj.title)
        obj.save()
        messages.success(request, "Updated post!")
        return HttpResponseRedirect("/blog/{num}".format(num=obj.id))

    template = "blog/update-view.html"
    return render(request, template, context)


def blog_details(request, slug):
    obj = get_object_or_404(PostModel, slug=slug)
    artikelnya = PostModel.objects.all().order_by('-publish_date')[:5]
    profil = Profil.objects.all()

    # komentar = Komentar.objects.all().order_by('-publish_date')
    # form_komentar = KomentarForm(request.POST or None)

    # if form_komentar.is_valid():
    #     obj = form_komentar.save(commit=False)

    #     obj.save()
    #     return HttpResponseRedirect("/blog/{num}".format(num=obj.id))


    context = {
        "object": obj,
        "artikels":artikelnya,
        "profil":profil,
        # "komentars":komentar,
        # 'form':form_komentar,

    }

    template = "basic/blog-single.html"
    return render(request, template, context)



def post_model_delete_view(request, id=None):
    obj = get_object_or_404(PostModel, id=id)
    if request.method == "POST":
        obj.delete()
        messages.success(request, "Post deleted")
        return HttpResponseRedirect("/blog/")
    context = {
        "object": obj,
    }
    template = "blog/delete-view.html"
    return render(request, template, context)


def post_model_list_view(request):
    #query = request.GET["q"]

    query = request.GET.get("q", None)
    qs = PostModel.objects.all()
    if query is not None:
        qs = qs.filter(
                Q(title__icontains=query) |
                Q(content__icontains=query) |
                Q(slug__icontains=query)
                )
    context = {
        "object_list": qs,
    }
    template = "blog/ThreadList.html"
    return render(request, template, context)
