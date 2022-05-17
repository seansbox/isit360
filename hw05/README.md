# HW05 Data Without Structure, with Structure

## How to setup dependencies (MongoDB for non-production testing)

Windows

    choco install mongodb

macOS

    brew tap mongodb/brew
    brew update
    brew install mongodb-community

Both

    mkdir hw05
    cd hw05
    mkdir data
    mongod --dbpath data
    (use my data/.gitignore to ignore the DB files if you're using GIT)

## How to 'MongoDB' from the command-line

    mongo
    > db
    > use movies
    > db.movies.insert({ "name": "The Wizard of Oz", "release": new Date("1939-08-25"), "thumb": "https://resizing.flixster.com/ulqUDhVVuKGWDLeBtkp9KjyReo8=/206x305/v2/https://flxt.tmsimg.com/NowShowing/129612/129612_ab.jpg", "summary": "When a tornado rips through Kansas, Dorothy (Judy Garland) and her dog, Toto, are whisked away in their house to the magical land of Oz. They follow the Yellow Brick Road toward the Emerald City to meet the Wizard, and en route they meet a Scarecrow (Ray Bolger) that needs a brain, a Tin Man (Jack Haley) missing a heart, and a Cowardly Lion (Bert Lahr) who wants courage. The wizard asks the group to bring him the broom of the Wicked Witch of the West (Margaret Hamilton) to earn his help.", "meter": 98, "score": 89 })
    > show dbs
    > db.movies.find({ meter: { $gt: 80 } })
    > db.movies.updateMany({ name: "The Wizard of Oz" }, { $set: { meter: 100 } })
    > db.movies.updateMany({ name: "The Wizard of Oz" }, { $inc: { meter: 100 } })
    > db.movies.deleteMany({ name: "The Wizard of Oz" })

## How to 'MongoDB' in Python

    poetry config virtualenvs.in-project true
    poetry init -n
    code .
    poetry add pymongo
    (build your hw05.py file)
    poetry run python hw05.py

## How to run this folder

    poetry install
    poetry run python hw05.py

## Ways to reference movies/celebs...

- movies contains a list of celeb ids...
- celebs contains a list of movie ids...
- another collection contains movie-to-celeb mappings

Each has implications on performance and CRUD operations.

## Handy references

- MongoDB Query Selectors: https://www.mongodb.com/docs/manual/reference/operator/query/#std-label-query-selectors
- PyMongo Collection API: https://pymongo.readthedocs.io/en/stable/api/pymongo/collection.html
- AWS Database Services: https://aws.amazon.com/products/databases/
