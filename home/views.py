from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from registration.models import Coursereg
from django.contrib import messages
import json
from django.views.decorators.cache import cache_control

# Create your views here.
course={
    "cloud":"Practicing cloud computing (Azure)",
    "iot":"Internet of Things (IoT)",
    "uiux":"UI/UX Web-Dev (CSS, JS, Bootstrap)",
    "dbms":"Database Management with postgresql",
    "flask":"Dynamic Web-Dev with Flask",
    "django":"Dynamic Web-Dev with Django",
    "ml":"Machine Learning for Data Analysis",
    "cv":"Image Processing/ Computer vision",
    "python":"Python for AI (Advanced)",
    "java":"Java from A-Z (noob to pro)"
}

def homeIndex(request):
    return render(request,'home/index.html')

def challenge(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        f_data=request.POST
        cid = f_data['cid']
        ob=Coursereg.objects.all().filter(sid__iexact= cid)
        #globvar.ob=ob
        if ob.exists():
            with open('home/djangoqtn.json') as json_file:
                data = json.load(json_file)
            #print(type(data))
            if ob[0].chscore <0 :
                messages.success(request,'Successfully validated, please proceed with your test ! ')
                return render(request,'home/challengeAct.html',{'flag':True,'data':zip(list(data.values()),list(data.keys()),[1,2,3,4,5,6,7,8,9,10]),"cid":cid})
            elif ob[0].chscore >-1 and ob[0].handson <0:
                messages.success(request,'Successfully validated, please complete your handson ! ')
                return render(request,'home/challengeAct.html')
            else :
                messages.success(request,'Successfully validated')
                return render(request,'home/challengeAct.html',
                {'chscore':(ob[0].chscore + ob[0].handson +10 ),'sname':ob[0].name.upper(),'scollege':ob[0].college.upper(),
                'cstart':ob[0].cstart,'cend':ob[0].cend,'vcode':ob[0].sid,'repo':ob[0].projrepo,'course':course[ob[0].course]})

        else:
            messages.error(request,'Wrong Certification ID please reach your instructor !')
            return redirect('challenge')
        #return HttpResponse(len(ob))
    return render(request,'home/challenge.html')


def chalval(request):
    if request.method == 'POST':
        total = 0
        # create a form instance and populate it with data from the request:
        f_data=request.POST
        with open('home/djangokey.json') as json_file:
                dsol = json.load(json_file)
        cid = f_data["cid"]
        print(f_data)
        for i in range(1,11):
            if f_data[str(i)] == dsol[str(i)]:
                total+=2
        ob=Coursereg.objects.all()
        if ob.filter(sid__iexact= cid).exists():
            o1=ob.get(sid__iexact= cid)
            o1.chscore = total
            o1.save()
            cid = None
            print(cid)
            return render(request,'home/challengeAct.html',{'flag':False})
        else:
            messages.error(request,"you have reloaded the page/ connection timeout")
            return redirect('challenge')
        #return render(request,'home/challengeAct.html',{'flag':False})
    
    return redirect('challenge')