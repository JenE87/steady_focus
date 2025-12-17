from django.shortcuts import render


def pomodoro_home(request):
    """
    Display the Pomodoro timer interface.

    Renders the public Pomodoro timer page, which allows users
    to start focus and break sessions using predefined intervals.

    **Template**

    :template:`pomodoro/pomodoro.html`

    """
    return render(request, 'pomodoro/pomodoro.html')
