# KISS (Keep It Simple, Stupid)

## Description
KISS is about keeping it simple. I want to make a project that uses as few other tools as possible. Javascript keeps growing and features in frameworks trickle into the base language. Once JQuery was the way to work with the DOM. Now many of its better features have been added to javascript. So this project will see how far I can push base javascript to do what I need. 

## Limitations
- Modularity. It needs to be easy to add or move features as needed. I've worked on enough enterprise level projects to know that requirements change. So should the code.
- No dependencies. If I need a library I will just write it. kiss will be the only dependency.
- No frameworks. Again see kiss. 
- I will use testing libraries like jest to do the testing and eslint to make sure the code is clean. 

## Goals
- create an app that has access to the same features as a modern web app without the bloat.
- Understand at what point a framework is needed.
- Make a project that pushes my skills and knowledge as much as the language.
- Easy for others to follow along and learn from.
- Have fun.

## Features
- A game that is desktop and mobile friendly. turned based mutliplayer web game that includes chat, nation building ship building and ability to create alliances for war, trade or just to move through each others territories.
- A base framework that lets me add features as each is completed but that doesnt require a complete refactor to add them.
- Websockets for real time chat. 
- interface that uses a custom built style system that is easy to use and change. 
- package any systems to reimport them as needed. Want to learn the package system and how to publish packages to npm.
- Use a sprite system for images and tokens. Build in blender and export out to a sprite sheet. create python tools to setup a grid of cameras that can render out sheet of images. This will let me build once and just render. Planets, ships, orbital stations etc.
- Use a custom built animation system that uses the sprite system to animate objects. since it will be ships and other static objects with sprites it should require less work than having full character animation. 
- Server side should have strong Authentication, Aurhorization and Accounting. Accounting is important to see what players are actually doing.

- A server will be setup to handle game logic and API to the database. 
- harden the server and game to prevent cheating and hacks.

## Questions
- If Diplomacy do players get to make a character? or will it be a flag? 
- If a flag can i make an easy way to tile/layer graphic elements and colors to make a unique flag?
- What kind of resources will be used?
- can you win using trade and diplomacy or just war?
- What are the levels of allegiance? from partner to ally to protectorate etc.
- Will need documentation for the game for when people need to know how each part works.
- solidify what data formats will be used and how they will be stored.
- how are planets created and the races that live on them. I created a planet and alien generator in python that i can use to start the universe for each game.
- how big will the universe be? 32x32 grid of planets and other objects.
- how many players can play at once? estimate 4-8 players per universe. 
- what are the rules of the game?
- what are the weak points that need security?
- how will the game be monetized?
- how will the game be hosted?
- how will the game be marketed?

## Project Status
This project is in the early stages of development. The initial setup is complete, and I am currently working on the core features.
## How to install it

### Prerequisites
- **Docker Desktop for Windows** (includes Docker Compose)
- **Git** (to clone the repository)

#### Installing Docker Desktop on Windows:
1. Download Docker Desktop from: https://www.docker.com/products/docker-desktop/
2. Run the installer and follow the setup wizard
3. Restart your computer when prompted
4. Launch Docker Desktop and wait for it to start
5. Verify installation by opening PowerShell/Command Prompt and running:
   ```powershell
   docker --version
   docker compose version
   ```

### Installation Steps
1. Clone the repository:
   ```bash
   git clone <your-repo-url>
   cd KISS
   ```

2. Build and start all services:
   ```powershell
   docker compose up -d
   ```

## How to run it

### Starting the Project
```powershell
# Start all services (frontend, backend, database, phpMyAdmin)
docker compose up -d

# View logs (optional)
docker compose logs -f

# Stop all services
docker compose down
```

### Accessing the Application
Once running, you can access:

- **Frontend (Game Interface)**: http://localhost:3000
- **Backend API**: http://localhost:8000
- **phpMyAdmin (Database Management)**: http://localhost:8080
- **MySQL Database**: localhost:3306

### phpMyAdmin Login
- **Server**: mysql
- **Username**: root
- **Password**: root_password (or check your .env file for KISS_MYSQL_ROOT_PASSWORD)

### Environment Variables
The project uses environment variables for configuration. Copy `.env.example` to `.env` and update the values:
```bash
cp .env.example .env
```

Key variables:
- `KISS_MYSQL_ROOT_PASSWORD`: MySQL root password
- `KISS_MYSQL_USER`: Application database user
- `KISS_MYSQL_PASSWORD`: Application database password
- `KISS_MYSQL_DATABASE`: Database name

### Development Workflow
- Frontend files are in `frontend/public/` and `frontend/src/`
- Backend PHP files are in `backend/app/`
- Database files are stored in `database/data/` (persisted on your local filesystem)
- Database initialization scripts can be placed in `database/init/`
- Changes to files are automatically reflected (no need to rebuild containers)
- Database data persists between container restarts and is stored as files

### Useful Commands
```powershell
# Rebuild containers after Dockerfile changes
docker compose up -d --build

# View running containers
docker compose ps

# Access container shell (for debugging)
docker compose exec backend bash
docker compose exec frontend sh

# View logs for specific service
docker compose logs backend
docker compose logs frontend
docker compose logs mysql

# Stop and remove all containers and volumes
docker compose down -v
```

### Troubleshooting

#### Docker Credential Issues
If you encounter an error like `docker-credential-desktop: executable file not found`, try these solutions:

1. **Restart Docker Desktop**:
   - Close Docker Desktop completely
   - Restart Docker Desktop and wait for it to fully load
   - Try running the commands again

2. **Reset Docker Desktop**:
   - Open Docker Desktop
   - Go to Settings → Troubleshoot → Reset to factory defaults
   - Restart and try again

3. **Alternative: Use Docker without credentials**:
   - Open PowerShell as Administrator
   - Run: `docker logout`
   - Try running `docker compose up -d` again

4. **Check Docker Desktop Status**:
   - Make sure Docker Desktop is running (green icon in system tray)
   - Wait for "Docker Desktop is running" message before executing commands

#### Version Warning
The warning about `version` attribute being obsolete can be safely ignored - it has been removed from the docker-compose.yml file.

## how to contribute

## How to support it

If you want to support the project, you can do so in a few ways:

- **Contribute Code**: Check the issues list and see if there's something you'd like to work on. Pull requests are welcome!
- **Spread the Word**: Share the project with others who might be interested.
- **Provide Feedback**: Use the project and let me know what works and what doesn't. Your feedback is invaluable.
- **Report Issues**: If you find bugs or have suggestions for improvements, please open an issue on the project's GitHub page.
- **Follow the Project**: Star the repository on GitHub to keep up with updates and new features.
- **Follow on youtube**: Subscribe to the YouTube channel for progress: https://www.youtube.com/channel/your-channel-link
- **Join the Community**: Engage with other users and contributors on discord: https://discord.gg/your-discord-link
- **Donate**: If you find the project useful and want to support its development, consider making a donation.


### testing formats and other things

### Contact
If you have any questions, suggestions, or just want to say hi, feel free to reach out:
- **Email**: your-email@example.com
- **Twitter**: [@yourtwitterhandle](https://twitter.com/yourtwitterhandle)
- **GitHub**: [your-github-username](https://github.com/your-github-username)
- **YouTube**: [Your YouTube Channel](https://www.youtube.com/channel/your-channel-link)
- **Discord**: [Your Discord Server](https://discord.gg/your-discord-link)


- [ ] Task 1
- [ ] Task 2
- [x] Task 3 (Completed)

term
: definition

X^2^

Here's a sentence with a footnote. [^1]

[^1]: This is the footnote.

==Highlighted Text== and this is not.

![alt text](image.jpg)
[title](https://www.example.com)

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
