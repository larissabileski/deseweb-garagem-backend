from django.db import models

from uploader.models import Image
from garagem.models import Marca, Categoria, Cor, Acessorio 


class Veiculo(models.Model):
    modelo = models.CharField(max_length=255, default="")
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT, related_name="veiculo")
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name="veiculo")
    cor = models.ForeignKey(Cor, on_delete=models.PROTECT, related_name="veiculo")
    ano = models.IntegerField(default=0)
    preco = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    acessorios = models.ManyToManyField(Acessorio, related_name="acessorios")
    capa = models.ForeignKey(
        Image,
        related_name="+",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default=None,
    )

    def __str__(self):
        return f"{self.modelo} (Marca: {self.marca} - Ano: {self.ano} - Cor: {self.cor})"

    class Meta:
        verbose_name = "veículo"