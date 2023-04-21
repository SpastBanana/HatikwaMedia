from django.db import models

class member_invites(models.Model):
    email = models.CharField(max_length=200)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name_plural = "Outgoing invites"