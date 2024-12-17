from django.db import models
import uuid

# Create your models here.
class Account(models.Model):
   id = models.UUIDField(primary_key=True,  default=uuid.uuid4, editable=False)
   name = models.CharField(max_length=100)
   balance = models.IntegerField()
   
   def __str__(self):
        return self.name
   
from django.db import models
from django.utils.timezone import now

class Transaction(models.Model):
    source_account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="outgoing_transfers")
    destination_account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="incoming_transfers")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(default=now)

    def __str__(self):
        return f"{self.source_account} -> {self.destination_account} : {self.amount}"
