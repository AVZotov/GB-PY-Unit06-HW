import random


def get_int():
	while True:
		user_input = input('Enter value: ')
		try:
			int(user_input)
			return int(user_input)
		except ValueError:
			print('error, please try again')


list_1 = [random.randint(1, 20) for i in range(20)]
print("enter min range")
min_range = get_int()
print("enter max range")
max_range = get_int()
result = []

for i in range(0, len(list_1)):
	if min_range <= list_1[i] <= max_range:
		result.append(i)
print(list_1)
print(result)
