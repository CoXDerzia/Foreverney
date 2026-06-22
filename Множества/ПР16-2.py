base_id = [10, 20, 30]
incoming_id = [20, 40, 10, 50]
print("Разрешенные ID: ", base_id)
print("Входящие ID: ", incoming_id)

allowed_id = set(base_id)

for id in set(incoming_id):
    if id in allowed_id:
        print("OK")
        print(id)
    else:
        allowed_id.add(id)
        print("ADDED")
        print(id)

print(allowed_id)