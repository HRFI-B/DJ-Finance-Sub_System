from datetime import *
current_date = date.today()
datem = datetime.strptime(str(current_date), "%Y-%m-%d")
print(datem.month)