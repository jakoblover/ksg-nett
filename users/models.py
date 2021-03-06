# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import AbstractUser
from django.db import models

# KSG choices
from commissions.models import Commission

KSG_STATUS_TYPES = (
    ("aktiv", "Aktiv"),  # Wants to stay in KSG
    ("inaktiv", "Ikke aktiv"),  # Finished with KSG duties, but want to leave
    ("permittert", "Permittert"),  # Implicitly inactive, wants to continue
    ("sluttet", "Sluttet før tiden"),  # Implicitly inactive, has jumped ship
)

# Roles in the KSG hierarchy
KSG_ROLES = (
    ("gjengis", "Gjengis"),
    ("funk", "Funksjonær"),
    ("hangaround", "Hangaround"),
    ("gjengpang", "GjengPang"),
    ("funkepang", "FunkePang"),
    ("hospitant", "Hospitant"),
)


class User(AbstractUser):
    """
    A KSG user
    """
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField(blank=True, null=True)
    study = models.CharField(default="", blank=True, max_length=100)
    profile_image = models.FileField(upload_to='profiles/', null=True)

    phone = models.CharField(default="", blank=True, max_length=50)
    study_address = models.CharField(default="", blank=True, max_length=100)
    home_address = models.CharField(default="", blank=True, max_length=100)

    start_ksg = models.DateField(auto_now_add=True)
    ksg_status = models.CharField(max_length=32, choices=KSG_STATUS_TYPES, default=KSG_STATUS_TYPES[0])
    ksg_role = models.CharField(max_length=32, choices=KSG_ROLES, default=KSG_ROLES[0])

    commission = models.ForeignKey(
        Commission,
        default=None,
        blank=True,
        null=True,
        related_name='holders'
    )

    def __str__(self):
        return "User %s" % (self.first_name,)

    def __repr__(self):
        return "User(name=%s)" % (self.first_name,)

    def current_commission(self):
        if self.commission:
            return "%s" % (self.commission.name,)
        else:
            return None

    def active(self):
        return self.ksg_status == KSG_STATUS_TYPES[0][0]

    active.boolean = True

    class Meta:
        default_related_name = 'users'
        verbose_name_plural = 'Users'
