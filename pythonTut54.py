class student:
    pass

harry=student()
rohan=student()
larry=student()
print(harry,rohan,larry)

harry.name="Harry"
harry.std=12
harry.secction=1

rohan.name="Rohan"
rohan.std=12
rohan.secction=1

larry.subject=["Hindi", "Physics"]

print(harry.name, rohan.name)
print(harry.std, rohan.std)
print(larry.subject)