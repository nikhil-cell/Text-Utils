from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, "index.html")
def analyze(request):
    global params
    djtext =(request.POST.get('text', 'defult'))
    removepunc =(request.POST.get('removepunc', 'off'))
    fullcaps =(request.POST.get('fullcaps', 'off'))
    newlineremover =(request.POST.get('newlineremover', 'off'))
    extraspaceremover =(request.POST.get('extraspaceremover', 'off'))
    #wordcount =  (request.POST.get('wordcount', 'off'))

    if removepunc == "on":
        analyzed =""
        punctuation = '''!@#$%^&*(){}[];':<>,.\|/?~`'''
        for char in djtext:
            if char not in punctuation:
                analyzed = analyzed + char
        params = {'purpose':'Remove punctuation', 'analyzed_text':analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)
        
    if fullcaps == "on":
        analyzed=""
        for char in djtext:
            analyzed = analyzed + char.upper()
        
        params = {'purpose': 'Changed to Upper case', 'analyzed_text': analyzed}
        djtext =analyzed
        #return render(request, 'analyze.html', params)
    
    if newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char !="\n" and char != "\r":
                analyzed = analyzed + char

        params = {'purpose': 'LINE REMOVER', 'analyzed_text': analyzed}
        
        djtext =analyzed
        #return render(request, 'analyze.html', params)
    
    if extraspaceremover == "on":
        analyzed = ""
        for indx, char in enumerate(djtext):
            if not (djtext[indx]==" " and djtext[indx+1]==" "): 
                 analyzed = analyzed + char

        params = {'purpose': 'REMOVE SPACE', 'analyzed_text': analyzed}
        #return render(request, 'analyze.html', params)

    if removepunc!="on" and fullcaps!="on" and newlineremover!="on" and extraspaceremover!="on":
        return HttpResponse("Please select any operation and try again later")  
    
    return render(request, 'analyze.html', params)
