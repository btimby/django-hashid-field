from django.db import models

from hashid_field import HashidAutoField, HashidField


class Author(models.Model):
    id = HashidAutoField(primary_key=True)
    name = models.CharField(max_length=40)
    uid = models.UUIDField(null=True, blank=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=40)
    author = models.ForeignKey(Author, null=True, blank=True)
    reference_id = HashidField(salt="alternative salt")
    key = HashidField(min_length=10, alphabet="abcdlmnotuvwxyz0123789", null=True, blank=True)
    some_number = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return "{} ({})".format(self.name, self.reference_id)
