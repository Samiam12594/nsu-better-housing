# NSU Better Housing
**Welcome to NSU Better Housing! Please follow the instructions below to properly install our application.**

## Pre-requisites:
- Install [MongoDB Compass](https://www.mongodb.com/try/download/compass)
- Install [MongoDB Community Server](https://www.mongodb.com/try/download/community)
- Have Python installed.


## Running with Docker (recommended)
1. Install Docker Desktop and make sure it is running.
2. From this folder, build and start the stack:
   ```
   docker compose up --build
   ```
3. Open `http://localhost:8000/` in your browser. The MongoDB container is seeded automatically from `datasets/*.json`.
   - MongoDB is exposed on host port `27018` to avoid conflicts with a locally running `mongod`.
4. To access the database and its contents, copy+paste this URI into browser: `mongodb://localhost:27018`
   1. You MUST have MongoDB Compass installed in order for this to work (see Pre-requisites)

## Running natively (legacy)
1. Please ensure MongoDB Compass is open and running properly, as the datasets will be inserted to the Database.
2. Open up 'Run.sh' within this folder. This will auto-install any necessary extensions and open up the server on your favorite browser.
3. Control-click on the IP address [Ex: `http://127.0.0.1:8000/`]
4. You will need to register an account if this is the first time using the application.
5. Enjoy NSUBH!

---
Any questions should be sent through gitHub to Lavaughn's account.

## Change History
- Added Dockerized stack (`Dockerfile`, `docker-compose.yml`, `docker-entrypoint.sh`, `.dockerignore`) and documented usage in this README.
- Introduced `requirements.txt` and environment-driven `MONGO_URI` for all Django view modules.
- Updated Mongo port mapping to 27018 and fixed seeding script path/escaping for `datasets/*.json`.
