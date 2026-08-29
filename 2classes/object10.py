class Movie:
    def __init__(self, movie_name, hero, heroine, rating):
        self.movie_name = movie_name
        self.hero = hero
        self.heroine = heroine
        self.rating = rating
movie1 = Movie("RRR", "Ram Charan", "Alia Bhatt", 9.0)
movie2 = Movie("Pushpa", "Allu Arjun", "Rashmika Mandanna", 8.5)

print("Movie 1 Details:")
print("Movie Name:", movie1.movie_name)
print("Hero:", movie1.hero)
print("Heroine:", movie1.heroine)
print("Rating:", movie1.rating)

print("\nMovie 2 Details:")
print("Movie Name:", movie2.movie_name)
print("Hero:", movie2.hero)
print("Heroine:", movie2.heroine)
print("Rating:", movie2.rating)