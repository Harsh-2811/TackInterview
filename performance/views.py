from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
import time
from .models import DailyPerformance
import random
def randomFactor():
    import decimal
    return round(decimal.Decimal(random.uniform(1.5, 2)),1)

class randomRevenue(APIView):
    def get(self,request):
        performances = DailyPerformance.dailyperformances.filter_by_min_roi(0.5)

        print("Length of Queryset : ")
        print(performances.count())

        print("Length of Queryset Multiplied by 2 : ")
        print(performances.count()*2)
        
        for i in range(performances.count()):
            print("Index {}/{}".format(i+1,performances.count()))
            randomDecimal = randomFactor()
            performance= DailyPerformance.objects.filter(pk = performances[i].pk).first()
            performance.daily_revenue = performance.performance.revenue * randomDecimal
            performance.save()
        return Response("Please check CMD to Check Output and Checkout DailyPerformance Data")

class slowIteration(APIView):
    def get(self,request):
        from .slowIterationCelery import perfromSlowIteration
        perfromSlowIteration.delay()
        return Response("Your CELERY Task has been scheduled.. Check CELERY CMD to Check a logs")

class genertaeRandomData(APIView):
    def get(self,request):
        from .slowIterationCelery import insertRandomData
        insertRandomData.delay()
        return Response("Process to Insert data has been started")