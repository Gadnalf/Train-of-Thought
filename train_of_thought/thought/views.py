from django.shortcuts import render
from django.http import JsonResponse
from .twitterTools import get_random_trending, search_twitter

# Create your views here.
def thought(request):
    trending_topics = get_random_trending("toronto", "canada", 2)
    random_tweet = " ".join(search_twitter(trending_topics[0], 1)[0])
    return render(request, 'index.html', {"start_topic": trending_topics[0], "end_topic": trending_topics[1], "current_tweet": random_tweet})