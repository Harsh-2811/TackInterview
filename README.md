-- REQUIREMENTS
1. Python 3.10
2. Redis Server should be Running
3. Use Ubuntu or WSL to Run Project (Required to Check CELERY Logs)

-- Project Setup
1. install requirements using pip install -r requirements.txt
2. Run Python Server : python3 manage.py runserver
3. Run Celery Terminal (Seperate): python3 -m celery -A assignment worker -B -l info

-- Test Project
For First Task : 
In this script filter the queryset using filter_by_min_roi previously created and save in a variable all the daily performance where the roi > 50%. Print the length of the queryset. Print the length of the queryset multiplied by 2. Expected query set length ~= 50.000 records. In a loop show the index of the loop out of the length of the queryset: 1/50000, 2/50000, 3/50000 and so on. In the same loop assign a new value to the revenue = revenue multiplied by a random factor which goes between 0.5 and 2 and save the daily_revenue with the new values
Execute this URL in Browser: http://127.0.0.1:8000/api/performance/random_revenue/

For Second Task :
Create another script called slow_iteration.py. In this script get a DailyPerformance queryset limiting it to 50 records. Iter over this queryset, and add a time.sleep(60) inside the loop. Implement this with celery task.
Execute this URL in Browser: http://127.0.0.1:8000/api/performance/slow_iteration/


-- Information
I have created slowiterationCelery.py file inside performance app to implement all celery tasks and functions.