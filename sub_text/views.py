from django.shortcuts import render, redirect, HttpResponse
from sub_text.forms import SignupForm
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from sub_text.forms import studentform
from sub_text.models import signup, products, userrecord,contact





def home(request):
	return render(request, 'registration/index.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'registration/reg.html', {'form': form}) 

def img(request):
    if request.method == 'POST':
        form = studentform(request.POST,request.FILES) # A form
        if form.is_valid():
            form.save()
            return redirect('w1')
    else:
        form=studentform()
    return render(request, 'registration/img.html', {'form':form})



"""
def userfrm(request):
    if request.method == 'POST':
            
        form1 = userform(request.POST)
        if form1.is_valid():   
            u1 = form1.cleaned_data['username']
            u2 = form1.cleaned_data['first_name']
            u3 = form1.cleaned_data['last_name']
            u4 = form1.cleaned_data['email']
            u5 = form1.cleaned_data['password']
            uu = User.objects.create_user(username=u1,first_name=u2,last_name=u3,email=u4,password=u5)
            #uu.save()
             
            return redirect('log1')
    else:   
        form1 = userform()
    return render(request, 'registration/reg.html',{'form': form1})    
"""
def blocktry(request):
    return render(request,'sub_text/blocktry1.html')
    #return render(request,'song/blocktry2.html')     

def blocktry2(request):
    return render(request,'sub_text/blocktry2.html')

"""
def log(request): 
    if request.method == 'POST': 

        form = loginform(request.POST)
        if form.is_valid():
            u1= form.cleaned_data['name']
            u2= form.cleaned_data['password']
            user = authenticate(username=u1, password=u2)
            if user is not None:
                login(request, user)
                return redirect('index2')
            else:
                return redirect('log1') 
    else:
        form=loginform()   
    return render(request, 'sub_text/login3.html', {'form':form})                 
""" 

@login_required(login_url='log1')
def welcome(request):
    return render(request, 'registration/welcome.html')
"""
def logout1(request):
    logout(request)
    return redirect('log1')
"""
@login_required(login_url='log1')
def profile(request):
    args = {'user': request.user}
    return render(request, 'registration/profile.html')

@login_required(login_url='log1')
def about(request):
    return render(request, 'sub_text/about.html')    

@login_required(login_url ='log1')
def contact1(request):
    if request.method == 'POST':
        data1 = request.POST.get('name','')
        data2 = request.POST.get('phone','')
        data3 = request.POST.get('email','')
        data4 = request.POST.get('message','')
        aa = contact(name=data1,phone=data2,email=data3,message=data4)

        aa.save()        

        return render(request, 'sub_text/contact.html')
    else:
        return render(request, 'sub_text/contact.html')    


@login_required(login_url='log1')
def recipes(request):
    return render(request, 'sub_text/recipes.html') 

@login_required(login_url='log1')
def news(request):
    return render(request, 'sub_text/news.html')

@login_required(login_url='log1')
def services(request):
    return render(request, 'sub_text/services.html') 

@login_required(login_url='log1')
def single(request):
    return render(request, 'sub_text/single.html') 

def index2(request):
    return render(request, 'registration/index2.html')          

def qv1(request, ppid):
    pp = products.objects.get(pid=ppid)
    return render(request, 'sub_text/qv1.html', {'pp':pp})  

def addtocart(request, aid):
    #return HttpResponse("hi")
    if request.user.is_authenticated:
        userid = request.user.id
        pp = products.objects.get(pid=aid)
        uu = userrecord(uid=userid,  pid=pp.pid, pname=pp.pname, pimage=pp.pimage, pprice=pp.pprice)
        uu.save()
        return redirect('index2')                
    else:
        return redirect('login')    


def alldata(request):
    #return HttpResponse("hi")
    if request.user.is_authenticated:
        userid = request.user.id
        pp = userrecord.objects.filter(uid=userid)
        t=0.0        
        for i in pp:
            t=float(t)+float(i.pprice)

        paypal_dict={
            "business":"punnu4uu-facilitator@gmail.com",
            "amount": t,
            "currency_code":"INR",
            "item_name":"items added",
            "invoice":"unique-invoice-0001",
            "notify_url":"http://localhost:8000/home/a-very-hard-to-guess-url/",
            "return_url":"http://localhost:8000/home/paypal-return/",
            "cancel_return":"http://localhost:8000/home/paypal-cancel/",
        }
        form=PayPalPaymentsForm(initial=paypal_dict)
    #args['form']=form
    
        

        return render(request, 'sub_text/showdata.html', {'pp':pp, 'tp':t, 'form':form })  
                
    else:
        return redirect('login')    
def delete(request, did):
    #return HttpResponse("hi")
    if request.user.is_authenticated:
        userid = request.user.id
        pp = userrecord.objects.get(id=did).delete()

        return redirect('alldata1')    

    else:
        return redirect('login')    

def forget(request):
    return render(request, 'sub_text/forget.html')        

#=========================================


from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from paypal.standard.forms import PayPalPaymentsForm

def home1(request):
    #args={}
    
    paypal_dict={
        "business":"punnu4uu-facilitator@gmail.com",
        "amount":"01.00",
        "currency_code":"INR",
        "item_name":"Jot's LIVER",
        "invoice":"unique-invoice-0001",
        
        "notify_url":"http://localhost:8000/home/a-very-hard-to-guess-url/",
        "return_url":"http://localhost:8000/home/paypal-return/",
        "cancel_return":"http://localhost:8000/home/paypal-cancel/",
        }
    form=PayPalPaymentsForm(initial=paypal_dict)
    #args['form']=form
    context={"form":form}
    return render_to_response('sub_text/home1.html',context)
@csrf_exempt
def paypal_return(request):
    args={'post':request.POST,'get':request.GET}
    return render_to_response('sub_text/paypal_return.html',args)

def paypal_cancel(request):
    args={'post':request.POST,'get':request.GET}
    return render_to_response('sub_text/paypal_cancel.html',args)



#----------------------------


