from django.urls import path
from .views import (homepage,
                    add_event,
                    update_event_completed,
                    event_delete)

app_name = "todo"

urlpatterns = [
    path('', homepage, name="home"),
    path('create/', add_event, name="create_event"),
    path('event-completed/<int:pk>/', update_event_completed, name="complete_event"),
    path('event/delete/<int:pk>/', event_delete, name="delete_event")
]