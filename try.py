import sql_data as sd
return_data = sd.find_all()

row = 0

for person in return_data:
    print(len(person))

