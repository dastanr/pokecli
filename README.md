## Service: Pokémon Height/Weight Analyzer
Using a language and any libraries, frameworks, etc of your choice, develop a small service that
will determine the average weight and height of a given subset of Pokémon. Use the open
PokéApi (https://pokeapi.co) to pull the data and perform your calculations. There does not
need to be a GUI for this service, a CLI tool is preferred. Upon completion of the project,
push the code to a public GitHub repository and send the GitHub repository link to
kiel.wood@stratusgrid.com.
Requirements & Specifications
The program should:
- Your CLI script should take two arguments: limit and offset
- Query a list of Pokémon from the API using the limit and offset inputs mentioned above
- Query details for each Pokémon to retrieve it’s height and weight
- Calculate an average weight and height for all the Pokémon in the subset queried and
then print the values to the CLI
- Track the time it takes in seconds to execute the entire service and print to CLI following
the averages
- Add at least one unit test case to the project using a unit testing framework of your
choice

*HINT* for this challenge, speed of the program’s execution time is more important than code
quality