from django.http.response import HttpResponse
from django.shortcuts import render
from registration.models import Coursereg
from django.core.mail import EmailMessage, send_mail
import datetime
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
        dateadded = datetime.datetime.now()
        #print(name,dob,college,dep,yos,contact,mailid,course,note)
        Coursereg.objects.create(dateadded = dateadded,name=name,dob=dob,college=college,dep=dep,
        ystudy=yos,contact=contact,mailid=mailid,course=course,note=note)

        # Send Email
        email = EmailMessage(
            subject='KAVWV Internship Registration Confirmation for {0}'.format(name),
            body='''Hello {0}, \n We received your registration for the course with following Details, we will reach you shortly.
            \n name : {0} \n college : {1}\n Year of study : {2} \n course : {3}
            \n Please reply to this mail in case of any Queries\n             
            \nKind Regards,\nKAVWV\ninfo.kavwv@gmail.com  '''.format(
                name,college,yos,course),
            from_email='info.kavwv@gmail.com',
            to=[mailid],
            bcc=['rameshsharma261098@gmail.com'],
            reply_to=['info.kavwv@gmail.com'],
            headers={'Message-ID': 'Kavwv internship challenge'},
        )
        email.send(fail_silently=False )
        #send_mail(
        #    subject='KAVWV Internship Registration Confirmation for {0}'.format(name),
        #    message='''Hello {0}, \n We received your registration for the course with following Details, we will reach you shortly.
        #        \n name : {0} \n college : {1}\n Year of study : {2} \n course : {3}
        #        \n Please reply to this mail in case of any Queries\n             
        #        \nKind Regards,\nKAVWV\ninfo.kavwv@gmail.com  '''.format(
        #        name,college,yos,course),
        #    from_email='info.kavwv@gmail.com',
        #    recipient_list=[mailid,'rameshsharma261098@gmail.com'],
        #    fail_silently=False
        #)
        
        return render(request,'register/index.html',{'result':'1','name':name,})
    return render(request,'register/index.html')