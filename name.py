name = input('please type in your name :'  )
if len(name) < 3:
    print('name must be at least 3 characters long')
elif  len(name) > 50:
    print('name can be a maximuim of 50 characters')
else:
    print(f'your name {name} is in order')        