from django.db import models

# Create your models here.

class Stock(models.Model):
    def __unicode__(self):
        return u'%s \"%s\" (%.2f, %.2f)' % (self.symbol, self.company, self.latitude, self.longitude)
    
    symbol = models.CharField(max_length = 50, null=False)
    company = models.CharField(max_length = 200, null=False)
    latitude = models.FloatField()
    longitude = models.FloatField()

class Quote(models.Model):
    def __unicode__(self):
        return u'%.2f %s %.2f' % (self.price, (u'\u25b2' if self.change>= 0 else u'\u25bc'), abs(self.change))

    def __str__(self):
        return '%.2f %s %.2f' % (self.price, ('/\\' if self.change>= 0 else '\\/'), abs(self.change))
    
    stock = models.ForeignKey(Stock, null=False, unique=True)
    price = models.FloatField()
    change = models.FloatField()
    last_modified = models.DateTimeField(null=False, auto_now=True, auto_now_add=True)