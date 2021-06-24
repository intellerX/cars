from django.db import models
from simple_history.models import HistoricalRecords


class CarManager():
    def _create_car(self,  model, color, date):
        car = self.model(
            model=model,
            color=color,
            date=date,
    
        )
        car.save(using=self.db)
        return car

    def create_car(self,  model, color, date):
        return self._create_car( model, color, date)


class Car(models.Model):
    id = models.AutoField(primary_key=True)
    model = models.CharField('Modelo', max_length=255)
    color = models.CharField('Color', max_length=255)
    date =  models.DateField("Fecha de nacimiento",blank=True, null=True)
    historical = HistoricalRecords()
    objects = CarManager()

    class Meta:
        verbose_name = 'Car'
        verbose_name_plural = 'Cars'

    REQUIRED_FIELDS = ['model', 'color']

    def __str__(self):
        return f'{self.model} {self.color}'
