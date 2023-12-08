from django.shortcuts import render,HttpResponse,redirect
from .models import sadman,product2,orders
from math import ceil

# Create your views here.
def userwork(request):

  return render(request,'userwork.html')


def Header(request):
 
    allProds=[]
    catprods= product2.objects.values('category', 'id')
    cats= {item["category"] for item in catprods}
    for cat in cats:
        prod=product2.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])

    params={'allProds':allProds }
    return render(request,"Home.html", params)







def about1(request):
   return render(request,'Header.html')
def basic1(request):
   return render(request,'basic.html')
def AboutUs(request):
   return render(request,'AboutUs.html')
def loginpage(request):
   return render(request,'login.html')
def contractpage(request):
   return render(request,'contract.html')
def footerpage(request):
   return render(request,'footer.html')
def cheakoutpage(request):

   if request.method=="POST":
     
      name=request.POST.get('name','')
      email=request.POST.get('email','')
      phone_no=request.POST.get('phone_no','')
      address=request.POST.get('address','')
      city=request.POST.get('city','')
      state=request.POST.get('state','')

      order=orders(name=name,email=email,phone_no=phone_no,address=address,city=city,state=state)
      if name and email and phone_no and address and city and state is not None:
          order.save()
          return redirect('Home')
      else:
         return HttpResponse('please fill all the field')

      
         



   return render(request,'cheakout.html')