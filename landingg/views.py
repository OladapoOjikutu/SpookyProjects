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
                    thisresult2= AlphaGuide.objects.get(id=234)
                    this = thisresult2.attribute
                    name.thisresult = this
                    name.save()
                if idx == 0 and user[0].upper() in BT:
                    name = get_object_or_404(NameField, id=id)
                    thisresult= AlphaGuide.objects.get(id=235)
                    this = thisresult.attribute
                    name.thisresult = this
                    name.save()
                
                if idx == 0 and user[0].upper() in CLU:
                    name = get_object_or_404(NameField, id=id)
                    thisresult= AlphaGuide.objects.get(id=236)
                    this = thisresult.attribute
                    name.thisresult = this
                    name.save()
                
                if idx == 0 and user[0].upper() in DMV:
                    name = get_object_or_404(NameField, id=id)
                    thisresult= AlphaGuide.objects.get(id=237)
                    this = thisresult.attribute
                    name.thisresult = this
                    name.save()
                
                if idx == 0 and user[0].upper() in ENW:
                    name = get_object_or_404(NameField, id=id)
                    thisresult= AlphaGuide.objects.get(id=238)
                    this = thisresult.attribute
                    name.thisresult = this
                    name.save()
                
                if idx == 0 and user[0].upper() in FOX:
                    name = get_object_or_404(NameField, id=id)
                    thisresult= AlphaGuide.objects.get(id=239)
                    this = thisresult.attribute
                    name.thisresult = this
                    name.save()
                
                if idx == 0 and user[0].upper() in GPY:
                    name = get_object_or_404(NameField, id=id)
                    thisresult= AlphaGuide.objects.get(id=240)
                    this = thisresult.attribute
                    name.thisresult = this
                    name.save()
                if idx == 0 and user[0].upper() in HQZ:
                    name = get_object_or_404(NameField, id=id)
                    thisresult= AlphaGuide.objects.get(id=241)
                    this = thisresult.attribute
                    name.thisresult = this
                    name.save()
                if idx == 0 and user[0].upper() in IR:
                    name = get_object_or_404(NameField, id=id)
                    thisresult= AlphaGuide.objects.get(id=242)
                    this = thisresult.attribute
                    name.thisresult = this
                    name.save()
                # return render(request,'results.html')
            
                if idx == 1 and user[1].upper() in AJS:
                    name = get_object_or_404(NameField, id=id)
                    thisresult1= AlphaGuide.objects.get(id=243)
                    this = thisresult1.attribute
                    name.thisresult1 = this
                    name.save()

                if idx == 1 and user[1].upper() in BT:
                    name = get_object_or_404(NameField, id=id)
                    thisresult1= AlphaGuide.objects.get(id=244)
                    this = thisresult1.attribute
                    name.thisresult1 = this
                    name.save()

                if idx == 1 and user[1].upper() in CLU:
                    name = get_object_or_404(NameField, id=id)
                    thisresult1= AlphaGuide.objects.get(id=245)
                    this = thisresult1.attribute
                    name.thisresult1 = this
                    name.save()

                if idx == 1 and user[1].upper() in DMV:
                    name = get_object_or_404(NameField, id=id)
                    thisresult1= AlphaGuide.objects.get(id=246)
                    this = thisresult1.attribute
                    name.thisresult1 = this
                    name.save()

                if idx == 1 and user[1].upper() in ENW:
                    name = get_object_or_404(NameField, id=id)
                    thisresult1= AlphaGuide.objects.get(id=247)
                    this = thisresult1.attribute
                    name.thisresult1 = this
                    name.save()
            
                if idx == 1 and user[1].upper() in FOX:
                    name = get_object_or_404(NameField, id=id)
                    thisresult1= AlphaGuide.objects.get(id=248)
                    this = thisresult1.attribute
                    name.thisresult1 = this
                    name.save()
            
                if idx == 1 and user[1].upper() in GPY:
                    name = get_object_or_404(NameField, id=id)
                    thisresult1= AlphaGuide.objects.get(id=249)
                    this = thisresult1.attribute
                    name.thisresult1 = this
                    name.save()
            
                if idx == 1 and user[1].upper() in HQZ:
                    name = get_object_or_404(NameField, id=id)
                    thisresult1= AlphaGuide.objects.get(id=250)
                    this = thisresult1.attribute
                    name.thisresult1 = this
                    name.save()
            
                if idx == 1 and user[1].upper() in IR:
                    name = get_object_or_404(NameField, id=id)
                    thisresult1=  AlphaGuide.objects.get(id=251)
                    this = thisresult1.attribute
                    name.thisresult1 = this
                    name.save()
                
            
                if idx == 2 and user[2].upper() in AJS:
                    thisresult2= AlphaGuide.objects.get(id=252)
                    name = get_object_or_404(NameField, id=id)
                    this = thisresult2.attribute
                    name.thisresult2 = this
                    name.save()

                if idx == 2 and user[2].upper() in BT:
                    thisresult2=AlphaGuide.objects.get(id=253)
                    name = get_object_or_404(NameField, id=id)
                    this = thisresult2.attribute
                    name.thisresult2 = this
                    name.save()
            
                if idx == 2 and user[2].upper() in CLU:
                    thisresult2=AlphaGuide.objects.get(id=254)
                    name = get_object_or_404(NameField, id=id)
                    this = thisresult2.attribute
                    name.thisresult2 = this
                    name.save()
            
                if idx == 2 and user[2].upper() in DMV:
                    thisresult2=AlphaGuide.objects.get(id=255)
                    name = get_object_or_404(NameField, id=id)
                    this = thisresult2.attribute
                    name.thisresult2 = this
                    name.save()
            
                if idx == 2 and user[2].upper() in ENW:
                    thisresult2=AlphaGuide.objects.get(id=265)
                    name = get_object_or_404(NameField, id=id)
                    this = thisresult2.attribute
                    name.thisresult2 = this
                    name.save()

                if idx == 2 and user[2].upper() in FOX:
                    thisresult2=AlphaGuide.objects.get(id=257)
                    name = get_object_or_404(NameField, id=id)
                    this = thisresult2.attribute
                    name.thisresult2 = this
                    name.save()
            
                if idx == 2 and user[2].upper() in GPY:
                    thisresult2=AlphaGuide.objects.get(id=258)
                    name = get_object_or_404(NameField, id=id)
                    this = thisresult2.attribute
                    name.thisresult2 = this
                    name.save()
            
                if idx == 2 and user[2].upper() in HQZ:
                    thisresult2=AlphaGuide.objects.get(id=259)
                    name = get_object_or_404(NameField, id=id)
                    this = thisresult2.attribute
                    name.thisresult2 = this
                    name.save()
                if idx == 2 and user[2].upper() in IR:
                    thisresult2=AlphaGuide.objects.get(id=260)
                    name = get_object_or_404(NameField, id=id)
                    this = thisresult2.attribute
                    name.thisresult2 = this
                    name.save()

                if idx == 3 and user[3].upper() in AJS:
                    thisresult3= AlphaGuide.objects.get(id=262)
                    name = get_object_or_404(NameField, id=id)
                    this = thisresult3.attribute
                    name.thisresult3 = this
                    name.save()
            
                if idx == 3 and user[3].upper() in BT:
                    thisresult3= AlphaGuide.objects.get(id=263)
                    name = get_object_or_404(NameField, id=id)
                    this = thisresult3.attribute
                    name.thisresult3 = this
                    name.save()
            
                if idx == 3 and user[3].upper() in CLU:
                    thisresult3= AlphaGuide.objects.get(id=264)
                    name = get_object_or_404(NameField, id=id)
                    this = thisresult3.attribute
                    name.thisresult3 = this
                    name.save()
            
                if idx == 3 and user[3].upper() in DMV:
                    thisresult3= AlphaGuide.objects.get(id=265)
                    name = get_object_or_404(NameField, id=id)
                    this = thisresult3.attribute
                    name.thisresult3 = this
                    name.save()
            
                if idx == 3 and user[3].upper() in ENW:
                    thisresult3= AlphaGuide.objects.get(id=266)
                    name = get_object_or_404(NameField, id=id)
                    this = thisresult3.attribute
                    name.thisresult3 = this
                    name.save()
            
                if idx == 3 and user[3].upper() in FOX:
                    thisresult3= AlphaGuide.objects.get(id=267)
                    name = get_object_or_404(NameField, id=id)
                    this = thisresult3.attribute
                    name.thisresult3 = this
                    name.save()
            
                if idx == 3 and user[3].upper() in GPY:
                    thisresult3= AlphaGuide.objects.get(id=268)
                    name = get_object_or_404(NameField, id=id)
                    this = thisresult3.attribute
                    name.thisresult3 = this
                    name.save()
            
                if idx == 3 and user[3].upper() in HQZ:
                    thisresult3= AlphaGuide.objects.get(id=269)
                    name = get_object_or_404(NameField, id=id)
                    this = thisresult3.attribute
                    name.thisresult3 = this
                    name.save()
            
                if idx == 3 and user[3].upper() in IR:
                    thisresult3= AlphaGuide.objects.get(id=270)
                    name = get_object_or_404(NameField, id=id)
                    this = thisresult3.attribute
                    name.thisresult3 = this
                    name.save()
            
                if  idx == 4 and user[4].upper() in AJS:
                    thisresult4= AlphaGuide.objects.get(id=271)
                    name = get_object_or_404(NameField, id=id)
                    this = thisresult4.attribute
                    name.thisresult4 = this
                    name.save()
            

                if idx == 4 and user[4].upper() in BT:
                    thisresult4= AlphaGuide.objects.get(id=272)
                    name = get_object_or_404(NameField, id=id)
                    this = thisresult4.attribute
                    name.thisresult4 = this
                    name.save()
            
                if idx == 4 and user[4].upper() in CLU:
                    thisresult4= AlphaGuide.objects.get(id=273)
                    name = get_object_or_404(NameField, id=id)
                    this = thisresult4.attribute
                    name.thisresult4 = this
                    name.save()
            
                if idx == 4 and user[4].upper() in DMV:
                    thisresult4= AlphaGuide.objects.get(id=274)
                    name = get_object_or_404(NameField, id=id)
                    this = thisresult4.attribute
                    name.thisresult4 = this
                    name.save()
            
                if idx == 4 and user[4].upper() in ENW:
                    thisresult4= AlphaGuide.objects.get(id=275)
                    name = get_object_or_404(NameField, id=id)
                    this = thisresult4.attribute
                    name.thisresult4 = this
                    name.save()
            
                if idx == 4 and user[4].upper() in FOX:
                    thisresult4= AlphaGuide.objects.get(id=276)
                    name = get_object_or_404(NameField, id=id)
                    this = thisresult4.attribute
                    name.thisresult4 = this
                    name.save()
            
                if idx == 4 and user[4].upper() in GPY:
                    thisresult4= AlphaGuide.objects.get(id=277)
                    name = get_object_or_404(NameField, id=id)
                    this = thisresult4.attribute
                    name.thisresult4 = this
                    name.save()
            
                if idx == 4 and user[4].upper() in HQZ:
                    thisresult4= AlphaGuide.objects.get(id=278)
                    name = get_object_or_404(NameField, id=id)
                    this = thisresult4.attribute
                    name.thisresult4 = this
                    name.save()
            
                if idx == 4 and user[4].upper() in IR:
                    thisresult4= AlphaGuide.objects.get(id=279)
                    name = get_object_or_404(NameField, id=id)
                    this = thisresult4.attribute
                    name.thisresult4 = this
                    name.save()

                if idx == 5 and user[5].upper() in AJS:
                    thisresult5= AlphaGuide.objects.get(id=280)
                    name = get_object_or_404(NameField, id=id)
                    this = thisresult5.attribute
                    name.thisresult5 = this
                    name.save()
            
                if idx == 5 and user[5].upper() in BT:
                    thisresult5= AlphaGuide.objects.get(id=281)
                    name = get_object_or_404(NameField, id=id)
                    this = thisresult5.attribute
                    name.thisresult5 = this
                    name.save()
            
                if idx == 5 and user[5].upper() in CLU:
                    thisresult5= AlphaGuide.objects.get(id=282)
                    name = get_object_or_404(NameField, id=id)
                    this = thisresult5.attribute
                    name.thisresult5 = this
                    name.save()
            
                if idx == 5 and user[5].upper() in DMV:
                    thisresult5= AlphaGuide.objects.get(id=283)
                    name = get_object_or_404(NameField, id=id)
                    this = thisresult5.attribute
                    name.thisresult5 = this
                    name.save()
            
                if idx == 5 and user[5].upper() in ENW:
                    thisresult5= AlphaGuide.objects.get(id=284)
                    name = get_object_or_404(NameField, id=id)
                    this = thisresult5.attribute
                    name.thisresult5 = this
                    name.save()
            
                if idx == 5 and user[5].upper() in FOX:
                    thisresult5= AlphaGuide.objects.get(id=285)
                    name = get_object_or_404(NameField, id=id)
                    this = thisresult5.attribute
                    name.thisresult5 = this
                    name.save()
            
                if idx == 5 and user[5].upper() in GPY:
                    thisresult5= AlphaGuide.objects.get(id=286)
                    name = get_object_or_404(NameField, id=id)
                    this = thisresult5.attribute
                    name.thisresult5 = this
                    name.save()
            
                if idx == 5 and user[5].upper() in HQZ:
                    thisresult5= AlphaGuide.objects.get(id=287)
                    name = get_object_or_404(NameField, id=id)
                    this = thisresult5.attribute
                    name.thisresult5 = this
                    name.save()
            
                if idx == 6 and user[6].upper() in IR:
                    name = get_object_or_404(NameField, id=id)
                    thisresult5= AlphaGuide.objects.get(id=288)
                    this = thisresult5.attribute
                    name.thisresult5 = this
                    name.save()

                if idx == 6 and user[6].upper() in AJS:
                    thisresult6= AlphaGuide.objects.get(id=289)
                    name = get_object_or_404(NameField, id=id)
                    this = thisresult6.attribute
                    name.thisresult6 = this
                    name.save()
            
                if idx == 6 and user[6].upper() in BT:
                    thisresult6= AlphaGuide.objects.get(id=270)
                    name = get_object_or_404(NameField, id=id)
                    this = thisresult6.attribute
                    name.thisresult6 = this
                    name.save()
            
                if idx == 6 and user[6].upper() in CLU:
                    thisresult6= AlphaGuide.objects.get(id=271)
                    name = get_object_or_404(NameField, id=id)
                    this = thisresult6.attribute
                    name.thisresult6 = this
                    name.save()
            
                if idx == 6 and user[6].upper() in DMV:
                    thisresult6= AlphaGuide.objects.get(id=272)
                    name = get_object_or_404(NameField, id=id)
                    this = thisresult6.attribute
                    name.thisresult6 = this
                    name.save()
            
                if idx == 6 and user[6].upper() in ENW:
                    thisresult6= AlphaGuide.objects.get(id=273)
                    name = get_object_or_404(NameField, id=id)
                    this = thisresult6.attribute
                    name.thisresult6 = this
                    name.save()
            
                if idx == 6 and user[6].upper() in FOX:
                    thisresult6= AlphaGuide.objects.get(id=274)
                    name = get_object_or_404(NameField, id=id)
                    this = thisresult6.attribute
                    name.thisresult6 = this
                    name.save()
        
                if idx == 6 and user[6].upper() in GPY:
                    thisresult6= AlphaGuide.objects.get(id=275)
                    name = get_object_or_404(NameField, id=id)
                    this = thisresult6.attribute
                    name.thisresult6 = this
                    name.save()
            
                if idx == 6 and user[6].upper() in HQZ:
                    thisresult6= AlphaGuide.objects.get(id=276)
                    name = get_object_or_404(NameField, id=id)
                    this = thisresult6.attribute
                    name.thisresult6 = this
                    name.save()
                    return render(request,'results.html')
                if idx == 6 and user[6].upper() in IR:
                    thisresult6= AlphaGuide.objects.get(id=277)
                    name = get_object_or_404(NameField, id=id)
                    this = thisresult6.attribute
                    name.thisresult6 = this
                    name.save()
                if idx == 7 and user[7].upper() in AJS:
                    thisresult7= AlphaGuide.objects.get(id=288)
                    name = get_object_or_404(NameField, id=id)
                    this = thisresult7.attribute
                    name.thisresult7 = this
                    name.save()
                    return render(request,'results.html')
                if idx == 7 and user[7].upper() in BT:
                    thisresult7= AlphaGuide.objects.get(id=289)
                    name = get_object_or_404(NameField, id=id)
                    this = thisresult7.attribute
                    name.thisresult7 = this
                    name.save()
                if idx == 7 and user[7].upper() in CLU:
                    thisresult7= AlphaGuide.objects.get(id=290)
                    name = get_object_or_404(NameField, id=id)
                    this = thisresult7.attribute
                    name.thisresult7 = this
                    name.save()
                    return render(request,'results.html',{'name':name})
                if idx == 7 and user[7].upper() in DMV:
                    thisresult7= AlphaGuide.objects.get(id=291)
                    name = get_object_or_404(NameField, id=id)
                    this = thisresult7.attribute
                    name.thisresult7 = this
                    name.save()
                # return render(request,'results.html',{'name':name})
                if idx == 7 and user[7].upper() in ENW:
                    thisresult7= AlphaGuide.objects.get(id=292)
                    name = get_object_or_404(NameField, id=id)
                    this = thisresult7.attribute
                    name.thisresult7 = this
                    name.save()
            # return render(request,'results.html',{'name':name})
                if idx == 7 and user[7].upper() in FOX:
                    thisresult7= AlphaGuide.objects.get(id=293)
                    name = get_object_or_404(NameField, id=id)
                    this = thisresult7.attribute
                    name.thisresult7 = this
                    name.save()
                # return render(request,'results.html',{'name':name})
                if idx == 7 and user[7].upper() in GPY:
                    thisresult7= AlphaGuide.objects.get(id=294)
                    name = get_object_or_404(NameField, id=id)
                    this = thisresult7.attribute
                    name.thisresult7 = this
                    name.save()
            # return render(request,'results.html',{'name':name})
                if idx == 7 and user[7].upper() in HQZ:
                    thisresult7= AlphaGuide.objects.get(id=295)
                    name = get_object_or_404(NameField, id=id)
                    this = thisresult7.attribute
                    name.thisresult7 = this
                    name.save()
            # return render(request,'results.html',{'name':name})
                if idx == 7 and user[7].upper() in IR:
                    thisresult7= AlphaGuide.objects.get(id=296)
                    name = get_object_or_404(NameField, id=id)
                    this = thisresult7.attribute
                    name.thisresult7 = this
                    name.save()

                if idx == 8 and user[8].upper() in AJS:
                    thisresult8= AlphaGuide.objects.get(id=297)
                    name = get_object_or_404(NameField, id=id)
                    this = thisresult8.attribute
                    name.thisresult8 = this
                    name.save()
            # return render(request,'results.html',{'name':name})
                if idx == 8 and user[8].upper() in BT:
                    thisresult8= AlphaGuide.objects.get(id=298)
                    name = get_object_or_404(NameField, id=id)
                    this = thisresult8.attribute
                    name.thisresult8 = this
                    name.save()
            # return render(request,'results.html',{'name':name})
                if idx == 8 and user[8].upper() in CLU:
                    thisresult8= AlphaGuide.objects.get(id=299)
                    name = get_object_or_404(NameField, id=id)
                    this = thisresult8.attribute
                    name.thisresult8 = this
                    name.save()
            # return render(request,'results.html',{'name':name})
                if idx == 8 and user[8].upper() in DMV:
                    thisresult8= AlphaGuide.objects.get(id=300)
                    name = get_object_or_404(NameField, id=id)
                    this = thisresult8.attribute
                    name.thisresult8 = this
                    name.save()
            # return render(request,'results.html',{'name':name})
                if idx == 8 and user[8].upper() in ENW:
                    thisresult8= AlphaGuide.objects.get(id=301)
                    name = get_object_or_404(NameField, id=id)
                    this = thisresult8.attribute
                    name.thisresult8 = this
                    name.save()
            # return render(request,'results.html',{'name':name})
                if idx == 8 and user[8].upper() in FOX:
                    thisresult8= AlphaGuide.objects.get(id=302)
                    name = get_object_or_404(NameField, id=id)
                    this = thisresult8.attribute
                    name.thisresult8 = this
                    name.save()
            # return render(request,'results.html',{'name':name})
                if idx == 8 and user[8].upper() in GPY:
                    thisresult8= AlphaGuide.objects.get(id=303)
                    name = get_object_or_404(NameField, id=id)
                    this = thisresult8.attribute
                    name.thisresult8 = this
                    name.save()
                # return render(request,'results.html',{'name':name})
                if idx == 8 and user[8].upper() in HQZ:
                    thisresult8= AlphaGuide.objects.get(id=304)
                    name = get_object_or_404(NameField, id=id)
                    this = thisresult8.attribute
                    name.thisresult8 = this
                    name.save()
                    # return render(request,'results.html',{'name':name})
                if idx == 8 and user[8].upper() in IR:
                    thisresult8= AlphaGuide.objects.get(id=305)
                    name = get_object_or_404(NameField, id=id)
                    this = thisresult8.attribute
                    name.thisresult8 = this
                    name.save()
            return render(request,'results.html',{'name':name})
            # return render(request, 'results.html',)
        else:
            pass
        return render(request,'results.html',{'name':name})

        
