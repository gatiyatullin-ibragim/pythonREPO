import re

text = "Contact me at test@example.com or info@site.net"
pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

emails = re.findall(pattern, text)
print(emails)  # ['test@example.com', 'info@site.net']
