from django.contrib import auth
from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Allcourses
from django.http import HttpResponseRedirect
from .forms import LoginForm, UserForm
from .models import Post, Tag
from .forms import Register, Contact

from django.shortcuts import render

def contact_form(request):
    if request.method == 'GET':
        form =Contact(request.GET)
        if form.is_valid():
            if form.is_valid():
                # process the data in form.cleaned_data as required
                # ...
                # redirect to a new URL:
                return HttpResponseRedirect('/thanks/')

            # if a GET (or any other method) we'll create a blank form
        else:
            form = Contact()

        return render(request, 'TechnicalCourses/Name.html', {'form': form})

def yourchoice(request, couse_id):
    course = get_object_or_404(Allcourses, pk=couse_id)
    try:
        selected_ct = course.details_set.get(pk=request.GET['choice'])
    except(KeyError, Allcourses.DoesNotExist):
        return render(request, 'TechnicalCourses/detail.html', {'course': course, 'error_message':"Select a valid option"})
    else:
        selected_ct.your_choice = True
    selected_ct.save()
    return render(request, 'TechnicalCourses/detail.html', {'course': course})


def login_acc(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = Register(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = Register()

    return render(request, 'TechnicalCourses/register.html', {'form': form})


class UserProfileForm:
    pass


def add_user(request):
    if request.method == "POST":
        uform = UserForm(data = request.POST)
        pform = UserProfileForm(data = request.POST)
        if uform.is_valid() and pform.is_valid():
            user = uform.save()
            profile = pform.save(commit = False)
            profile.user = user
            profile.save()
            return HttpResponse(template.render(context, request))

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'NAME':
        # create a form instance and populate it with data from the request:
        form = Contact(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = Contact()

    return render(request, 'TechnicalCourses/Register.html', {'form': form})

# Create your views here.
def Courses(request):
    ac = Allcourses.objects.all()
    template = loader.get_template('TechnicalCourses/Courses.html')
    context = {
        'ac': ac,
    }
    return HttpResponse(template.render(context, request))

def detail(request, couse_id):
    course = get_object_or_404(Allcourses, pk=couse_id)
    return render( request, 'TechnicalCourses/detail.html', {'course': course})
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
    tags = Tag.objects.all()
    return render(request, 'TechnicalCourses/tag.html', context={'tags': tags})


def tag_detail(request, slug):
    tag = Tag.objects.get(slug_iexact=slug)
    return render(request, 'TechnicalCourses/tag_detail.html', context={'tag': tag })

def add(request):
    form = NameForm()
    context = {'form': form}
    return render(request, 'TechnicalCourses/Name.html', context)





def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return redirect('/')
    else:
        return render(request, 'TechnicalCourses/register.html', context={'username': username})
        return redirect('TechnicalCourses/Courses.html')


def register(request):
    if request.method == 'POST':
        user_form = Register(request.GET)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(request, 'TechnicalCourses/register_done.html', {'new_user': new_user})
    else:
        user_form = Register(request.GET)
    return render(request, 'TechnicalCourses/register.html', {'users': user_form})