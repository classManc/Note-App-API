from django.urls import path

from .views import NoteDetail, NoteList

app_name = "note_app"


urlpatterns = [
    path("", NoteList.as_view(), name="note_list"),
    path("<int:pk>/", NoteDetail.as_view(), name="note_detail"),
]
