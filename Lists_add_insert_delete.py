fav_movies = ["Sandlot", "The Lego Movie", "Dune"]

#find out length of the list 
print(len(fav_movies)) # prints 3 as there are 3 itemsin the list 

#to add another item to the list 
fav_movies.append("Iron Man") #this added another item to the end of the list 
print(len(fav_movies))
print(fav_movies)

#to add item in a specific place 
fav_movies.insert(1, "Batman") #enter in brackets what position do you want to place the item and then the actual item 
print(fav_movies)

#to remove item 
del(fav_movies[2])
print(fav_movies)

#challenge remove enough items from fav_movies until there's only one movie left

del(fav_movies[0])
print(fav_movies)
del(fav_movies[0])
print(fav_movies)
del(fav_movies[0])
print(fav_movies)