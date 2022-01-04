from datetime import datetime, timedelta

def get_future_date(days = 0):
    today = datetime.now()
    delta = timedelta(days = days)
    
    return today + delta

def get_month_from_date(date):
    return date.month

def get_year_from_date(date):
    return date.year