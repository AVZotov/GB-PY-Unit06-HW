def get_int():
	while True:
		user_input = input('Enter value: ')
		try:
			int(user_input)
			return int(user_input)
		except ValueError:
			print('error, please try again')
		
		
print("enter progression start")
progression_start = get_int()
print("enter progression step")
progression_step = get_int()
print("enter progression length")
progression_length = get_int()
progression = []

for i in range(1, progression_length + 1):
	progression.append(progression_start + (i - 1) * progression_step)
print(progression)