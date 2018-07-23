from django.shortcuts import render
import random
def appmain(request):
    random.seed()
    value = random.randint(1,100)
    if value < 10:
        file = open('./appname/fortune/daikiti.txt', 'r')
        result = '大吉'
        string = file.read()
    elif value < 15:
        file = open('./appname/fortune/chukiti.txt', 'r')
        result = '中吉'
        string = file.read()
    elif value < 40:
        file = open('./appname/fortune/kiti.txt', 'r')
        result = '吉'
        string = file.read()
    elif value < 85:
        file = open('./appname/fortune/suekiti.txt', 'r')
        result = '末吉'
        string = file.read()
    elif value < 95:
        file = open('./appname/fortune/kyou.txt', 'r')
        result = '凶'
        string = file.read()
    else:
        file = open('./appname/fortune/daikyou.txt', 'r')
        result = '大凶'
        string = file.read()
    return render(request, 'omikuji/main.html', {
        'result': result,
        'sentence': string,
    })

# Create your views here.
