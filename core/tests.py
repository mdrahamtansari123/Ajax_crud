from django.test import TestCase
from core.models import Post

# Create your tests here.
class AnimalTestCase(TestCase):
    def setUp(self):
        Post.objects.create(title="Rahamat", description="Ansari")
        Post.objects.create(title="Anuj", description="Kumar")

    def test_animals_can_speak(self):
        """Animals that can speak are correctly identified"""
        rahamat = Post.objects.get(name="Rahamat")
        ansari = Post.objects.get(name="Anuj")
        self.assertEqual(rahamat.speak(), 'The lion says "roar"')
        self.assertEqual(ansari.speak(), 'The cat says "meow"')