from datetime import datetime

today = datetime.now()
print(f"{today.strftime('%B')} {today.strftime('%d')}, {today.strftime('%Y')}")
