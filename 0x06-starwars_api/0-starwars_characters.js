#!/usr/bin/node

const request = require('request');

if (process.argv.length < 3) {
  console.log('Usage: node 0-starwars_characters.js <film-id>');
  process.exit(1);
}
const filmId = process.argv[2];

const apiUrl = 'https://swapi-api.alx-tools.com/api/';
const url = `${apiUrl}films/${filmId}/`;

request(url, async (error, response, body) => {
  if (error) {
    console.error(error);
    process.exit(1);
  }
  if (response.statusCode !== 200) {
    console.error(`Error fetching ${url}: ${response.statusCode}`);
    process.exit(1);
  }
  const data = JSON.parse(body);
  for (const characterUrl of data.characters) {
    const character = await getCharacter(characterUrl);
    console.log(character);
  }
});

function getCharacter (characterUrl) {
  return new Promise((resolve, reject) => {
    request(characterUrl, async (error, response, body) => {
      if (error) {
        reject(error);
      }
      if (response.statusCode !== 200) {
        reject(Error(`Error fetching ${url}: ${response.statusCode}`));
      }
      const data = JSON.parse(body);
      resolve(data.name);
    });
  });
}
