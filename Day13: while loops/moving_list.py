# Available toppings
request = ['mushroom', 'pineapple', 'onion']
completed = []

print(request, completed, sep='\n')

while request:
    data = request.pop()
    # call the function for current task
    print(f'fetching {data}...')

    completed.append(data)
    
print(request, completed, sep='\n')
