from django.shortcuts import render
from .forms import CalculatorForm, GuessForm


def calculator(request):
    submit_button = request.POST.get("submit")
    a = 2
    b = 4
    c = 2

    form = CalculatorForm(request.POST or None)
    if form.is_valid():
        a = form.cleaned_data.get("a")
        b = form.cleaned_data.get("b")
        c = form.cleaned_data.get("c")
    try:
        discriminant = float(b) ** 2 - 4 * float(a) * float(c)
        if discriminant < 0:
            discriminant_res = "Корней нет"
        elif discriminant == 0:
            x = -float(b) / (2 * float(a))
            discriminant_res = x
        else:
            x1 = (-float(b) + discriminant**0.5) / (2 * float(a))
            x2 = (-float(b) - discriminant**0.5) / (2 * float(a))
            discriminant_res = f"{round(x1, 2)} , X2 = {round(x2, 2)}"

        context = {
            "form": form,
            "discriminant": round(discriminant, 2),
            "discriminant_res": discriminant_res,
            "submit_button": submit_button,
        }
        return render(request, "calculator.html", context)
    except (ZeroDivisionError, ValueError):
        return render(request, "calculator.html")


def guess_the_color(request):
    submit_button2 = request.POST.get("submit2")
    guess = 0
    blue = "Синий"
    green = "Зеленый"
    red = "Красный"

    form2 = GuessForm(request.POST or None)
    if form2.is_valid():
        guess = form2.cleaned_data.get("guess")

    if 1 <= int(guess) <= 60:
        color = blue
    elif 61 <= int(guess) <= 85:
        color = green
    elif 86 <= int(guess) <= 100:
        color = red
    else:
        color = "Нет такого предмета"

    context = {"form2": form2, "color": color, "submit_button2": submit_button2}

    return render(request, "guess_the_color.html", context)
