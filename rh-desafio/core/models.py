import uuid

from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Company(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    logo = models.ImageField(verbose_name='Logo', upload_to='imagens')
    name = models.CharField(verbose_name='Name(Nome)', max_length=100)
    legal_number = models.CharField(verbose_name='Legal Number(CNPJ)', max_length=100)
    # This is auto created and updated date
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    create_user = models.UUIDField(editable=False, null=True)
    update_user = models.UUIDField(editable=False, null=True)

    class Meta:
        db_table = 'Company'

    def __str__(self):
        return self.name


class Department(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    admin = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='User')
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Name', max_length=100)
    status = models.BooleanField(verbose_name='Ativo', default=False)
    # This is auto created and updated date
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    create_user = models.UUIDField(editable=False, null=True)
    update_user = models.UUIDField(editable=False, null=True)

    class Meta:
        db_table = 'Department'

    def __str__(self):
        return self.name


class Employee(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Others')

    )
    gender = models.CharField(max_length=1, choices=GENDER)
    # department = models.ForeignKey(Department, on_delete=models.PROTECT)
    # company = models.ForeignKey(Company, on_delete=models.PROTECT)
    phone = models.CharField(max_length=14, default='Sem Telefone')
    role = models.CharField(max_length=50, default='Sem Atribuição')
    age = models.IntegerField(default=0)
    joining_date = models.DateField(null=True)
    salary = models.DecimalField(decimal_places=2, max_digits=12, default=0)
    # This is auto created and updated date
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    create_user = models.UUIDField(editable=False, null=True)
    update_user = models.UUIDField(editable=False, null=True)

    class Meta:
        db_table = 'Employee'

    # Simple title return queue for django admin or auto template
    def __str__(self):
        return str(self.name)
