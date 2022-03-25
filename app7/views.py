from django.shortcuts import render

# Create your views here.
def ifelsecondition(request):
    d={'a':98465,'b':969834}
    return render(request,'condition.html',d)