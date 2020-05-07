from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from account.forms import RegistrationForm, AccountAuthenticationForm, AccountUpdateForm

from .models import Student
from school.models import School
from department.models import Department
from dptclass.models import DptClass
from account.forms import CreateStdForm

def detail_std(request, id=None):
    form = CreateStdForm()
    std = Student.objects.filter(pk=id)
    return render(request, "detail_std.html", {'form': form, 'std': std})

def list_std(request):
    form = CreateStdForm()
    stds = Student.objects.all()
    return render(request, "list_std.html", {'form': form, 'stds': stds})

def load_schools(request):
    inst_id = request.GET.get('inst')
    schools = School.objects.filter(sch_inst=1).order_by('sch_name')
    return render(request, 'load_school.html', {'schools': schools})

def load_depts(request):
    sch_id = request.GET.get('sch')
    depts = Department.objects.filter(dept_sch=sch_id).order_by('dept_name')
    return render(request, 'load_dept.html', {'depts': depts})

def load_deptcls(request):
    dept_id = request.GET.get('dept')
    deptcls = DptClass.objects.filter(dptcls_dpt=dept_id).order_by('dptcls_name')
    return render(request, 'load_deptcl.html', {'deptcls': deptcls})




def registration_view(request):
	context = {}
	if request.POST:
		form = RegistrationForm(request.POST)
		if form.is_valid():
			print(request.POST)
			form.save()
			email = form.cleaned_data.get('email')
			raw_password = form.cleaned_data.get('password1')
			account = authenticate(email=email, password=raw_password)
			login(request, account)
			return redirect('list_inst')
		else:
			context['registration_form'] = form

	else:
		form = RegistrationForm()
		context['registration_form'] = form
	return render(request, 'account/register.html', context)


def logout_view(request):
	logout(request)
	return redirect('/')


def login_view(request):
	context = {}
	user = request.user
	if user.is_authenticated: 
		return redirect("list_inst")

	if request.POST:
		form = AccountAuthenticationForm(request.POST)
		if form.is_valid():
			print(request.POST)
			email = request.POST['email']
			password = request.POST['password']
			user = authenticate(email=email, password=password)

			if user:
				login(request, user)
				return redirect("list_inst")

	else:
		form = AccountAuthenticationForm()

	context['login_form'] = form

	# print(form)
	return render(request, "account/login.html", context)


def account_view(request):

	if not request.user.is_authenticated:
			return redirect("login")

	context = {}
	if request.POST:
		form = AccountUpdateForm(request.POST, instance=request.user)
		if form.is_valid():
			form.initial = {
					"email": request.POST['email'],
					"username": request.POST['username'],
			}
			form.save()
			context['success_message'] = "Updated"
	else:
		form = AccountUpdateForm(

			initial={
					"email": request.user.email, 
					"username": request.user.username,
				}
			)

	context['account_form'] = form

	return render(request, "account/account.html", context)


def must_authenticate_view(request):
	return render(request, 'account/must_authenticate.html', {})


