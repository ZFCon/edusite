from django.shortcuts import render, redirect, get_object_or_404

from account.models import Student
from student.forms import CreateStdForm

def list_std(request):
    form = CreateStdForm()
    stds = Student.objects.all()
    return render(request, "list_std.html", {'form': form, 'stds': stds})
