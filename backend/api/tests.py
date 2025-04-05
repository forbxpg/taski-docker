from http import HTTPStatus

from api.models import Task
from django.test import TestCase, Client


class TasksTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_tasks(self):
        response = self.client.get("/api/tasks/")
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_task_creation(self):
        response = self.client.post(
            "/api/tasks/",
            data={
                "title": "Test",
                "description": "Test",
            },
        )
        self.assertEqual(response.status_code, HTTPStatus.CREATED)
        self.assertTrue(Task.objects.filter(title="Test").exists())
