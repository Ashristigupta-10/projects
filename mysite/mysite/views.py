#i have created this file.
from django.http import HttpResponse
from django.shortcuts import render



#def index(request):
 #   return HttpResponse("<h1>hello</h1>")

#def about(request):
 #   return HttpResponse("About")

 #code for vedio 7
 #3rd variable in render is variable or dictionary pass
 #in render we also pass a dictionary 
 #sending variables of dict in index.html templates
def index(request):
    #params={'name':'Abc','place':'Ladakh'}#dictionary used
    return render(request,'index.html',)#(params)
    #return HttpResponse("Home")

def analyze(request):
    #get the text
    djtext=request.GET.get('text','default')#its return text value and if value is not exist so it take default value.
    #check checkbox value
    removepunc=request.GET.get('removepunc','off')
    fullcaps=request.GET.get('fullcaps','off')
    newlineremover=request.GET.get('newlineremover','off')
    extraspaceremover=request.GET.get('extraspaceremover','off')
    #check which checkbox is on
    if removepunc=="on":
        analyzed =djtext
        punctuations='!()-[]{};:\'"\\,<>./?@#$%^&*_~'
        analyzed=" "
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params={'purpose':'Remove punctuations','analyzed_text':analyzed}
        #analyze the text
        return render(request,'analyze.html',params )

    elif(fullcaps=="on"):
        analyzed=""
        for char in djtext:
            analyzed =analyzed+char.upper()
        
        params={'purpose':'Changed to Uppercase','analyzed_text':analyzed}
        #analyze the text
        return render(request,'analyze.html',params )
    
    elif(extraspaceremover=="on"):
        analyzed=""
        for index,char in enumerate (djtext):
            #if djtext space and also djtext index+1 is spaceso...
            if not(djtext[index]=="" and djtext[index+1]==" "):
                analyzed =analyzed+char
        
        params={'purpose':'extraspaceremover','analyzed_text':analyzed}
        #analyze the text
        return render(request,'analyze.html',params )
    
    elif(newlineremover=="on"):
        analyzed=""
        for char in djtext:
            if char !="\n":
                analyzed =analyzed+char
        
        params={'purpose':'Removed new lines','analyzed_text':analyzed}
        #analyze the text
        return render(request,'analyze.html',params )
    else:
        return HttpResponse("Error")

