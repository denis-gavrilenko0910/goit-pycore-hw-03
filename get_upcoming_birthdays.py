from datetime import datetime, timedelta

users = [
    {"name" : "John Doe", "birthday" : "1985.03.27"},
    {"name" : "John Doe", "birthday" : "1985.03.29"},
    {"name" : "John Doe", "birthday" : "1985.03.30"},
    {"name" : "Jane Smith", "birthday" : "1990.01.27"},
    {"name" : "Jane Smith", "birthday" : "1990.04.02"},
    {"name" : "Jane Smith", "birthday" : "1990.04.01"},
    {"name" : "Jane Smith", "birthday" : "1990.05.27"},
    {"name" : "Jane Smith", "birthday" : "1990.05.15"},
    {"name" : "Jane Smith", "birthday" : "1990.10.27"}
]

def get_upcoming_birthdays(users: list[dict]):
  result = []
  date_now = datetime.today().date()
  for user in users:
    user_brthday = datetime.strptime(user.get('birthday'), "%Y.%m.%d").date()
    user_brthday = user_brthday.replace(year=date_now.year)
    if user_brthday < date_now:
      user_brthday = user_brthday.replace(year=date_now.year + 1)

    if user_brthday >= date_now and user_brthday < date_now + timedelta(days=7):
      if user_brthday.weekday() == 5:
        user_brthday = user_brthday + timedelta(days=2)
      if user_brthday.weekday() == 6:
        user_brthday = user_brthday + timedelta(days=1)

      user_brthday = user_brthday.strftime("%Y.%m.%d")
      result.append({'name': user.get('name'), 'congratulation_date ':  user_brthday})
      
  return result  
      
upcoming_birthdays = get_upcoming_birthdays(users)

print("Список приветствий на этой неделе:", upcoming_birthdays)