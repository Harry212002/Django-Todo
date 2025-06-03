from django.shortcuts import redirect, render
from crud_app.models import tbl_Employee

# Create your views here.
def create(request):
    if request.method =="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        mobile_no=request.POST.get("mobile_no")        
        qs=tbl_Employee.objects.create(name=name,email=email,mobile_no=mobile_no)
        print(qs.id,"===========id \n\n")
        
        if qs:
            return redirect("/retrive/")
        
    else:
        return render(request,"create_emp.html")
        
def retrive_all_emp(request):
    qs=tbl_Employee.objects.all()
    context={
        "emp_data":qs
    }
    return render(request,"retrive.html",context)

def delete_emp(request,emp_id):
    print(emp_id)  
    qs=tbl_Employee.objects.filter(id=emp_id).delete()
    
    if qs:
        return redirect("/retrive/")
      
def update_emp(request,emp_id):
    if request.method =="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        mobile_no=request.POST.get("mobile_no") 
        qs=tbl_Employee.objects.filter(id=emp_id).update(name=name,email=email,mobile_no=mobile_no)
        
        if qs:
             return redirect("/retrive/")
           
    
    else:    
        qs=tbl_Employee.objects.get(id=emp_id)
        return render(request,"update.html",{"emp_update_data":qs})
        