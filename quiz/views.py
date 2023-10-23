
from .models import Add,Quiz
from django.shortcuts import render
import random

def myview(request):
    comment_objs = Quiz.objects.all()
    comment_objs2 = Add.objects.all()
    mydict = {'comments':comment_objs ,'comments2':comment_objs2}
    return render(request, 'index.html', context=mydict)


def detail(request, pk):
    the_post_obj = Quiz.objects.get(pk=pk)
    comment_objs = list(Add.objects.all())
    comment_objs2 = random.sample(comment_objs,len(Add.objects.all()))
    mydict = {'the_post':the_post_obj,'comments3':comment_objs2}

    return render(request, 'details.html', context=mydict)





