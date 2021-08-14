from django.http import HttpResponse
from django.shortcuts import render
from . import text_class

text_obj = text_class.text


def index(request):
    return render(request,"index2.html")

def text_analysis(request):
    text = request.POST.get('text')
    cap = request.POST.get('capital')
    low = request.POST.get('lower')
    length = request.POST.get('len')
    remvpnc = request.POST.get('remvpnc')
    #print(cap)
    if cap == "on":
        analysed_txt = text_obj.captilize(text)
        purpose = "Uppercased"
    elif low == "on":
        analysed_txt = text_obj.lower(text)
        purpose = "Lowercased"
    elif length == "on":
        analysed_txt = text_obj.length(text)
        purpose = "Length"
    elif remvpnc == 'on':
        analysed_txt = text_obj.removepun(text)
        purpose = "remove puncuation"
    else:
        return HttpResponse("Errorr")
    
    params = {'html_txt':analysed_txt,'purpose':purpose}
    return render(request,"text_analysis.html",params)

def about(request):
    return HttpResponse("about page is under construction")