from django.shortcuts import render, redirect, get_object_or_404

from .models import Institute
from school.models import School
from department.models import Department
from dptclass.models import DptClass
from course.models import Course


from institute.forms import CreateInstForm
from school.forms import CreateSchForm
from department.forms import CreateDeptForm
from dptclass.forms import CreateDptclsForm
from course.forms import CreateCrseForm

def list_inst(request):
    form = CreateInstForm()
    insts = Institute.objects.all()
    return render(request, "list_inst.html", {'form': form, 'insts': insts})

def list_sch(request, id):
    form = CreateSchForm()
    schs = School.objects.filter(sch_inst=id)
    return render(request, "list_sch.html", {'form': form, 'schs': schs}) 

def list_dept(request, id, sid):
    form = CreateDeptForm()
    dpts = Department.objects.filter(dpt_sch=sid)
    return render(request, "list_dept.html", {'form': form, 'dpts': dpts})

def list_dptcls(request, id, sid, did):
    form = CreateDptclsForm()
    dptclss = DptClass.objects.filter(dcls_dpt=did)
    return render(request, "list_dptcls.html", {'form': form, 'dptclss': dptclss}) 

def list_crse(request, id, sid, did, dcid):
    form = CreateCrseForm()
    crses = Course.objects.filter(ce_dptcls=dcid)
    return render(request, "list_crse.html", {'form': form, 'crses': crses}) 

def detail_crse(request, id, sid, did, dcid, cid):
    form = CreateCrseForm()
    dpts = Department.objects.filter(dpt_sch=sid)
    return render(request, "detail_crse.html", {'form': form, 'dpts': dpts}) 

def list_assess(request, id, sid):
    form = CreateDeptForm()
    dpts = Department.objects.filter(dpt_sch=sid)
    return render(request, "list_dept.html", {'form': form, 'dpts': dpts}) 