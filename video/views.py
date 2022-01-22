from xml.etree.ElementTree import Comment
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

import video
from .addins.auth import authenticate, login as login_backend, logout as backend_logout, auth
from .models import User, Video, VideoStat, Comment
import datetime


# Create your views here.


@auth
def dashboard(request):
    user_id = request.session['_miniplayer_userid']
    user = User.objects.get(pk=user_id)
    content = {
        'user': user
    }
    return render(request, 'miniplayer/miniplayer.html', content)

def login(request):
    if request.method == "GET":
        return render(request, 'auth/login.html')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username, password)
        if user is not None:
            login_backend(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'auth/login.html', {'error': 'Złe dane logowania!'})

@auth
def logout(request):
    backend_logout(request)
    return redirect('login')

@auth
def getVideos(request):
    videos = Video.objects.all()
    video_json = [x.toJson() for x in videos]
    return JsonResponse(video_json, safe=False)

@auth
def videoPage(request, id):
    if request.method == "GET":
        user_id = request.session['_miniplayer_userid']
        user = User.objects.get(pk=user_id)
        content = {
            'user': user
        }
        return render(request, 'miniplayer/videoPage.html', content)
    if request.method == "POST":
        if request.POST.get('type') == 'video':
            video = Video.objects.get(pk=id)
            return JsonResponse(video.toJson(), safe=False)

@auth
def comments(request, id):
    if request.method == "GET":
        comments = Comment.objects.filter(video_id=id).order_by('-date')
        if comments == None:
            return JsonResponse([], safe=False)
        else:
            comments_json = [x.toJson() for x in comments]
            return JsonResponse(comments_json, safe=False)
    if request.method == 'POST':
        comment_post = request.POST.get('comment')
        comment = Comment()
        comment.user_id = int(request.session['_miniplayer_userid'])
        comment.video_id = id
        comment.date = datetime.datetime.now()
        comment.text = comment_post
        comment.save()
        return JsonResponse(1, safe=False)

@auth
def rating(request, id):
    if request.method == "GET":
            user_id = request.session['_miniplayer_userid']
            video_stat = VideoStat.objects.filter(user_id=user_id, video_id=id).first()
            if video_stat == None:
                return JsonResponse(0, safe=False)
            else:
                return JsonResponse(video_stat.toJsonRating(), safe=False)
    if request.method == "POST":
        user_id = request.session['_miniplayer_userid']
        rating_post = request.POST.get('rating')
        rating_user = VideoStat.objects.filter(user_id=user_id, video_id=id).first()
        if rating_user != None:
            rating_user.rating = int(rating_post)
            rating_user.save()
            return JsonResponse(1, safe=False)
        else:
            rating = VideoStat()
            rating.rating = int(rating_post)
            rating.user_id = int(user_id)
            rating.video_id = id
            rating.save()
            return JsonResponse(1, safe=False)


