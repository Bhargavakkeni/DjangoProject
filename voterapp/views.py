from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

# Create your views here.
arr=['C','Python','Java','Kotlin','C++','Ruby','Javascript','PHP','.net','swift','MySQL']
globaldictcnt=dict()
def index(request):
    
    mydict={
        'arr': arr
    }
    return render(request,"index.html",context=mydict)

def getquery(request):
    q=request.GET['languages']
    if q in globaldictcnt:
        globaldictcnt[q]=globaldictcnt[q]+1
    else:
        globaldictcnt[q]=1
    mydict={
            'arr':arr,
            'globaldictcnt':globaldictcnt
        }
    return render(request,'index.html',context=mydict)

def sortdata(request):
    global globaldictcnt
    globaldictcnt=dict(sorted(globaldictcnt.items(),key=lambda x:x[1],reverse=True))
    mydict={
        'arr':arr,
        'globaldictcnt':globaldictcnt
    }
    return render(request,'index.html',context=mydict)