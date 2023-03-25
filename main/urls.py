from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("notes", views.notes, name="notes"),
    path("notes/<uuid>", views.notes_active, name="notes-active"),
    path("note-edit/<uuid>", views.note_edit, name="notes-edit"),
    path("notes-upload", views.note_upload, name="upload"),  
    path("note-del/<uuid>", views.notes_delete, name="notes-del"),
    path("note-delete/<uuid>", views.delete_notes, name="notes-delete"),
    
    path("tasks", views.tasks, name="tasks"),
    path("tasks/<uuid>", views.task_active, name="task-active"),
    path("task-create", views.task_create, name="task-create"),
    path("task-edit/<uuid>", views.task_edit, name="task-edit"),
    path("task-confirm/<uuid>", views.task_confirm, name="task-confirm"),

    path("signin", views.signin, name="signin"),
    path("signup", views.signup, name="signup"),
    path("logout", views.logout, name="logout")
]
