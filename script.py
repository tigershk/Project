import csv

with open ('films.csv') as file:
    reader = csv.DictReader(file)

    for row in reader:
        # print (row)
        # title,imdb_id=row
        mylist= (row['title'],row['imdb_id'])
        print (mylist)
        #  print (row['id'],row['imdb_id'],row['title'],row['overview'])
     

my_list = ['foo', 'bar']
      