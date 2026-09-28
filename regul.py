import re
# Читаем лог из файла
with open('log.txt', 'r', encoding='utf-8') as file:
    log = file.read()
print("1) Строки с уровнем ERROR или WARN")
# Используем re.finditer
for match in re.finditer(r'^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (ERROR|WARN) (.+)$', log, re.MULTILINE):
    time, level, message = match.groups()
    print(f"{time} {level} {message}")
print()
print("2) Строки, в которых упоминаются IP-адреса")
# Используем re.findall для получения всех строк
lines = re.findall(r'^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (\w+) (.+)$', log, re.MULTILINE)
# Паттерн IP-адреса
ip_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
for time, level, message in lines:
    if re.search(ip_pattern, message):
        print(f"{time} {level} {message}")
