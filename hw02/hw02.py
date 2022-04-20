import csv
import json

movies = []

with open('movies.csv', 'r', encoding="utf-8-sig") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        movies.append(row)

with open('movies.xml', 'w', encoding="utf-8-sig") as xmlfile:
    xmlfile.write("<movies>\n")
    for movie in movies:
        print(movie['name'])
        # AS XML ATTRIBUTES
        #xmlfile.write(f"  <movie name=\"{movie['name']}\" year=\"{movie['year']}\" />\n")
        # OR AS XML CHILD TAGS
        xmlfile.write(f"  <movie>\n")
        xmlfile.write(f"    <name>{movie['name']}</name>\n")
        xmlfile.write(f"    <year>{movie['year']}</year>\n")
        xmlfile.write(f"    <genre>{movie['genre']}</genre>\n")
        xmlfile.write(f"    <rotten_tomato>{movie['rotten_tomato']}</rotten_tomato>\n")
        xmlfile.write(f"  </movie>\n")
    xmlfile.write("</movies>\n")

with open('movies.json', 'w', encoding="utf-8-sig") as jsonfile:
    jsonfile.write(json.dumps(movies, indent=2))
