from flask import Flask, escape, request
import requests
import json

from decorator import timer
app = Flask(__name__)


@app.route('/char_details/', methods=['GET'])
@timer
def get_charachter_details():
	data = []


	url = "https://swapi.co/api/people/?search=%s" %escape(request.json["name"])
	response = requests.get(url)

	stars = json.loads(response.text)["results"]
	if stars:
		for result in stars:
			data_dict = {}

			data_dict["full name"] = result["name"]
			data_dict["gender"] = result["gender"]
		
			data_dict["species name"] = json.loads(requests.get(result["species"][0]).text)["name"]
			data_dict["lifespan"] = result["birth_year"]


			data_dict["home planet name"] = json.loads(requests.get(result["homeworld"]).text)["name"]
			movies = []

			for film in result["films"]:
				movies.append(json.loads(requests.get(film).text)["title"])

			data_dict["list of movies"] = movies


			data.append(data_dict) 

	else:
		data.append({"status code": 404, 
					"status": "No characters found"})

	return (json.dumps(data))