from django.db import models

#this is error where i create tow table at the firest
class TrackList(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=150)


    # def get_absolute_url(self):
    #     return '/my-lists/{}/'.format(self.pk)

    def __str__(self):
        return '{} - {}'.format(self.user.get_full_name(), self.title)


class TodoItem(models.Model):
    track_list = models.ForeignKey(TrackList, on_delete=models.CASCADE)
    time = models.IntegerField()
    distance = models.IntegerField()
    date = models.DateTimeField(null=True, blank=True)

###################################################
    #
    # def __str__(self):
    #     return self.title

# the right table
class Track(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    time = models.IntegerField()
    distance = models.IntegerField()
    date = models.DateField(null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.user.get_full_name() )