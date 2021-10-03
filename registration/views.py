from django.shortcuts import render
from registration.models import Coursereg
# Create your views here.
def regStudent(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        f_data=request.POST
        name = f_data['Sname']
        dob = f_data['dob']
        college = f_data['college']
        dep = f_data['dep']
        yos = f_data['yos']
        contact = f_data['contact']
        mailid = f_data['admit-mail']
        course = f_data['course']
        note = f_data['note']
        #print(name,dob,college,dep,yos,contact,mailid,course,note)
        Coursereg.objects.create(name=name,dob=dob,college=college,dep=dep,
        ystudy=yos,contact=contact,mailid=mailid,course=course,note=note)
        return render(request,'register/index.html',{'result':'1','name':name})
    return render(request,'register/index.html')