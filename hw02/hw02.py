import csv
import json

import pandas as pd

file = open("movies.csv", "r", encoding="utf-8-sig")
reader = csv.DictReader(file)
movies = []
for row in reader:
    movies.append(row)
file.close()

# Calculate the average of the SeanScores

average = 0
for movie in movies:
    average += int(movie["SeanScore"])
average = average / len(movies)
print(f"Sean's average score on movies he has seen is {average}")

with open("movies.json", "w", encoding="utf-8-sig") as jsonfile:
    print(json.dumps(movies, indent=2))
    jsonfile.write(json.dumps(movies, indent=2))

with open("movies.xml", "w", encoding="utf-8-sig") as xmlfile:
    xmlfile.write("<movies>\n")
    for movie in movies:
        print(movie["Title"])
        xmlfile.write(f"  <movie>\n")
        xmlfile.write(f"    <title>{movie['Title']}</title>\n")
        xmlfile.write(f"    <year>{movie['Year']}</year>\n")
        xmlfile.write(f"    <tomatoMeter>{movie['TomatoMeter']}</tomatoMeter>\n")
        xmlfile.write(f"    <audienceScore>{movie['AudienceScore']}</audienceScore>\n")
        xmlfile.write(f"    <seanScore>{movie['SeanScore']}</seanScore>\n")
        xmlfile.write(f"  </movie>\n")
    xmlfile.write("</movies>\n")

# Let's do the same stuff but with the pandas library!

df = pd.read_excel("movies.xlsx")
# print(df.head())
with open("movies.html", "w", encoding="utf-8-sig") as htmlfile:
    htmlfile.write(df.to_html())
print(f"Sean's average score on movies he has seen is {df["SeanScore"].mean()}")
