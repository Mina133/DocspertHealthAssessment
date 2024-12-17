from django import forms
from .models import Account

class UploadData(forms.Form):
    file = forms.FileField()
    class Meta:
        model = Account
        fields = ['id', 'name', 'balance']


class TransferForm(forms.Form):
    source_account = forms.ModelChoiceField(queryset=Account.objects.all(), label="From Account")
    destination_account = forms.ModelChoiceField(queryset=Account.objects.all(), label="To Account")
    amount = forms.DecimalField(max_digits=10, decimal_places=2, label="Amount")

    def clean(self):
        cleaned_data = super().clean()
        source = cleaned_data.get("source_account")
        destination = cleaned_data.get("destination_account")
        amount = cleaned_data.get("amount")

        if source == destination:
            raise forms.ValidationError("Source and destination accounts cannot be the same.")
        
        if amount and source and source.balance < amount:
            raise forms.ValidationError("Insufficient funds in the source account.")
        
        return cleaned_data
