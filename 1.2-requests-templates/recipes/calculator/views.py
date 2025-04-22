from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import Http404, HttpResponseNotFound, HttpResponse

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    'pancake': {
        'яйцо, шт.': 1,
        'молоко, мл.': 500,
        'мука, ст.': 1.5,
        'масло растительное, ст.л.': 2,
        'сахар, ст.л.': 2,
        'соль, ч.л.': 0.5,
        'разрыхлитель, ч.л.': 0.5,
        'кипяток, ст.': 0.5,
    },
}

def recipe(request, rec):
    quantity = request.GET.get('servings')

    context = {'recipe': DATA,
               'title': 'Рецепты',
               'rec': rec,
               }

    if rec:
        try:
            context['recipe'] = DATA[rec]
            context['title'] = f'Рецепт блюда {rec}'
        except Exception:
            context['recipe'] = {}
            # raise Http404

        if quantity:
            context['recipe'] = {k: v * int(quantity) for k, v in DATA[rec].items()}
            context['title'] = f'Рецепт блюда {rec} - {quantity}шт.'

    return render(request, 'calculator/index.html', context=context)

# def PageNotFound(request, exception):
#     return HttpResponseNotFound('Такого рецепта нет')
