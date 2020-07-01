d=dict()
status=''
while status!='Done':
	key=input('Enter product: ')
	value=eval(input('Enter the price: '))
	d[key]=value
	status=input('Enter Done to complete.')

status=''
while status!='Done':
	product=input('Enter product to crosscheck: ')
	if product in d:
		print(d[product])
	else:
		print('Product not in the list.')
	status=input('Enter Done to stop.')