from import_export import resources
from .models import BankDetail

class BankDetailResource(resources.ModelResource):
    class Meta:
        model = BankDetail