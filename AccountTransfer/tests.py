from django.test import TestCase
from django.urls import reverse
from .models import Account, Transaction
from io import StringIO, BytesIO
import csv
from decimal import Decimal
import uuid

# Create your tests here.
class HomePageViewTest(TestCase):
    def test_homepage_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')


class AccountsListViewTest(TestCase):
    def setUp(self):
        # Create test accounts
        Account.objects.create(id=uuid.uuid4(), name="Alice", balance=1000)
        Account.objects.create(id=uuid.uuid4(), name="Bob", balance=500)

    def test_accounts_list_view(self):
        response = self.client.get(reverse('accounts'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts.html')
        self.assertContains(response, "Alice")
        self.assertContains(response, "Bob")

        
class UploadDataViewTest(TestCase):
    def test_upload_valid_csv(self):
        # Prepare a mock CSV file
        valid_csv = BytesIO(b"id,name,balance\n1,Alice,1000\n2,Bob,500")
        valid_csv.name = "valid.csv"
        response = self.client.post(reverse("upload data"), {"file": valid_csv}, format="multipart")
        self.assertContains(response, "File uploaded successfully.")

    
class TransferViewTest(TestCase):
    def setUp(self):
        self.source_account = Account.objects.create(id=uuid.uuid4(), name="Alice", balance=1000)
        self.destination_account = Account.objects.create(id=uuid.uuid4(), name="Bob", balance=500)

    def test_valid_transfer(self):
        response = self.client.post(reverse('transfer'), data={
            'source_account': self.source_account.id,
            'destination_account': self.destination_account.id,
            'amount': 200
        })
        self.assertRedirects(response, reverse('transfer'))

        # Verify balances
        self.source_account.refresh_from_db()
        self.destination_account.refresh_from_db()
        self.assertEqual(self.source_account.balance, 800)
        self.assertEqual(self.destination_account.balance, 700)

    def test_invalid_transfer_insufficient_funds(self):
        response = self.client.post(reverse('transfer'), data={
            'source_account': self.source_account.id,
            'destination_account': self.destination_account.id,
            'amount': 1500
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Insufficient funds in the source account")
        self.source_account.refresh_from_db()
        self.destination_account.refresh_from_db()
        self.assertEqual(self.source_account.balance, 1000)
        self.assertEqual(self.destination_account.balance, 500)

    def test_invalid_transfer_same_account(self):
        response = self.client.post(reverse('transfer'), data={
            'source_account': self.source_account.id,
            'destination_account': self.source_account.id,
            'amount': 200
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Source and destination accounts cannot be the same")

class TransactionModelTest(TestCase):
    def setUp(self):
        self.source_account = Account.objects.create(id=uuid.uuid4(), name="Alice", balance=1000)
        self.destination_account = Account.objects.create(id=uuid.uuid4(), name="Bob", balance=500)

    def test_transaction_creation(self):
        Transaction.objects.create(
            source_account=self.source_account,
            destination_account=self.destination_account,
            amount=200
        )
        self.assertEqual(Transaction.objects.count(), 1)
        transaction = Transaction.objects.first()
        self.assertEqual(transaction.amount, 200)
        self.assertEqual(transaction.source_account, self.source_account)
        self.assertEqual(transaction.destination_account, self.destination_account)
