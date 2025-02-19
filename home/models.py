# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Bill(models.Model):

    #__Bill_FIELDS__
    id_bill = models.CharField(max_length=255, null=True, blank=True)
    tgl_in = models.DateTimeField(blank=True, null=True, default=timezone.now)
    path_img = models.TextField(max_length=255, null=True, blank=True)
    tgl_out = models.DateTimeField(blank=True, null=True, default=timezone.now)
    pathout_img = models.TextField(max_length=255, null=True, blank=True)
    total = models.IntegerField(null=True, blank=True)
    pos_in = models.CharField(max_length=255, null=True, blank=True)
    pos_out = models.CharField(max_length=255, null=True, blank=True)
    nm_op = models.CharField(max_length=255, null=True, blank=True)
    jns_knd = models.CharField(max_length=255, null=True, blank=True)
    st = models.IntegerField(null=True, blank=True)
    st_mbr = models.IntegerField(null=True, blank=True)
    no_pol = models.CharField(max_length=255, null=True, blank=True)
    lm_pk = models.CharField(max_length=255, null=True, blank=True)
    nm_sf = models.CharField(max_length=255, null=True, blank=True)
    total_biaya = models.IntegerField(null=True, blank=True)
    jml_org = models.IntegerField(null=True, blank=True)

    #__Bill_FIELDS__END

    class Meta:
        verbose_name        = _("Bill")
        verbose_name_plural = _("Bill")


class Lap(models.Model):

    #__Lap_FIELDS__
    path_img = models.DateTimeField(blank=True, null=True, default=timezone.now)
    tgl_out = models.DateTimeField(blank=True, null=True, default=timezone.now)
    pathout_img = models.TextField(max_length=255, null=True, blank=True)
    total = models.IntegerField(null=True, blank=True)
    pos_in = models.CharField(max_length=255, null=True, blank=True)
    post_out = models.CharField(max_length=255, null=True, blank=True)
    nm_op = models.CharField(max_length=255, null=True, blank=True)
    jns_knd = models.CharField(max_length=255, null=True, blank=True)
    no_pol = models.CharField(max_length=255, null=True, blank=True)
    lm_pk = models.CharField(max_length=255, null=True, blank=True)
    nm_sf = models.CharField(max_length=255, null=True, blank=True)
    total_biaya = models.IntegerField(null=True, blank=True)
    jml_org = models.IntegerField(null=True, blank=True)

    #__Lap_FIELDS__END

    class Meta:
        verbose_name        = _("Lap")
        verbose_name_plural = _("Lap")



#__MODELS__END
