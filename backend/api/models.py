from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class TgUser(models.Model):
    user_id = models.BigIntegerField(verbose_name="User-ID", unique=True)
    username = models.CharField(max_length=150, verbose_name="Username", null=True)
    language = models.CharField(max_length=10, default='uz')
    team = models.CharField(max_length=100, null=True)

    def __str__(self):
        return "{} - {}".format(self.user_id, self.username)


class Liga(models.Model):
    stiker = models.CharField(max_length=20, null=True)
    name = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.name


class LigaTable(models.Model):
    liga = models.CharField(max_length=200)
    place = models.IntegerField(null=True)
    team = models.CharField(max_length=200, unique=True)
    games = models.IntegerField()
    win = models.IntegerField()
    lose = models.IntegerField()
    goals = models.IntegerField()
    score = models.IntegerField()

    def __str__(self):
        return self.team

    class Meta:
        ordering = ['place']


class LigaPlayer(models.Model):
    liga = models.CharField(max_length=200)
    team = models.CharField(max_length=200)
    player = models.CharField(max_length=200, unique=True)
    games = models.IntegerField()
    goals = models.IntegerField()
    place = models.IntegerField(null=True)

    def __str__(self):
        return self.player

    class Meta:
        ordering = ['place']


class TopTeam(models.Model):
    place = models.IntegerField(null=True)
    team = models.CharField(max_length=200, unique=True)
    rate = models.IntegerField()

    def __str__(self):
        return self.team

    class Meta:
        ordering = ['place']


class GameCalendar(models.Model):
    liga = models.CharField(max_length=200)
    tour = models.IntegerField(null=True)
    team = models.CharField(max_length=200)
    score = models.CharField(max_length=50)
    date = models.DateTimeField()

    def __str__(self):
        return self.team

    class Meta:
        ordering = ['tour']



