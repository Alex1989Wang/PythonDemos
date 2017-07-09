
numbers = [1, 3, 5]
postition = 0
while postition < len(numbers):
    number = numbers[postition]
    if number % 2 == 0:
        print('Found even number', number)
        break
    postition += 1
else:
    print('no even number was found.')

# iteration 
rabitts = ['Flopsy', 'Mopsy', 'Cottontail', 'Peter']
current = 0
while current < len(rabitts):
    print(rabitts[current])
    current += 1

for rabbit in rabitts:
    print(rabbit)
