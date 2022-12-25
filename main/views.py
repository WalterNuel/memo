from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.utils import timezone
from .models import Profile, Note, Task


from django.contrib.auth.decorators import login_required

# Create your views here.
def signin(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']

    user = auth.authenticate(username=username, password=password)

    if user is not None:
      auth.login(request, user)
      return redirect('index')
    else:
      messages.info(request, "Invalid Input")
      return render(request, 'signin.html')

  return render(request, 'signin.html')



def signup(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']
    password2 = request.POST['password2']

    if password == password2:
      if User.objects.filter(username=username).exists():
        messages.info(request, 'Username Taken')
        return redirect('signup')
      else:
        user = User.objects.create_user(username=username, password=password)
        user.save()

        user_login = auth.authenticate(username=username, password=password)
        auth.login(request, user_login)

        user_model = User.objects.get(username=username)
        new_profile = Profile.objects.create(username=user_model)
        new_profile.save()
        return redirect('index')
    else:
      messages.info(request, 'Passwords do not match')
      return redirect('signup')


  return render(request, 'signup.html')


@login_required(login_url='signin')
def logout(request):
  auth.logout(request)
  return redirect('signin')


@login_required(login_url='signin')
def index(request):
  user_acc = User.objects.get(username=request.user.username)
  user_profile = Profile.objects.get(username=user_acc)

  user_notes = Note.objects.filter(author=user_acc).order_by('-entry_date')
  user_tasks = Task.objects.filter(author=user_acc).order_by('-create')

  notes_length = len(user_notes)
  tasks_length = len(user_tasks)

  number_of_completed = Task.objects.filter(author=user_acc, completed=True)
  get_length = len(number_of_completed)

  context = {
    'user_acc':user_acc,
    'user_profile':user_profile,
    'user_notes':user_notes,
    'user_tasks':user_tasks,
    'length':get_length,
    'notes_length':notes_length,
    'tasks_length':tasks_length
  }

  return render(request, 'index.html', context)


@login_required(login_url='signin')
def tasks(request):
  user_acc = User.objects.get(username=request.user.username)
  user_profile = Profile.objects.get(username=user_acc)

  user_tasks = Task.objects.filter(author=user_acc).order_by('-create')

  tasks_length = len(user_tasks)

  number_of_completed = Task.objects.filter(author=user_acc, completed=True)
  get_length = len(number_of_completed)

  context = {
    'user_acc':user_acc,
    'user_profile':user_profile,
    'user_tasks':user_tasks,
    'length':get_length,
    'tasks_length':tasks_length
  }

  return render(request, 'tasksboard.html', context)


@login_required(login_url='signin')
def task_create(request):
  user_acc = User.objects.get(username=request.user.username)
  user_profile = Profile.objects.get(username=user_acc)

  if request.method == 'POST':
    task = request.POST['title']
    description = request.POST['description']

    new_task = Task.objects.create(author=user_acc, task=task, description=description)
    new_task.save()
    return redirect('tasks')


  context = {
    'user_acc':user_acc,
    'user_profile':user_profile,
  }

  return render(request, 'taskcreate.html', context)


@login_required(login_url='signin')
def notes(request):
  user_acc = User.objects.get(username=request.user.username)
  user_profile = Profile.objects.get(username=user_acc)

  user_notes = Note.objects.filter(author=user_acc).order_by('-entry_date')
  notes_length = 0
  
  context = {
    'user_acc':user_acc,
    'user_profile':user_profile,
    'user_notes':user_notes,
    'notes_length':notes_length
  }

  return render(request, 'notesboard.html', context)


@login_required(login_url='signin')
def note_upload(request):
  user_acc = User.objects.get(username=request.user.username)

  user_notes = Note.objects.filter(author=user_acc)
  notes_length = len(user_notes)

  author = User.objects.get(username=user_acc)
  title = f'New Note ({notes_length + 1})'
  note_text = ''
  entry_date = timezone.now()

  new_note = Note.objects.create(author=author, title=title, note_text=note_text, entry_date=entry_date)

  new_note.id

  return redirect('/notes/'+str(new_note.id))


@login_required(login_url='signin')
def note_edit(request, uuid):
  if request.method == 'POST':
    title = request.POST['title']
    note_text = request.POST['note_text']
    entry_date = timezone.now()

    note_save = Note.objects.get(id=uuid)
    note_save.title = title
    note_save.note_text = note_text
    note_save.entry_date = entry_date

    note_save.save()

    return redirect('/notes/'+str(note_save.id))

  else:
    note_save = Note.objects.get(id=uuid)

    return redirect('/notes/'+str(note_save.id))


@login_required(login_url='signin')
def task_confirm(request, uuid):
  task = Task.objects.get(id=uuid)
  
  if task.completed == True:
    task.completed = False
    task.save()
    return redirect('/')
  else:
    task.completed = True
    task.save()
    return redirect('/')


@login_required(login_url='signin')
def notes_active(request, uuid):
  user_acc = User.objects.get(username=request.user.username)
  user_profile = Profile.objects.get(username=user_acc)
  user_notes = Note.objects.filter(author=user_acc).order_by('-entry_date')
  active_note = Note.objects.get(id=uuid)
  
  context = {
    'user_acc':user_acc,
    'user_profile':user_profile,
    'user_notes':user_notes,
    'active_note':active_note,
  }

  return render(request, 'activenote.html', context)


@login_required(login_url='signin')
def task_active(request, uuid):
  user_acc = User.objects.get(username=request.user.username)
  user_profile = Profile.objects.get(username=user_acc)
  active = Task.objects.get(id=uuid)

  user_tasks = Task.objects.filter(author=user_acc).order_by('-create')

  tasks_length = len(user_tasks)

  number_of_completed = Task.objects.filter(author=user_acc, completed=True)
  get_length = len(number_of_completed)

  context = {
    'user_acc':user_acc,
    'user_profile':user_profile,
    'user_tasks':user_tasks,
    'length':get_length,
    'tasks_length':tasks_length,
    'active':active
  }

  return render(request, 'activetask.html', context)


@login_required(login_url='signin')
def notes_delete(request, uuid):
  note = Note.objects.get(id=uuid)
  note.delete()
  return redirect('notes')


@login_required(login_url='signin')
def delete_notes(request, uuid):
  note = Note.objects.get(id=uuid)
  note.delete()
  return redirect('/', messages.info(request, 'Note Deleted'))