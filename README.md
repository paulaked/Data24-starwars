# Data 24 Star Wars Project

## Links

Trello board: 
https://trello.com/invite/b/wu28Ecub/5f4b291ad0d1f8352adc1a201a543e32/data24-starwars-ahmedreman

My Git Branch:
https://github.com/paulaked/Data24-starwars/tree/AhmedReman

Design Documents:
The design documents can be found in the following directory:
/docs/design

## Basic Coding Requirements

- Pull data on all available starships
- Using the "pilots" field, join every starship with the character who pilots it (set the value of the pilots field to the characters id)



## Instructions

The character data in your MongoDB database has been pulled from https://swapi.dev/.
As well as 'people', the API has data on starships.
Using Python, write code to pull data on all available starships from the API.
The "pilots" key contains URLs pointing to the characters who pilot the starship.
Use these to replace 'pilots' with a list of ObjectIDs from our characters collection, then insert the starships into their own collection in MongoDB.
(Make sure you drop any existing starships collections.)

You have until 9am on Tuesday.

## Requirements

- Use good coding principles.  That means testing, appropriate comments, good naming conventions and handling errors gracefully.
- Follow PEP 8
- Create a job board in Trello or similar to keep track of your user stories.  Provide a link to that job board in your version of this README.
- Your code should utilise functional programming OR object-oriented programming
- Use Test Driven Development: write your tests first

## Using this repo

- Branch off from main.
- Use your own name for the name of the branch (e.g. mine would be PaulaKedra - please copy this format).
- Make sure you commit and push to the remote repo frequently to keep your work up-to-date.
- The gitignore should catch most unnecessary project files, but do pay attention to what you are adding to the repo.
- Replace this README with an appropriate README for your project (including a link to your job board).
