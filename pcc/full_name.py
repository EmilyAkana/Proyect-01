"""full_name.py"""

first = input("\nInserte su primer nombre ")
last = input("\nInserte su apellido ")

message = f"\nHola, {first} {last}!  "
print(message.title().rstrip())

input("\nQuieres ver algo más? ")
youtube_url = "https://youtu.be/xvFZjo5PgG0?si=kmTC_khNMhnvJplH"

print(f"\nAqui tienes tu premio. {youtube_url}\n")
# full_name = f"{first} {last}"
# print(f"Hello, {full_name.title()}!")
