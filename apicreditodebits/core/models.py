from django.db import models


class Person(models.Model):
    cpf = models.CharField(max_length=11)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.cpf


class Debt(models.Model):
    person = models.ForeignKey(Person, related_name='debits', on_delete=models.CASCADE)
    company = models.CharField(max_length=100)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('person', 'company')
        ordering = ['company']

    def __str__(self):
        return '%s: %d ' % (self.company, self.value)
