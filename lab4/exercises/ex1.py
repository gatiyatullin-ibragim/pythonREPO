from datetime import datetime, timedelta

today = datetime.today()

future_date = today + timedelta(days=5)

print("Текущая дата:", today.strftime("%Y-%m-%d"))
print("Дата через 5 дней:", future_date.strftime("%Y-%m-%d"))
