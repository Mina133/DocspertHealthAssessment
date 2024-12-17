from django.shortcuts import render, redirect
import csv
from .models import Account, Transaction
from .forms import UploadData, TransferForm
from django.views.generic import FormView, ListView
from django.urls import reverse_lazy
from django.db import transaction
from django.contrib import messages

# Create your views here.

class UploadDataView(FormView):
    template_name = 'upload.html'
    def post(self, request, *args, **kwargs):
        file = request.FILES.get("file")
        if not file or not file.name.endswith(".csv"):
            messages.error(request, "Please upload a valid CSV file.")
            return render(request, self.template_name)

        # Simulate processing the file (replace with actual processing logic)
        try:
            decoded_file = file.read().decode("utf-8").splitlines()
            reader = csv.reader(decoded_file)
            # Iterate over rows or perform database operations here
        except Exception as e:
            messages.error(request, "An error occurred while processing the file.")
            return render(request, self.template_name)

        # Add success message
        messages.success(request, "File uploaded successfully.")
        return render(request, self.template_name)

def HomePage(request):
    return render(request, 'home.html')

def UploadSuccess(request):
    return render(request, 'success.html')

class AccountsView(ListView):
    model = Account
    template_name = 'accounts.html'
    context_object_name = 'accounts'

    def get_queryset(self):
        return Account.objects.all()
    

class TransferView(FormView):
    template_name = 'transfer.html'
    form_class = TransferForm
    success_url = reverse_lazy('transfer')

    def form_valid(self, form):
        source = form.cleaned_data['source_account']
        destination = form.cleaned_data['destination_account']
        amount = form.cleaned_data['amount']

        try:
            with transaction.atomic():
                source.balance -= amount
                source.save()

                destination.balance += amount
                destination.save()

                # Record the transaction
                Transaction.objects.create(
                    source_account=source,
                    destination_account=destination,
                    amount=amount
                )

                messages.success(self.request, 'Transfer successful.')

        except Exception as e:
                    messages.error(self.request, f'An error occurred: {e}')
                    return self.form_invalid(form)
        
        return super().form_valid(form)
            

