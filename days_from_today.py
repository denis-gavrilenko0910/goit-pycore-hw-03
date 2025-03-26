from datetime import datetime as dtdt
def get_days_from_today(date):
  now = dtdt.today()

  parsed_date = dtdt.strptime(date, '%Y-%m-%d')

  result = parsed_date - now

  return result.days

print(get_days_from_today('2025-03-10'))
res = get_days_from_today('2025-03-10')
print(res)