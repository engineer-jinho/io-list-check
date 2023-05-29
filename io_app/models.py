from django.db import models

# 공통 필드를 정의한 IOBaseModel
class IOBaseModel(models.Model):
    field_tag = models.CharField(max_length=200)
    plc_tag = models.CharField(max_length=200)
    description = models.TextField()
    hmi_description = models.TextField()
    signal_io_diagram_location = models.CharField(max_length=200)
    panel_diagram_location = models.CharField(max_length=200)
    io_module_location = models.CharField(max_length=200)
    io_module_picture = models.ImageField(upload_to='io_module/')
    io_channel_number = models.IntegerField()
    status = models.CharField(max_length=200)
    diagnosis = models.TextField()
    pid = models.CharField(max_length=200)
    modbus_address = models.IntegerField()

    class Meta:
        abstract = True


# AI 모델
class AIModel(IOBaseModel):
    min = models.FloatField()
    max = models.FloatField()
    unit = models.CharField(max_length=200)
    low_low = models.FloatField()
    low = models.FloatField()
    high = models.FloatField()
    high_high = models.FloatField()
    low_low_error = models.CharField(max_length=200)
    low_error = models.CharField(max_length=200)
    high_error = models.CharField(max_length=200)
    high_high_error = models.CharField(max_length=200)
    sf_error = models.CharField(max_length=200)


# AO 모델
class AOModel(IOBaseModel):
    min = models.FloatField()
    max = models.FloatField()
    unit = models.CharField(max_length=200)
    low_low = models.FloatField()
    low = models.FloatField()
    high = models.FloatField()
    high_high = models.FloatField()
    low_low_error = models.CharField(max_length=200)
    low_error = models.CharField(max_length=200)
    high_error = models.CharField(max_length=200)
    high_high_error = models.CharField(max_length=200)
    sf_error = models.CharField(max_length=200)


# DI 모델
class DIModel(IOBaseModel):
    pulse = models.BooleanField()
    contact_type = models.CharField(max_length=200)
    true_description = models.TextField()
    false_description = models.TextField()
    alarm_msg = models.TextField()
    trip_msg = models.TextField()


# DO 모델
class DOModel(IOBaseModel):
    pulse = models.BooleanField()
    contact_type = models.CharField(max_length=200)
    true_description = models.TextField()
    false_description = models.TextField()
    alarm_msg = models.TextField()
    trip_msg = models.TextField()