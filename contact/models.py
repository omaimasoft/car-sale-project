# models.py
from django.db import models

class Contact(models.Model):
    nom_complet = models.CharField(max_length=150)
    telephone = models.CharField(max_length=20)
    message = models.TextField()
    date_envoi = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom_complet
