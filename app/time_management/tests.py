from django.test import TestCase

# Create your tests here.
from time_management.models import Worker


class SimpleTestCase(TestCase):

	def setUp(self) -> None:
		Worker.objects.create(name="Test Doe", birthdate='2021-02-02')

	def test_worker_getting(self):
		worker = Worker.objects.get(name="Test Doe")
		self.assertIsNotNone(worker)
		sample = f"[ 2021-02-02 ] Test Doe"
		self.assertEqual(str(worker), sample)

	def test_shifts_creation_for_worker(self):
		worker = Worker.objects.get(name="Test Doe")

		range_iter = range(1, 5)

		for i in range_iter:
			worker.shifts.create(target_dt=f'2021-12-0{i} 00:00', memo=f'TEST{i}')

		self.assertEqual(len(range_iter), worker.shifts.count())
