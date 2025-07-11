# Rules
A note about all the rules for RNG. They should use a seeded number generator so a player can start their own game with the same seed. The seed is held by the server so the clients wouldn't see it. But if a player wants to start a game with the same universe they can. 

## Universe Generation
- Universe is a 32 x 32 grid with a roll for each cell to determine if empty based on a population density value. 

## System Generation
- Each system is generated with a random number of planets and or other features. it can be a standard system, a nebula or a collapsed star such as neutron, black hole or white dwarf.
- A random chance of a empire artifact or ancient artifact being present in the system.
- If it is a starting system then also have a space fairing race present.

## Planet Generation
- Each planet has a random population density value.
- Each planet has a random number of resources based on the resource density value.

