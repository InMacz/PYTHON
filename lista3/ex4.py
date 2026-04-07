popA = 80000
popB = 200000
anos = 0
while popA < popB:
    popA += (popA*3)/100
    popB += (popB*1.5)/100
    anos += 1
print(f"Irá demorar {anos} anos para popA passar popB")
print(f"População A: {popA:.2f}")
print(f"População B: {popB:.2f}")