Random=input("skriv något random ")

for i in range(0, 10):
    print(str(1+ i ) , Random )

y=int(input("Hur högt ska jag räkna? "))
for x in range(0,y):
    print(str(1+x))



for table in range(1,11):
    for y in range(1,13):
        print (f"Tabell {table}) {table} * {y} = {table * y} ")
