from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class TgUser(models.Model):
    user_id = models.BigIntegerField(verbose_name="User-ID", unique=True)
    username = models.CharField(max_length=150, verbose_name="Username", null=True)

    def __str__(self):
        return "{} - {}".format(self.user_id, self.username)


class BotContext(models.Model):
    start_context = RichTextUploadingField()
    info_context = RichTextUploadingField()


class Liga(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class LigaTable(models.Model):
    liga = models.ForeignKey(Liga, on_delete=models.CASCADE)
    team = models.CharField(max_length=200, unique=True)
    games = models.IntegerField()
    win = models.IntegerField()
    lose = models.IntegerField()
    goals = models.IntegerField()
    score = models.IntegerField()

    def __str__(self):
        return self.team


class LigaPlayer(models.Model):
    liga = models.ForeignKey(Liga, on_delete=models.CASCADE)
    team = models.CharField(max_length=200)
    player = models.CharField(max_length=200)
    games = models.IntegerField()
    goals = models.IntegerField()
    assist = models.IntegerField()

    def __str__(self):
        return self.player


class TopTeam(models.Model):
    team = models.CharField(max_length=200)
    rate = models.IntegerField()

    def __str__(self):
        return self.team


class GameCalendar(models.Model):
    liga = models.ForeignKey(Liga, on_delete=models.CASCADE)
    team = models.CharField(max_length=200)
    score = models.CharField(max_length=50)
    date = models.DateTimeField()

    def __str__(self):
        return self.team



