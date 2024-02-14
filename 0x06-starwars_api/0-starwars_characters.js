#!/usr/bin/node
/**
 * Prints all characters of a Star Wars movie
 * The first positional argument passed is the Movie ID
 * Display one character name per line in the same order
 * as'characters' list in the /films/ endpoint.
 */

const request = require('request');

const makeRequest = (url) => {
    return new Promise((resolve, reject) => {
        request.get(url, (err, response, body) => {
            if (err) {
                reject(err);
            } else {
                resolve(body);
            }
        });
    });
};

const getCharacters = async () => {

    const films = await makeRequest(`https://swapi-api.alx-tools.com/api/films/${process.argv[2]}/`);
    const characters = JSON.parse(films).characters;

    for (let i = 0; i < characters.length; i++) {
        const character = await makeRequest(characters[i]);
        console.log(JSON.parse(character).name);
    }
}

getCharacters();
