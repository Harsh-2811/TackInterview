from django.db import models

# Create your models here.
class Performance(models.Model):
    cost = models.DecimalField(max_digits=20,decimal_places=3,verbose_name="Cost in $")
    revenue = models.DecimalField(max_digits=20,decimal_places=3,verbose_name="Revenue in $")
    profit = models.DecimalField(max_digits=20,decimal_places=3,verbose_name="Profit in $",blank=True)
    roi = models.DecimalField(max_digits=20,decimal_places=3,verbose_name="ROI in %(Points)",blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Cost {},Revenue {}, Profit {}".format(self.cost,self.revenue,self.profit)

    def save(self, *args, **kwargs):
        profit = self.revenue - self.cost
        self.profit = profit
        self.roi = (float(profit)/float(self.cost))
        super(Performance, self).save(*args, **kwargs)
    
class PerformanceManager(models.Manager):
    def filter_by_min_roi(self, min_roi = 0.5):
        return DailyPerformance.objects.filter(performance__roi__gt = min_roi) 

class DailyPerformance(models.Model):
    performance = models.OneToOneField(Performance,on_delete=models.CASCADE)
    date = models.DateField()
    daily_revenue = models.DecimalField(max_digits=20,decimal_places=3,verbose_name="Daily Revenue in $",blank=True)
    objects = models.Manager()
    dailyperformances = PerformanceManager()
    def __str__(self):
        return "Daily Prformance For Performance Object {} Date {}, Daily Revenue {}".format(self.performance.id,self.date,self.daily_revenue)
    
class HourlyPerformance(models.Model):
    performance = models.OneToOneField(Performance,on_delete=models.CASCADE)
    datetime = models.DateTimeField()


    