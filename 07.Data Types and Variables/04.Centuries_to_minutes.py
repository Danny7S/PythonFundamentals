centuries=int(input())
years=centuries*100
days=int(years*365.242)
hours=days*24
minutes=hours*60
print(f'{centuries} centuries = {years} years = {int(days)} days = {int(hours)} hours = {int(minutes)} minutes')