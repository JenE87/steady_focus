from django.shortcuts import render


def pomodoro_home(request):
    """
    Public Pomodoro page 
    """
    return render(request, 'pomodoro/pomodoro.html')
