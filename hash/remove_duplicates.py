string="sawapp"
seen=set()
result=""
for char in string:
  if char not in seen:
    seen.add(char)
    result+=char
print(result)