from lib2to3.refactor import get_all_fix_names
from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from django.db import models
from django.template.defaulttags import csrf_token
from .models import *
from landingg.forms import Name
from django.http import HttpResponseRedirect
from landingg.models import site_visitor
from.models import AlphaGuide
from django.shortcuts import redirect
from django.urls import reverse
from django.shortcuts import get_object_or_404

# Create your views here.
def home_view(request):
    # if this is a POST request we need to process the form data
    # if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        # form = name(request.POST)
        # check whether it's valid:
        # if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            # return HttpResponseRedirect('/thanks/')
    # if a GET (or any other method) we'll create a blank for
    # return render(request, "home_view.html")
    if request.method == 'POST':
        form = Name(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect(reverse("results", args=[user.id]))
    else:
        form = Name()
    return render(request, "home_view.html",{'form':form})
# create another view for the Alphanumeric operations

def results(request,id):
       # print(name, email)
        #ins = Alphanumeric(name=name, email=email)
        name = get_object_or_404(NameField, id=id)
        user = name.name
            # ins = NameField(name=name.name,email=name.email)
            # ins.save()
        y=list(user)
        print(name)
        AJS = ['A','J','S']
        BT = ['B','K','T']
        CLU = ['C','L','U']
        DMV = ['D','M','V']
        ENW = ['E','N','W']
        FOX = ['F','O','X']
        GPY = ['G','P','Y']
        HQZ = ['H','Q','Z']
        IR = ['I','R']
        GPY = ['G','P','Y']
            # print(name[0])
        # name = get_object_or_404(NameField, id=id) 
        for idx, x in enumerate(y):
            for idx in range(len(y)):
                if idx == 0 and user[0].upper() in AJS:
                    name = NameField.objects.get(id=id)
                    thisresult2= AlphaGuide.objects.get(id=166)
                    this = thisresult2.attribute
                    name.thisresult = this
                    name.save()
                if idx == 0 and user[0].upper() in BT:
                    name = get_object_or_404(NameField, id=id)
                    thisresult= AlphaGuide.objects.get(id=167)
                    this = thisresult.attribute
                    name.thisresult = this
                    name.save()
                
                if idx == 0 and user[0].upper() in CLU:
                    name = get_object_or_404(NameField, id=id)
                    thisresult= AlphaGuide.objects.get(id=168)
                    this = thisresult.attribute
                    name.thisresult = this
                    name.save()
                
                if idx == 0 and user[0].upper() in DMV:
                    name = get_object_or_404(NameField, id=id)
                    thisresult= AlphaGuide.objects.get(id=169)
                    this = thisresult.attribute
                    name.thisresult = this
                    name.save()
                
                if idx == 0 and user[0].upper() in ENW:
                    name = get_object_or_404(NameField, id=id)
                    thisresult= AlphaGuide.objects.get(id=170)
                    this = thisresult.attribute
                    name.thisresult = this
                    name.save()
                
                if idx == 0 and user[0].upper() in FOX:
                    name = get_object_or_404(NameField, id=id)
                    thisresult= AlphaGuide.objects.get(id=171)
                    this = thisresult.attribute
                    name.thisresult = this
                    name.save()
                
                if idx == 0 and user[0].upper() in GPY:
                    name = get_object_or_404(NameField, id=id)
                    thisresult= AlphaGuide.objects.get(id=172)
                    this = thisresult.attribute
                    name.thisresult = this
                    name.save()
                if idx == 0 and user[0].upper() in HQZ:
                    name = get_object_or_404(NameField, id=id)
                    thisresult= AlphaGuide.objects.get(id=173)
                    this = thisresult.attribute
                    name.thisresult = this
                    name.save()
                if idx == 0 and user[0].upper() in IR:
                    name = get_object_or_404(NameField, id=id)
                    thisresult= AlphaGuide.objects.get(id=174)
                    this = thisresult.attribute
                    name.thisresult = this
                    name.save()
                # return render(request,'results.html')
            
                if idx == 1 and user[1].upper() in AJS:
                    name = get_object_or_404(NameField, id=id)
                    thisresult1= AlphaGuide.objects.get(id=175)
                    this = thisresult1.attribute
                    name.thisresult1 = this
                    name.save()

                if idx == 1 and user[1].upper() in BT:
                    name = get_object_or_404(NameField, id=id)
                    thisresult1= AlphaGuide.objects.get(id=176)
                    this = thisresult1.attribute
                    name.thisresult1 = this
                    name.save()

                if idx == 1 and user[1].upper() in CLU:
                    name = get_object_or_404(NameField, id=id)
                    thisresult1= AlphaGuide.objects.get(id=177)
                    this = thisresult1.attribute
                    name.thisresult1 = this
                    name.save()

                if idx == 1 and user[1].upper() in DMV:
                    name = get_object_or_404(NameField, id=id)
                    thisresult1= AlphaGuide.objects.get(id=178)
                    this = thisresult1.attribute
                    name.thisresult1 = this
                    name.save()

                if idx == 1 and user[1].upper() in ENW:
                    name = get_object_or_404(NameField, id=id)
                    thisresult1= AlphaGuide.objects.get(id=179)
                    this = thisresult1.attribute
                    name.thisresult1 = this
                    name.save()
            
                if idx == 1 and user[1].upper() in FOX:
                    name = get_object_or_404(NameField, id=id)
                    thisresult1= AlphaGuide.objects.get(id=180)
                    this = thisresult1.attribute
                    name.thisresult1 = this
                    name.save()
            
                if idx == 1 and user[1].upper() in GPY:
                    name = get_object_or_404(NameField, id=id)
                    thisresult1= AlphaGuide.objects.get(id=181)
                    this = thisresult1.attribute
                    name.thisresult1 = this
                    name.save()
            
                if idx == 1 and user[1].upper() in HQZ:
                    name = get_object_or_404(NameField, id=id)
                    thisresult1= AlphaGuide.objects.get(id=182)
                    this = thisresult1.attribute
                    name.thisresult1 = this
                    name.save()
            
                if idx == 1 and user[1].upper() in IR:
                    name = get_object_or_404(NameField, id=id)
                    thisresult1=  AlphaGuide.objects.get(id=183)
                    this = thisresult1.attribute
                    name.thisresult1 = this
                    name.save()
                
            
                if idx == 2 and user[2].upper() in AJS:
                    thisresult2= AlphaGuide.objects.get(id=184)
                    name = get_object_or_404(NameField, id=id)
                    this = thisresult2.attribute
                    name.thisresult2 = this
                    name.save()

                if idx == 2 and user[2].upper() in BT:
                    thisresult2=AlphaGuide.objects.get(id=185)
                    name = get_object_or_404(NameField, id=id)
                    this = thisresult2.attribute
                    name.thisresult2 = this
                    name.save()
            
                if idx == 2 and user[2].upper() in CLU:
                    thisresult2=AlphaGuide.objects.get(id=186)
                    name = get_object_or_404(NameField, id=id)
                    this = thisresult2.attribute
                    name.thisresult2 = this
                    name.save()
            
                if idx == 2 and user[2].upper() in DMV:
                    thisresult2=AlphaGuide.objects.get(id=187)
                    name = get_object_or_404(NameField, id=id)
                    this = thisresult2.attribute
                    name.thisresult2 = this
                    name.save()
            
                if idx == 2 and user[2].upper() in ENW:
                    thisresult2=AlphaGuide.objects.get(id=188)
                    name = get_object_or_404(NameField, id=id)
                    this = thisresult2.attribute
                    name.thisresult2 = this
                    name.save()

                if idx == 2 and user[2].upper() in FOX:
                    thisresult2=AlphaGuide.objects.get(id=189)
                    name = get_object_or_404(NameField, id=id)
                    this = thisresult2.attribute
                    name.thisresult2 = this
                    name.save()
            
                if idx == 2 and user[2].upper() in GPY:
                    thisresult2=AlphaGuide.objects.get(id=190)
                    name = get_object_or_404(NameField, id=id)
                    this = thisresult2.attribute
                    name.thisresult2 = this
                    name.save()
            
                if idx == 2 and user[2].upper() in HQZ:
                    thisresult2=AlphaGuide.objects.get(id=191)
                    name = get_object_or_404(NameField, id=id)
                    this = thisresult2.attribute
                    name.thisresult2 = this
                    name.save()
                if idx == 2 and user[2].upper() in IR:
                    thisresult2=AlphaGuide.objects.get(id=192)
                    name = get_object_or_404(NameField, id=id)
                    this = thisresult2.attribute
                    name.thisresult2 = this
                    name.save()

                if idx == 3 and user[3].upper() in AJS:
                    thisresult3= AlphaGuide.objects.get(id=193)
                    name = get_object_or_404(NameField, id=id)
                    this = thisresult3.attribute
                    name.thisresult3 = this
                    name.save()
            
                if idx == 3 and user[3].upper() in BT:
                    thisresult3= AlphaGuide.objects.get(id=194)
                    name = get_object_or_404(NameField, id=id)
                    this = thisresult3.attribute
                    name.thisresult3 = this
                    name.save()
            
                if idx == 3 and user[3].upper() in CLU:
                    thisresult3= AlphaGuide.objects.get(id=195)
                    name = get_object_or_404(NameField, id=id)
                    this = thisresult3.attribute
                    name.thisresult3 = this
                    name.save()
            
                if idx == 3 and user[3].upper() in DMV:
                    thisresult3= AlphaGuide.objects.get(id=196)
                    name = get_object_or_404(NameField, id=id)
                    this = thisresult3.attribute
                    name.thisresult3 = this
                    name.save()
            
                if idx == 3 and user[3].upper() in ENW:
                    thisresult3= AlphaGuide.objects.get(id=197)
                    name = get_object_or_404(NameField, id=id)
                    this = thisresult3.attribute
                    name.thisresult3 = this
                    name.save()
            
                if idx == 3 and user[3].upper() in FOX:
                    thisresult3= AlphaGuide.objects.get(id=198)
                    name = get_object_or_404(NameField, id=id)
                    this = thisresult3.attribute
                    name.thisresult3 = this
                    name.save()
            
                if idx == 3 and user[3].upper() in GPY:
                    thisresult3= AlphaGuide.objects.get(id=199)
                    name = get_object_or_404(NameField, id=id)
                    this = thisresult3.attribute
                    name.thisresult3 = this
                    name.save()
            
                if idx == 3 and user[3].upper() in HQZ:
                    thisresult3= AlphaGuide.objects.get(id=200)
                    name = get_object_or_404(NameField, id=id)
                    this = thisresult3.attribute
                    name.thisresult3 = this
                    name.save()
            
                if idx == 3 and user[3].upper() in IR:
                    thisresult3= AlphaGuide.objects.get(id=201)
                    name = get_object_or_404(NameField, id=id)
                    this = thisresult3.attribute
                    name.thisresult3 = this
                    name.save()
            
                if  idx == 4 and user[4].upper() in AJS:
                    thisresult4= AlphaGuide.objects.get(id=202)
                    name = get_object_or_404(NameField, id=id)
                    this = thisresult4.attribute
                    name.thisresult4 = this
                    name.save()
            

                if idx == 4 and user[4].upper() in BT:
                    thisresult4= AlphaGuide.objects.get(id=203)
                    name = get_object_or_404(NameField, id=id)
                    this = thisresult4.attribute
                    name.thisresult4 = this
                    name.save()
            
                if idx == 4 and user[4].upper() in CLU:
                    thisresult4= AlphaGuide.objects.get(id=204)
                    name = get_object_or_404(NameField, id=id)
                    this = thisresult4.attribute
                    name.thisresult4 = this
                    name.save()
            
                if idx == 4 and user[4].upper() in DMV:
                    thisresult4= AlphaGuide.objects.get(id=205)
                    name = get_object_or_404(NameField, id=id)
                    this = thisresult4.attribute
                    name.thisresult4 = this
                    name.save()
            
                if idx == 4 and user[4].upper() in ENW:
                    thisresult4= AlphaGuide.objects.get(id=206)
                    name = get_object_or_404(NameField, id=id)
                    this = thisresult4.attribute
                    name.thisresult4 = this
                    name.save()
            
                if idx == 4 and user[4].upper() in FOX:
                    thisresult4= AlphaGuide.objects.get(id=207)
                    name = get_object_or_404(NameField, id=id)
                    this = thisresult4.attribute
                    name.thisresult4 = this
                    name.save()
            
                if idx == 4 and user[4].upper() in GPY:
                    thisresult4= AlphaGuide.objects.get(id=208)
                    name = get_object_or_404(NameField, id=id)
                    this = thisresult4.attribute
                    name.thisresult4 = this
                    name.save()
            
                if idx == 4 and user[4].upper() in HQZ:
                    thisresult4= AlphaGuide.objects.get(id=209)
                    name = get_object_or_404(NameField, id=id)
                    this = thisresult4.attribute
                    name.thisresult4 = this
                    name.save()
            
                if idx == 4 and user[4].upper() in IR:
                    thisresult4= AlphaGuide.objects.get(id=210)
                    name = get_object_or_404(NameField, id=id)
                    this = thisresult4.attribute
                    name.thisresult4 = this
                    name.save()

                if idx == 5 and user[5].upper() in AJS:
                    thisresult5= AlphaGuide.objects.get(id=211)
                    name = get_object_or_404(NameField, id=id)
                    this = thisresult5.attribute
                    name.thisresult5 = this
                    name.save()
            
                if idx == 5 and user[5].upper() in BT:
                    thisresult5= AlphaGuide.objects.get(id=212)
                    name = get_object_or_404(NameField, id=id)
                    this = thisresult5.attribute
                    name.thisresult5 = this
                    name.save()
            
                if idx == 5 and user[5].upper() in CLU:
                    thisresult5= AlphaGuide.objects.get(id=213)
                    name = get_object_or_404(NameField, id=id)
                    this = thisresult5.attribute
                    name.thisresult5 = this
                    name.save()
            
                if idx == 5 and user[5].upper() in DMV:
                    thisresult5= AlphaGuide.objects.get(id=214)
                    name = get_object_or_404(NameField, id=id)
                    this = thisresult5.attribute
                    name.thisresult5 = this
                    name.save()
            
                if idx == 5 and user[5].upper() in ENW:
                    thisresult5= AlphaGuide.objects.get(id=215)
                    name = get_object_or_404(NameField, id=id)
                    this = thisresult5.attribute
                    name.thisresult5 = this
                    name.save()
            
                if idx == 5 and user[5].upper() in FOX:
                    thisresult5= AlphaGuide.objects.get(id=216)
                    name = get_object_or_404(NameField, id=id)
                    this = thisresult5.attribute
                    name.thisresult5 = this
                    name.save()
            
                if idx == 5 and user[5].upper() in GPY:
                    thisresult5= AlphaGuide.objects.get(id=217)
                    name = get_object_or_404(NameField, id=id)
                    this = thisresult5.attribute
                    name.thisresult5 = this
                    name.save()
            
                if idx == 5 and user[5].upper() in HQZ:
                    thisresult5= AlphaGuide.objects.get(id=218)
                    name = get_object_or_404(NameField, id=id)
                    this = thisresult5.attribute
                    name.thisresult5 = this
                    name.save()
            
                if idx == 6 and user[6].upper() in IR:
                    name = get_object_or_404(NameField, id=id)
                    thisresult5= AlphaGuide.objects.get(id=219)
                    this = thisresult5.attribute
                    name.thisresult5 = this
                    name.save()

                if idx == 6 and user[6].upper() in AJS:
                    thisresult6= AlphaGuide.objects.get(id=220)
                    name = get_object_or_404(NameField, id=id)
                    this = thisresult6.attribute
                    name.thisresult6 = this
                    name.save()
            
                if idx == 6 and user[6].upper() in BT:
                    thisresult6= AlphaGuide.objects.get(id=221)
                    name = get_object_or_404(NameField, id=id)
                    this = thisresult6.attribute
                    name.thisresult6 = this
                    name.save()
            
                if idx == 6 and user[6].upper() in CLU:
                    thisresult6= AlphaGuide.objects.get(id=222)
                    name = get_object_or_404(NameField, id=id)
                    this = thisresult6.attribute
                    name.thisresult6 = this
                    name.save()
            
                if idx == 6 and user[6].upper() in DMV:
                    thisresult6= AlphaGuide.objects.get(id=223)
                    name = get_object_or_404(NameField, id=id)
                    this = thisresult6.attribute
                    name.thisresult6 = this
                    name.save()
            
                if idx == 6 and user[6].upper() in ENW:
                    thisresult6= AlphaGuide.objects.get(id=224)
                    name = get_object_or_404(NameField, id=id)
                    this = thisresult6.attribute
                    name.thisresult6 = this
                    name.save()
            
                if idx == 6 and user[6].upper() in FOX:
                    thisresult6= AlphaGuide.objects.get(id=225)
                    name = get_object_or_404(NameField, id=id)
                    this = thisresult6.attribute
                    name.thisresult6 = this
                    name.save()
        
                if idx == 6 and user[6].upper() in GPY:
                    thisresult6= AlphaGuide.objects.get(id=226)
                    name = get_object_or_404(NameField, id=id)
                    this = thisresult6.attribute
                    name.thisresult6 = this
                    name.save()
            
                if idx == 6 and user[6].upper() in HQZ:
                    thisresult6= AlphaGuide.objects.get(id=227)
                    name = get_object_or_404(NameField, id=id)
                    this = thisresult6.attribute
                    name.thisresult6 = this
                    name.save()
                    return render(request,'results.html')
                if idx == 6 and user[6].upper() in IR:
                    thisresult6= AlphaGuide.objects.get(id=228)
                    name = get_object_or_404(NameField, id=id)
                    this = thisresult6.attribute
                    name.thisresult6 = this
                    name.save()
                if idx == 7 and user[7].upper() in AJS:
                    thisresult7= AlphaGuide.objects.get(id=229)
                    name = get_object_or_404(NameField, id=id)
                    this = thisresult7.attribute
                    name.thisresult7 = this
                    name.save()
                    return render(request,'results.html')
                if idx == 7 and user[7].upper() in BT:
                    thisresult7= AlphaGuide.objects.get(id=230)
                    name = get_object_or_404(NameField, id=id)
                    this = thisresult7.attribute
                    name.thisresult7 = this
                    name.save()
                if idx == 7 and user[7].upper() in CLU:
                    thisresult7= AlphaGuide.objects.get(id=231)
                    name = get_object_or_404(NameField, id=id)
                    this = thisresult7.attribute
                    name.thisresult7 = this
                    name.save()
                    return render(request,'results.html',{'name':name})
                if idx == 7 and user[7].upper() in DMV:
                    thisresult7= AlphaGuide.objects.get(id=232)
                    name = get_object_or_404(NameField, id=id)
                    this = thisresult7.attribute
                    name.thisresult7 = this
                    name.save()
                # return render(request,'results.html',{'name':name})
                if idx == 7 and user[7].upper() in ENW:
                    thisresult7= AlphaGuide.objects.get(id=233)
                    name = get_object_or_404(NameField, id=id)
                    this = thisresult7.attribute
                    name.thisresult7 = this
                    name.save()
            # return render(request,'results.html',{'name':name})
                if idx == 7 and user[7].upper() in FOX:
                    thisresult7= AlphaGuide.objects.get(id=234)
                    name = get_object_or_404(NameField, id=id)
                    this = thisresult7.attribute
                    name.thisresult7 = this
                    name.save()
                # return render(request,'results.html',{'name':name})
                if idx == 7 and user[7].upper() in GPY:
                    thisresult7= AlphaGuide.objects.get(id=235)
                    name = get_object_or_404(NameField, id=id)
                    this = thisresult7.attribute
                    name.thisresult7 = this
                    name.save()
            # return render(request,'results.html',{'name':name})
                if idx == 7 and user[7].upper() in HQZ:
                    thisresult7= AlphaGuide.objects.get(id=236)
                    name = get_object_or_404(NameField, id=id)
                    this = thisresult7.attribute
                    name.thisresult7 = this
                    name.save()
            # return render(request,'results.html',{'name':name})
                if idx == 7 and user[7].upper() in IR:
                    thisresult7= AlphaGuide.objects.get(id=237)
                    name = get_object_or_404(NameField, id=id)
                    this = thisresult7.attribute
                    name.thisresult7 = this
                    name.save()

                if idx == 8 and user[8].upper() in AJS:
                    thisresult8= AlphaGuide.objects.get(id=238)
                    name = get_object_or_404(NameField, id=id)
                    this = thisresult8.attribute
                    name.thisresult8 = this
                    name.save()
            # return render(request,'results.html',{'name':name})
                if idx == 8 and user[8].upper() in BT:
                    thisresult8= AlphaGuide.objects.get(id=239)
                    name = get_object_or_404(NameField, id=id)
                    this = thisresult8.attribute
                    name.thisresult8 = this
                    name.save()
            # return render(request,'results.html',{'name':name})
                if idx == 8 and user[8].upper() in CLU:
                    thisresult8= AlphaGuide.objects.get(id=240)
                    name = get_object_or_404(NameField, id=id)
                    this = thisresult8.attribute
                    name.thisresult8 = this
                    name.save()
            # return render(request,'results.html',{'name':name})
                if idx == 8 and user[8].upper() in DMV:
                    thisresult8= AlphaGuide.objects.get(id=241)
                    name = get_object_or_404(NameField, id=id)
                    this = thisresult8.attribute
                    name.thisresult8 = this
                    name.save()
            # return render(request,'results.html',{'name':name})
                if idx == 8 and user[8].upper() in ENW:
                    thisresult8= AlphaGuide.objects.get(id=242)
                    name = get_object_or_404(NameField, id=id)
                    this = thisresult8.attribute
                    name.thisresult8 = this
                    name.save()
            # return render(request,'results.html',{'name':name})
                if idx == 8 and user[8].upper() in FOX:
                    thisresult8= AlphaGuide.objects.get(id=243)
                    name = get_object_or_404(NameField, id=id)
                    this = thisresult8.attribute
                    name.thisresult8 = this
                    name.save()
            # return render(request,'results.html',{'name':name})
                if idx == 8 and user[8].upper() in GPY:
                    thisresult8= AlphaGuide.objects.get(id=244)
                    name = get_object_or_404(NameField, id=id)
                    this = thisresult8.attribute
                    name.thisresult8 = this
                    name.save()
                # return render(request,'results.html',{'name':name})
                if idx == 8 and user[8].upper() in HQZ:
                    thisresult8= AlphaGuide.objects.get(id=245)
                    name = get_object_or_404(NameField, id=id)
                    this = thisresult8.attribute
                    name.thisresult8 = this
                    name.save()
                    # return render(request,'results.html',{'name':name})
                if idx == 8 and user[8].upper() in IR:
                    thisresult8= AlphaGuide.objects.get(id=246)
                    name = get_object_or_404(NameField, id=id)
                    this = thisresult8.attribute
                    name.thisresult8 = this
                    name.save()
            return render(request,'results.html',{'name':name})
            # return render(request, 'results.html',)
        else:
            pass
        return render(request,'results.html',{'name':name})

        


    
            
        

        
        
        
        
        
       
        
     

