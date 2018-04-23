from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import TopLevelTopic

# Create your views here.
# This view is for homepage.
def home(request):
    topic_list = TopLevelTopic.objects.all()
    topic_one = topic_list[0]
    topic_two = topic_list[1]
    topic_three = topic_list[2]
    topic_four = topic_list[3]
    template = loader.get_template('siteframe/home.html')
    context = {
        'topic_one':topic_one,
        'topic_two':topic_two,
        'topic_three':topic_three,
        'topic_four':topic_four
    }
    return HttpResponse(template.render(context, request))

# The following view is the simplest view possible in Django.
# To call the view, we need to map it to a URL - and for this we
# need a RULconf
def notes(request):
    print(type(request)) # only for test
    print(request.scheme)
    print(request.body)
    print(request.path)
    response = HttpResponse("This is the notes page")
    print(type(response))
    return response

def year_archive(request, year):
    return HttpResponse("This is the archives of the year of " + year)