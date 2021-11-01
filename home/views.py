from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from registration.models import Coursereg
from django.contrib import messages
import json
from django.views.decorators.cache import cache_control

# Create your views here.

class globvar:
    cid="errorval"

def homeIndex(request):
    return render(request,'home/index.html')
ob:object
def challenge(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        f_data=request.POST
        cid = f_data['cid']
        globvar.cid=cid
        ob=Coursereg.objects.all().filter(sid__iexact= cid)
        #globvar.ob=ob
        if ob.exists():
            with open('home/djangoqtn.json') as json_file:
                data = json.load(json_file)
            #print(type(data))
            if ob[0].chscore <0 :
                messages.success(request,'Successfully validated, please proceed with your test ! ')
                return render(request,'home/challengeAct.html',{'flag':True,'data':zip(list(data.values()),list(data.keys()),[1,2,3,4,5,6,7,8,9,10])})
            elif ob[0].chscore >-1 and ob[0].handson <0:
                messages.success(request,'Successfully validated, please complete your handson ! ')
                return render(request,'home/challengeAct.html')
            else :
                messages.success(request,'Successfully validated')
                return render(request,'home/challengeAct.html',{'chscore':(ob[0].chscore + ob[0].handson +10 )})

        else:
            messages.error(request,'Wrong Certification ID please reach your instructor !')
            return redirect('challenge')
        #return HttpResponse(len(ob))
    return render(request,'home/challenge.html')

@cache_control(no_cache=True, must_revalidate=True)
def chalval(request):
    if request.method == 'POST':
        total = 0
        # create a form instance and populate it with data from the request:
        f_data=request.POST
        with open('home/djangokey.json') as json_file:
                dsol = json.load(json_file)
        for i in range(1,11):
            if f_data[str(i)] == dsol[str(i)]:
                total+=2
        ob=Coursereg.objects.all()
        if ob.filter(sid__iexact= globvar.cid).exists():
            o1=ob.get(sid__iexact= globvar.cid)
            o1.chscore = total
            o1.save()
            globvar.cid = None
            return render(request,'home/challengeAct.html',{'flag':False})
        else:
            messages.error(request,"you have reloaded the page/ connection timeout")
            return redirect('challenge')
    
    return redirect('challenge')