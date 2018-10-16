import csv

with open ('films.csv') as file:
    reader = csv.DictReader(file)

    filmList=[]
    for row in reader:
        filmDictionary= {
                "movieid":row['id'],
                "title":row['title'],
                "imdbid":row['imdb_id'],
                "overview":row['overview']
                }
        filmList.append(filmDictionary)

        
    print (filmList)
     

      