from django.shortcuts import render,get_object_or_404,redirect,Http404
from django.http import HttpResponseRedirect
from django.urls import reverse

#from formapp import templates
#from formapp.models import *
from websitedata.form import *
from django.contrib.auth.models import User
from django.contrib import auth
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from datetime import timezone
from django.utils import timezone




# Create your views here.


    

def loginform(request):

    if request.method=='POST':
        form =loginformdesign(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'forms.html')
    else:
        form=loginformdesign()
    return render(request,'forms.html',{'form2':form})






def login(request):
    return render(request,'Login_page.html')




def formview(request):





    if request.method=='POST':
        form1=form(request.POST)

        if form1.is_valid():






            form1.save()
            return render(request,'signup.html',{'form':form1})
    else:
        form1=form()
    return render(request,'signup.html',{'form':form1})



def signup(request):
    if request.method=='POST':
        forms=form(request.POST)
        if forms.is_valid():
            username=forms.cleaned_data['username']
            email=forms.cleaned_data['email']
            first_name=forms.cleaned_data['first_name']
            last_name=forms.cleaned_data['last_name']
            password=forms.cleaned_data['password']
            User.objects.create_user(username=username,email=email,first_name=first_name,last_name=last_name,password=password)

            return HttpResponseRedirect('/signin')

    else:

        forms=form()


    return render(request,'signup.html',{'form':forms})



def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        try:
            user=auth.authenticate(username=username,password=password)
            if user is not None:
                auth.login(request,user)


                return HttpResponseRedirect(reverse('index'))
            elif username=="":

                messages.error(request,'Please Enter your username')
            elif password=="":
                messages.error(request,'Please Enter your password')


            else:
                messages.error(request,'Username and password doesnot match')


        except User.DoesNotExist:
            pass

    return render(request,'forms.html')

def logout(request):
    auth.logout(request)

    return HttpResponseRedirect('signin')






def index(request):
    return render(request,'index.html')

@login_required(login_url='signin')
def post(request):


    if request.method=='POST':
        if request.POST['titles'] and request.POST['description'] and request.FILES['photo']:
            Post=posts()
            Post.title=request.POST['titles']

            Post.description=request.POST['description']
            Post.images=request.FILES['photo']

            Post.pub_date=timezone.datetime.now()
            Post.username=request.user
            Post.save()
            return HttpResponseRedirect('/')
        else:
            return render(request, '../PostFiles/post/create_post.html', {'error': 'all fields are required'})

    else:
        return render(request, '../PostFiles/post/create_post.html')
@login_required(login_url='signin')
def data(request):
    datas=posts.objects.all()
    return render(request,'index.html',{'dat':datas})


def forum(request):
    post=ForumPost.objects.all()
    return render(request,'forum.html',{'post':post})


def ForumPostDetail(request,post_id):
    try:
        data = ForumPost.objects.get(pk=post_id)
    except ForumPost.DoesNotExist:
        raise Http404('Templates Doesnot Exist')
    return render(request, 'PostDetails.html', {'posts':data})

@login_required(login_url='signin')
def create(request):
    if request.method=='POST':
        if request.POST['title'] or request.POST['description'] or request.FILES['images']:
            form = ForumPost()
            form.title = request.POST.get('title')
            form.description = request.POST.get('description')
            form.images = request.FILES.get('images')
            form.upload_date = timezone.datetime.now()
            form.edit_date = timezone.now()
            form.user = request.user
            form.save()
            return HttpResponseRedirect('/forum')
        else:
            raise Http404('Please Enter the form correctly')


    else:


        return render(request,'create.html')






def user_profile(request,username=None):
    if username:
        user = User.objects.get(username=username)
    else:
        user = request.user
    args = {'user': user}
    return render(request, 'profile.html', args)



def profile_edit(request):
    if request.method == 'POST':

        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.userprofile)
        if p_form.is_valid():

            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('/profile')

    else:

        p_form = ProfileUpdateForm(instance=request.user.userprofile)

    context = {

        'p_form': p_form
    }

    return render(request, 'edit_profile.html', context)






def upload_profile(request):
    if request.method=='POST':
        if request.POST['description'] or request.POST['city'] or request.FILES['website'] or request.FILES['profile_pic'] or request.FILES['cover_pic']:
            form = UserProfile()
            form.description = request.POST.get('description')
            form.city = request.POST.get('city')
            form.Website = request.POST.get('website')
            form.profile_pic = request.FILES.get('profile_pic')
            form.cover_pic = request.FILES.get('cover_pic')
            
            form.user = request.user
            form.save()
            return HttpResponseRedirect('/user/profile')
        else:
            raise Http404('Please Enter the form correctly')


    else:


        return render(request,'uploadprofile.html')



def edit_post(request):
    if request.method == 'POST':

        post = post_edit(request.POST,
                                   request.FILES,
                                   instance=request.user.edit_post.pk
                                   
                                   )
        if post.is_valid():

            post.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('/forum')

    else:

        post = post_edit(instance=request.user.edit_post.pk)

    context = {

        'post': post
    }

    return render(request, 'edit_post.html', context)   


def create_profiles(request):
    if request.method=='POST':
        post=create_profile(request.user.city)
        if post.is_valid():
            post.save()

    else:
        post=create_profile()

    return render(request,'create.html',{'form':post})