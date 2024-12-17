from django.urls import path
from .views import UploadDataView, HomePage, UploadSuccess, AccountsView, TransferView

urlpatterns = [
    path('upload/',UploadDataView.as_view(), name='upload data'),   
    path ('', HomePage, name='home'),
    path('success/', UploadSuccess, name='UploadSuccess'),
    path('accounts/', AccountsView.as_view(), name='accounts'),
    path('transfer/', TransferView.as_view(), name='transfer')
]