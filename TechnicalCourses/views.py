from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Allcourses, details
from django import forms
from .models import Entry
from .forms import RegisterForm


from django.http import HttpResponseRedirect
from .forms import NameForm
from .models import Post , Tag
from django.shortcuts import render

def yourchoice(request, couse_id):
    course = get_object_or_404(Allcourses, pk = couse_id)
    try: selected_ct= course.details_set.get(pk=request.POST['choice'])
    except(KeyError,Allcourses.DoesNotExist):
        return render(request, 'TechnicalCourses/detail.html', {'course': course, 'error_message':"Select a valid option"})
    else: selected_ct.your_choice=True
    selected_ct.save()
    return render (request, 'TechnicalCourses/detail.html',{'course':course})

def register_acc(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = RegisterForm()

    return render(request, 'TechnicalCourses/register.html', {'form': form})

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'TechnicalCourses/Name.html', {'form': form})

# Create your views here.
def Courses(request):
    ac = Allcourses.objects.all()
    template = loader.get_template('TechnicalCourses/Courses.html')
    context = {
        'ac': ac,
    }
    return HttpResponse(template.render(context, request))

def detail(request, couse_id):
    course=get_object_or_404(Allcourses, pk=couse_id)
    return render( request, 'TechnicalCourses/detail.html',{'course':course})
    #try:
        #course = Allcourses.objects.get(pk=couse_id)
   # except Allcourses.DoesNotExist:
        #raise Http404("Course Not Available")
    #return render(request, 'TechnicalCourses/detail.html', {'course': course})
def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'TechnicalCourses/posts.html', context={'posts': posts})
def post_detail(request,slug):
    post=Post.objects.get(slug_iexact=slug)
    return render(request, 'TechnicalCourses/post_details.html', context={'post': post})
def tags_list(request):
    tags=Tag.objects.all()
    return render(request, 'TechnicalCourses/tags_list.html', context={'tags': tags})

def add(request):
    form = NameForm()
    context = {'form': form}
    return render(request,'TechnicalCourses/Name.html',context)

