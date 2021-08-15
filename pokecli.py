import requests
import sys
import json # For formatting the output
from timeit import default_timer as timer

def calculateAvg(limit , offset, printToCli):
	start = timer()

	response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=" + str(limit) + "&offset=" + str(offset))

	json_response = response.json()
	pokes = json_response['results'];
	pokesCount = len(pokes)

	height = 0;
	weight = 0;

	for poke in pokes:

		pokeDetail = requests.get("https://pokeapi.co/api/v2/pokemon/" + poke['name'])
		pokeDetail = pokeDetail.json()
		height = height + pokeDetail['height']
		weight = weight + pokeDetail['weight']


	avgHeight = height/pokesCount
	avgWeight = weight/pokesCount
	end = timer()
	output = 'Average Height: ' + str(round(avgHeight)) + "\n" + 'Average Height: ' + str(round(avgHeight)) + "\n" + 'Total time in seconds: ' + str(end - start)

	if printToCli:
		print(output)
	else:
		return output

if sys.argv[0] is not None and sys.argv[0] == 'pokecli.py':
	calculateAvg(sys.argv[1], sys.argv[2], True)