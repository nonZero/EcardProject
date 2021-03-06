from django.db import models


class Image(models.Model):
    image_file = models.ImageField(upload_to='cards/images/',
                                   width_field='width', height_field='height')
    width = models.IntegerField()
    height = models.IntegerField()

    rosetta_id = models.CharField(max_length=200, null=True, blank=True)


class Sheet(models.Model):
    title = models.CharField(max_length=200)
    subjects = models.TextField(default='')
    thumbnail_id = models.CharField(max_length=32)
    link_id = models.CharField(max_length=32)
    recordid = models.CharField(max_length=100)
    rights = models.CharField(max_length=200, blank=True)
    regions = models.TextField(default='')

    def __str__(self):
        return self.title + " " + self.recordid

    def image_url(self):
        return 'http://rosetta.nli.org.il/delivery/DeliveryManagerServlet?dps_func=stream&dps_pid={}'.format(
            self.link_id)

    def image_file(self):
        return self.link_id + ".jpg"

    def thumbnail_url(self):
        return 'http://rosetta.nli.org.il/delivery/DeliveryManagerServlet?dps_func=thumbnail&dps_pid={}'.format(
            self.thumbnail_id)


class EcardText(models.Model):
    text = models.TextField(default='')
    sheet = models.ForeignKey(Sheet)
