from django.db import models


class Consumer(models.Model):
    cpf = models.CharField(max_length=11)
    age = models.IntegerField()
    address = models.CharField(max_length=100)
    economic_income = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.cpf


class Asset(models.Model):
    consumer = models.ForeignKey(Consumer, related_name='assets', on_delete=models.CASCADE)
    description = models.CharField(max_length=100)
    value = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        unique_together = ('consumer', 'description')
        ordering = ['description']

    def __str__(self):
        return '%s: %d ' % (self.description, self.value)
