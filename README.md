# docker-api

## Overview

Quick API made with Django, Django-Rest-Framework, PostgreSQL, and Docker.

Collects Pokémon data from [PokéApi](pokeapi.co) on startup and saves into a local database. Django then serves as an API for this database.

Basic features are included such as fetching a list of all the Pokémon, detailed stats of specific Pokémon, as well as gathering the average stats of either all Pokémon, or the average stats of only a certain type.

## Instructions

Make sure to install the latest versions of Docker-Desktop, or Docker and Docker-Compose on Linux.

Then clone and run:

```
git clone https://github.com/wbisschoff13/docker-api
cd docker-api
sudo docker-compose up
```

## The API

- `/pokemon/` - List of all Pokémon, with their name, types, and average of their stats.
- `/pokemon/<id>/` - More detailed info for the given Pokémon.
- `/stats/`- List of all Pokémon, but with the average of the average stats calculated, and sorted by average stat.
- `/stats/<type>` - List of all Pokémon with given type as their main type, with the average stat calculated only for that type.

## Considerations

- Include validation for `<id>` and `<type>` and return suitable message
- Include testing and validation for the external API
- Clean up code. It is currently still in the "let's just get something that works" phase.
  - Split code into more functions
  - Add function documentation
- Find a better alternative for adding commands into docker-compose, as well as alternative for using the [./wait-for script](https://github.com/eficode/wait-for/).
  It is what currently allows for the commands to run only after the database is up and running, to ensure everything executes in the correct order from a single `docker-compose up`
- Add volumes so data is not lost after the container is closed. Currently omitted due to getting the data from the external API as a first step in the process.
