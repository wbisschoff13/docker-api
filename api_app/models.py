from django.db import models
import numpy as np
# Create your models here.


class Pokemon(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    type1 = models.CharField(max_length=20)
    type2 = models.CharField(max_length=20, blank=True, null=True)
    evolves_from = models.CharField(max_length=50, blank=True, null=True)
    hp = models.IntegerField(blank=True, null=True)
    attack = models.IntegerField(blank=True, null=True)
    defense = models.IntegerField(blank=True, null=True)
    sp_attack = models.IntegerField(blank=True, null=True)
    sp_defense = models.IntegerField(blank=True, null=True)
    speed = models.IntegerField(blank=True, null=True)

    @property
    def average_stat(self):
        try:
            avg = int(np.mean([self.hp, self.attack, self.defense,
                               self.sp_attack, self.sp_defense, self.speed]))
        except:
            avg = 0
        return avg

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']
