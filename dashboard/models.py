from django.db import models
from django.contrib.auth.models import User


CATEGORIA = (
    ('vestido', 'vestido'),
    ('camisa', 'camisa'),
    ('saia', 'saia'),

)


class Peca(models.Model):
    nome = models.CharField(max_length=100, null=True)
    categoria = models.CharField(max_length=20, choices=CATEGORIA, null=True)
    quantidade = models.PositiveIntegerField(null=True)

    class Meta:
        verbose_name_plural = 'Peça'

    def __str__(self):
        return f'{self.nome}-{self.quantidade}'


class Venda(models.Model):
    peca = models.ForeignKey(Peca, on_delete=models.CASCADE, null=True)
    staff = models.ForeignKey(User, models.CASCADE, null=True)
    venda_quantidade = models.PositiveIntegerField(null=True)
    data = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Venda'

    def __str__(self):
        return f'{self.peca} vendido por {self.staff.username}'