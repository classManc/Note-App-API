from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from note_app.models import Note
from note_app.serializers import NoteSerializer
from django.contrib.auth.models import User


class NoteTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username="testuser", email="testuser@example.com", password="testpassword"
        )
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)
        self.note = Note.objects.create(
            title="Test Note", content="This is a test note.", user=self.user
        )
        self.valid_payload = {
            "title": "New Test Note",
            "content": "This is a new test note.",
        }
        self.invalid_payload = {
            "title": "",
            "content": "",
        }

    def test_create_valid_note(self):
        response = self.client.post(
            reverse("notes:note_list"), data=self.valid_payload, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_note(self):
        response = self.client.post(
            reverse("notes:note_list"), data=self.invalid_payload, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_all_notes(self):
        Note.objects.create(title="Test Note", content="Test content", user=self.user)
        Note.objects.create(
            title="Test Note 2", content="Test content 2", user=self.user
        )
        response = self.client.get(reverse("notes:note_list"))
        notes = response.data.get("results")  # extract just the list of notes
        serializer = NoteSerializer(Note.objects.all(), many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(notes, serializer.data)

    def test_get_single_note(self):
        response = self.client.get(
            reverse("notes:note_detail", kwargs={"pk": self.note.id})
        )
        note = Note.objects.get(pk=self.note.id)
        serializer = NoteSerializer(note)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_valid_note(self):
        response = self.client.put(
            reverse("notes:note_detail", kwargs={"pk": self.note.id}),
            data=self.valid_payload,
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_invalid_note(self):
        response = self.client.put(
            reverse("notes:note_detail", kwargs={"pk": self.note.id}),
            data=self.invalid_payload,
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_note(self):
        response = self.client.delete(
            reverse("notes:note_detail", kwargs={"pk": self.note.id})
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
