movies = [
          "Star Wars", "Gandhi", "Casablance", "Shawshank Redemption", "Toy Story",
          "Gone with the Wind", "Citizen Kane", "It's a Wonderful Life", "The Wizard of Oz",
          "Gataca", "Rear Window", "Ghostbusters", "To Kill A Mockingbird", "Good Will Hunting",
          "2001: A Space Odyssey", "Raiders of the Lost Ark", "Groudhog Day", "Close Encouters of the Third Kind"
          ]
# Find movies that has title starting with T
gmovies = [title for title in movies if title.startswith("T")]   
print(gmovies)

movies = [
          ("Citizen Kane", 1941), ("Spirited Away", 2001), ("It's Wonderful Life", 1946),
          ("Gattaca", 1997), ("No Country for Old Men", 2007), ("Rear Window", 1954),
          ("The Lord of the Rings: The Fellowship of the Ring", 2001), ("Groundhog Day", 1993),
          ("Close Encounters of the Third Kind", 1977), ("The Royal Tenenbaums", 2001),
          ("The Aviator", 2004), ("Raiders of the Lost Ark", 1981)
         ]
# Find movies release before 2000
# Dictionary as Return Value
rmovies = { title : year for (title,year) in movies if year < 2000}
# List as a Return Value
rmovies = [(title,year) for title,year in movies if year < 2000]

print(rmovies)
