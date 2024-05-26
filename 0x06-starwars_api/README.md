# Star Wars API

This Node.js script fetches and displays the names of characters from a specified Star Wars film, displaying each character name on a new line.

## Objectives

- Retrieve a list of character URLs from the Star Wars API (`/films/` endpoint).
- Display the name of each character in the same order as the list.

## Prerequisites
- Nodejs

## Installation
Install Node 10
```bash
$ curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
$ sudo apt-get install -y nodejs
```
Install semi-standard
Documentation
```bash
$ sudo npm install semistandard --global
```
Install request module and use it
Documentation
```bash
$ sudo npm install request --global
$ export NODE_PATH=/usr/lib/node_modules
```

## Usage
Run the script using the following command:

```bash
$ ./0-starwars_characters.js <movieId>
```
Replace <movieId> with the ID of the Star Wars movie you want to fetch characters from. For example, to get characters from movie ID 1:

```bash
Copy code
./0-starwars_characters.js 1
```

Example:
Here is an example of how to run the script and what to expect as output:

```bash

$ ./0-starwars_characters.js 1
```
Output:

```bash
mathematica
Copy code
Luke Skywalker
C-3PO
R2-D2
Darth Vader
Leia Organa
Owen Lars
Beru Whitesun lars
R5-D4
Biggs Darklighter
Obi-Wan Kenobi
```

## Notes
Ensure the Star Wars API (https://swapi-api.alx-tools.com/api/films/) is accessible and working.
Handle possible errors like network issues or invalid movie IDs gracefully.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
