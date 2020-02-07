from datetime import datetime
import json

def timer(func):
	def inner(*args, **kwargs): 
		current_time = datetime.now()
		main_data = func(*args, **kwargs)

		end = datetime.now()

		time_delta = {"time delta" : str(end - current_time)}

		list_data = json.loads(main_data)
		list_data.append(time_delta)
		result = json.dumps(list_data)

		return (result)

	return inner