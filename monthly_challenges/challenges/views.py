from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.template.loader import render_to_string
from django.urls import reverse


# Create your views here
MONTHLY_CHALLENGES = {
    "january": "Eat no meat for the entire month!",
    "february": "Walk for at least 20 minutes every day",
    "march": "Learn Django at least 20 minutes every day",
    "april": "Embrace a daily meditation practice to find calm and clarity in your routine",
    "may": "Challenge yourself to read a new book every week and explore different literary worlds",
    "june": "Engage in a creative activity each day, whether it's drawing, writing, or crafting",
    "july": "Make an effort to connect with a friend or family member every day, even if it's just a quick chat",
    "august": "Dedicate time each day to practice a new language and broaden your linguistic skills!",
    "september": "Explore a new hiking trail or outdoor location every weekend to stay active and connected with nature",
    "october": "Try a new healthy recipe each day to boost your culinary repertoire and well-being",
    "november": "Express gratitude by writing down three things you're thankful for every day",
    # "december": "Spread kindness by performing a daily random act of kindness for others throughout the month",
    "december": None
}

def index(request):
    months = list(MONTHLY_CHALLENGES.keys())

    return render(request, "challenges/index.html",{
        "months":months
    })

def monthly_challenge_by_number(request, month):
    months = list(MONTHLY_CHALLENGES.keys())
    if month < 1 or month > 12:
        return HttpResponseNotFound("Invalid month!")

    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month]) # /challenges/january
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = MONTHLY_CHALLENGES[month]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month_name": month
        })
    except:
        raise Http404()
