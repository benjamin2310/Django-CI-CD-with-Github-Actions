from django.test import TestCase
from .models import TravelPackage

class TravelPackageTest(TestCase):
    def test_package_creation(self):
        # Create a TravelPackage instance
        package = TravelPackage.objects.create(
            name="Adventure Tour",
            destination="Hawaii",
            price=1500.00,
            description="An exciting adventure tour in Hawaii.",
            available=True
        )
        # Assertions to check if the package was created correctly
        self.assertEqual(package.name, "Adventure Tour")
        self.assertEqual(package.destination, "Hawaii")
        self.assertEqual(package.price, 1500.00)
        self.assertTrue(package.available)
