from unicodedata import name
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from .models import TaskDay
from .forms import Task
# Create your views here.html+tab

deleted_tasks = []

def home(request):

	dane = TaskDay.objects.all()

	if len(deleted_tasks) > 7:

		deleted_tasks.remove(deleted_tasks[0])

	return render(request,'track_day/home.html',context={'data':dane,'deleted':deleted_tasks})

def log_in(request):


	if request.method == 'POST':

		nick = request.POST.get('log')
		passw = request.POST.get('pass')

		user = authenticate(request,username=nick,password=passw)

		if user is not None:

			login(request, user)

			return redirect('/')


	return render(request,'track_day/login.html')

def reg_ister(request):

	form = UserCreationForm()

	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid:
			form.save()
		return redirect('track_day:login')

	return render(request,'track_day/register.html',{'form':form})


def day(request):

	dane = TaskDay.objects.all()
	task_count = len(list(dane))

	return render(request,'track_day/Day.html',context={'data':dane,'task_count':task_count})

def add_task(request):

	form =Task()

	if request.method == 'POST':
		form = Task(request.POST)
		if form.is_valid():
			form.save()
			return redirect('track_day:day')

	return render(request, 'track_day/add_task.html',context={'form':form})

def delete_task(request):

	dane = TaskDay.objects.all()

	if request.method == 'POST':
		select_name = request.POST.get('delet',None)
		if select_name:
			for n in range(len(dane)):
				if str(dane[n]) == str(select_name):
					item_name = str(select_name)
					opo = TaskDay.objects.get(name=item_name)
					opo.delete()
			deleted_tasks.append(select_name)
	
	return render(request,'track_day/delete.html',context={'data':dane})

def id_day(request,pk):
	task = TaskDay.objects.get(pk=pk)
	return render(request,'track_day/id.html',context={'items':task})