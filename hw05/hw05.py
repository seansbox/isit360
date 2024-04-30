import datetime
from pymongo import MongoClient

client = MongoClient()
print('databases:', client.list_database_names())
db = client.movies
print('movies:', db)

movie_data = {
    "name": "The Wizard of Oz",
    "release": datetime.datetime(1939, 8, 25),
    "thumb": "https://resizing.flixster.com/ulqUDhVVuKGWDLeBtkp9KjyReo8=/206x305/v2/https://flxt.tmsimg.com/NowShowing/129612/129612_ab.jpg",
    "summary": "When a tornado rips through Kansas, Dorothy (Judy Garland) and her dog, Toto, are whisked away in their house to the magical land of Oz. They follow the Yellow Brick Road toward the Emerald City to meet the Wizard, and en route they meet a Scarecrow (Ray Bolger) that needs a brain, a Tin Man (Jack Haley) missing a heart, and a Cowardly Lion (Bert Lahr) who wants courage. The wizard asks the group to bring him the broom of the Wicked Witch of the West (Margaret Hamilton) to earn his help.",
    "meter": 98,
    "score": 89
}

# db.movies.insert_one(movie_data)
db.movies.find_one_and_update(
    { 'name': "The Wizard of Oz" },
    { '$set': movie_data },
    upsert = True
)

celeb_data = {
    'name': 'Judy Garland',
    'birthday': datetime.datetime(1922, 6, 10),
    'birthplace': "Grand Rapids, Minnesota, USA",
    'thumb': "https://resizing.flixster.com/OMfygJ2W2siVuOs3yN1JDb9sCGk=/218x280/v2/https://flxt.tmsimg.com/assets/72714_v9_ba.jpg",
    'summary': "Judy Garland was born Frances Ethel Gumm on June 10, 1922 in Grand Rapids, MN. She was born into a family of vaudevillians and joined her older sisters in performing at their parents' Minnesota theater at a young age. The Gumm family relocated to Lancaster, CA in 1926, and Garland began studying dance properly two years later. Following a few years of performing in stage productions and film shorts with her siblings, a 13-year-old Garland was signed by Metro-Goldwyn-Mayer in 1935. Some of her earliest features included ""Thoroughbreds Don't Cry"" (1937) and ""Love Finds Andy Hardy"" (1938), both of which costarred Mickey Rooney. All the while, Garland began what would become long-term abuse of amphetamines and barbiturates, as provoked by the studio system. Within two years of her breaking out as a solo act, Garland landed what would be the most iconic role of her career: Dorothy in ""The Wizard of Oz"" (1938). The 1940s saw Garland take on more adult-oriented roles, beginning with ""Little Nellie Kelly"" (1940), and experience her first marriage-to composer David Rose in 1941, as well as their divorce three years later. She would go on to star in the smash hit ""Meet Me in St. Louis"" (1944) and experiment with non-musical drama in the critically revered ""The Clock"" (1945). Shortly afterward, she married Vincent Minelli, with whom she'd bear daughter Liza Minelli. In the late 1940s, Garland suffered her first suicide attempt and was hospitalized briefly. The stint preceded her first commercial failure in a decade, ""The Pirate"" (1947), though Garland earned far more successful returns with the following year's ""Easter Parade"" (1948). Nevertheless, Garland's acting slowed in the 1950s, during which time she appeared only in ""Summer Stock"" (1950) and the now iconic ""A Star Is Born"" (1954). Also during this period, Garland married Sidney Luft and gave birth to Lorna Luft. In the 1960s, Garland starred in dramas including ""Judgment at Nuremberg"" (1961) and John Cassavetes' ""A Child Is Waiting"" (1963), and, her final picture, the musical ""I Could Go on Singing"" (1963). She then headlined her own variety musical program ""The Judy Garland Show"" (CBS 1963-64). On June 22, 1969, Garland died at age 47 following a barbiturate overdose."
}

# db.celebs.insert_one(celeb_data)
db.celebs.find_one_and_update(
    { 'name': "Judy Garland" },
    { '$set': celeb_data },
    upsert = True
)

d = datetime.datetime(1979, 11, 30)
for doc in db.movies.find({ 'release': { '$lt': d } }):
    print('found:', doc)

client.close()