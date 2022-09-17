from celery import shared_task
from .models import DailyPerformance, Performance
import time
import logging
import sys

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("debug.log"),
        logging.StreamHandler(sys.stdout)
    ]
)

@shared_task()
def perfromSlowIteration():
    dailyperformances = DailyPerformance.objects.all()[:50]
    for performance in dailyperformances:
        logging.info(performance)
        with open('output.txt','w') as f:
            f.write(str(performance.id))
            f.write("\n")
            f.close()
        time.sleep(60)

@shared_task()
def insertRandomData():
    import random
    from datetime import datetime
    for i in range(5000):
        randomRevenueInt = random.randint(5000,10000)
        randomCostInt = random.randint(5000,10000) 

        performance = Performance.objects.create(
            cost = randomCostInt,
            revenue = randomRevenueInt
        )
        DailyPerformance.objects.create(
            date = datetime.today().date(),
            performance = performance,
            daily_revenue = 0
        )
        print("INSERTED")
        time.sleep(2)