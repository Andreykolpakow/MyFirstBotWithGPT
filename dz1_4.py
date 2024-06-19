def format_seconds(seconds):
  days, seconds = divmod(seconds, 86400)
  hours, seconds = divmod(seconds, 3600)
  minutes, seconds = divmod(seconds, 60)

  return f'{days}:{hours}:{minutes}:{seconds}'

total_seconds = 1000000  # Пример количества секунд
formatted_time = format_seconds(total_seconds)
print(formatted_time)