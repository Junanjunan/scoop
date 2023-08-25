from django.shortcuts import render


def first_user_view(request):
    return render(request, "users/first_user.html")
