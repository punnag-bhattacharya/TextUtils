from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def AboutUs(request):
    return render(request, 'AboutUs.html')

def ContactUs(request):
    return render(request, 'ContactUs.html')

def Analyze(request):
    djtext= request.POST.get('Text', 'default')

    removepunc= request.POST.get('rempunc', 'off')
    fullcapital= request.POST.get('fullcaps', 'off')

    if removepunc != 'on' and fullcapital != "on":
        analyzed= djtext
        params= {'purpose': 'not changed!', 'analyzed_text': analyzed}
        return render(request, 'Analyze.html', params)

    elif removepunc != "on":
        analyzed= djtext.upper()
        params= {'purpose': 'only converted to caps!', 'analyzed_text': analyzed}
        return render(request, 'Analyze.html', params)

    elif fullcapital != "on":
        punc_list= '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        new= ''
        for ch in djtext:
            if ch not in punc_list:
                new+= ch
        analyzed= new
        params= {'purpose': 'only freed from punctuations!', 'analyzed_text': analyzed}
        return render(request, 'Analyze.html', params)

    else:
        punc_list= '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        new= ''
        for ch in djtext:
            if ch not in punc_list:
                new+= ch
        analyzed= new.upper()
        params= {'purpose': 'both freed from punctuations and converted to caps!', 'analyzed_text': analyzed}
        return render(request, 'Analyze.html', params)