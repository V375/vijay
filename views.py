from django.shortcuts import render,redirect
from django.http import HttpResponse
from employee.models import employee
from employeer.models import employeer
from django.views.decorators.csrf import csrf_exempt
def HomePage(request):
	##first method
	employee_count = employee.objects.count() # show  the total no.of employee in table
	# employeer_count = employeer.objects.count()


	data = {
	  "employee_count":employee_count,
	  # "employeer_count": employeer_count,
	  }  
	return render(request,'index.html', data)

def employeeList(request):
	data = {
	'emp' : employee.objects.all()
	}
	return render(request,"employee.html", data)

# Create your views here.
def  employeer(request):
	return HttpResponse("you enter the employee")
@csrf_exempt
def Addemp(request):
	data = {
	"added":False,
	"message":"",
	"Employee":None
	}
	if request.method =="POST":
		input_data = request.POST
		print(input_data)

		if "id" in request.GET:
			#update
			if request.GET['id'] != "":
				emp = employee.objects.get(id=request.GET["id"])
				emp.name = input_data["name"]
				emp.email= input_data["email"]
				emp.address= input_data["address"]
				emp.phone = input_data["phone"]
				emp.save()
			else:
				emp = employee.objects.filter(email=input_data["email"])
				if emp:
					data["message"] = "This email is already exist"
				else:
					emp = employee(
						name = input_data["name"],
						email= input_data["email"],
						address= input_data["address"],
						phone= input_data["phone"],
						)
					emp.save()
				data["added"] = True
	if "id" in request.GET:
		try:
			data["Employee"] = employee.objects.get(id=request.GET["id"])
		except:
			pass
	return render(request,"addemployee.html", data)

@csrf_exempt
def employeedelete(request):
	id = request.GET["id"]
	emp = employee.objects.get(id= id)
	emp.delete()
	return redirect("/employee")








