from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
monthly_challenges = {
    'january': "Eat healthy food",
    'february': "Exercise regularly",
    'march': "Read a new book",
    'april': "Start a new hobby",
    'may': "Spend more time outdoors",
    'june': "Learn a new skill",
    'july': "Practice mindfulness",
    'august': "Drink more water",
    'september': "Organize your space",
    'october': "Volunteer for a cause",
    'november': "Practice gratitude",
    'december': None
}


def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html", {
        "months": months
    })


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month")

    redirect_month = months[month-1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect("/challenges/" + redirect_month)


def monthly_challenge(request, month):
    if month in monthly_challenges:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month_name": month.capitalize()
        })
    else:
        raise Http404("This month is not supported")
