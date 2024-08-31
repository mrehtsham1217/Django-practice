from django.shortcuts import render
from .models import Tweet
from .forms import TweetForm
from django.shortcuts import get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .forms import UserRegisterForm
from django.contrib.auth.models import User
# Create your views here.
def index(request):
    return render(request,'tweet/index.html')

# function for getting all tweets
def get_all_tweets(request):
    all_tweets=Tweet.objects.all().order_by("created_at")
    return render(request,'tweet/all_tweets.html',{"all_tweets":all_tweets})

@login_required
def tweet_create(request):
    if request.method=='POST':
        form=TweetForm(request.POST,request.FILES)
        #request.FILES-->if you are excepting the files from user
        if form.is_valid():
            tweet=form.save(commit=False)
            tweet.user=request.user
            tweet.save()
            return redirect('tweet_list')
    else: # if user is giving empty forms
        form=TweetForm()
    return render(request,'tweet/create_form.html',{"form":form})

@login_required
def tweet_edit(request, tweet_id):
    # Get the tweet object or return a 404 if not found
    tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user)
    
    if request.method == 'POST':
        # Create a form instance with POST data and files, and the existing tweet instance
        form = TweetForm(request.POST, request.FILES, instance=tweet)
        
        if form.is_valid():
            # Save the form without committing to the database immediately
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_list')  # Ensure this matches your URL pattern name
    else:
        # Create a form instance with the existing tweet instance
        form = TweetForm(instance=tweet)
    
    return render(request, 'tweet/create_form.html', {"form": form})


@login_required
def tweet_delete(request,tweet_id):
    tweet=get_object_or_404(Tweet,pk=tweet_id,user=request.user)
    if request.method=='POST':
        tweet.delete()
        return redirect("tweet_list")
    else:
        return render(request,'tweet/delete_form.html',{"tweet":tweet})
    
    
def register(request):
    if request.method=='POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request,user)
            return redirect("tweet_list")
    else:
        form=UserRegisterForm()
    return render(request,'registration/register.html',{"form":form})

def user_profile(request,username):
    user=get_object_or_404(User,username=username)
    tweets = Tweet.objects.filter(user=user).order_by('created_at')
    return render(request,"tweet/user_profile.html",{"user":user,"tweets":tweets})

def search_user(request):
    query=request.GET.get("query","")
    print(query)
    if query:
        users=User.objects.filter(username__icontains=query)
    else:
        users=User.objects.none()
    return render(request,'tweet/search_user.html',{"users":users,"query":query})
             

        
