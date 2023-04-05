from django.db import models


class Work(models.Model):
    work_name = models.CharField(max_length=50, verbose_name='Название работы')

    object = models.Manager


class Contractor(models.Model):
    сontractor_name = models.CharField(max_length=50, verbose_name='Название подрядчика')
    last_name = models.CharField(max_length=50, verbose_name='Описание')
    product = models.CharField(max_length=50, verbose_name='Работа')

    object = models.Manager


class Customer(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя покупателя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    phone = models.CharField(max_length=50, verbose_name='Номер телефона')

    object = models.Manager
