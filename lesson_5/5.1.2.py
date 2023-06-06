
# Создаем класс
class Anime:

    # Метод конструктор класса
    def __init__(self, name, genre, rating):
        self.name = name
        self.genre = genre
        self.__rating = rating

    # Метод для получения рейтинга
    def get_rating(self):
        return self.__rating

    # Метод для установки рейтинга
    def set_rating(self, rating):
        self.__rating = rating


# Создаем подклас и дополнитьный атрибут episodes
class TVSeries(Anime):
    def __init__(self, name, genre, rating, episodes):
        super().__init__(name, genre, rating)
        self.episodes = episodes

# Создаем подклас и дополнитьный атрибут duration

class Movie(Anime):
    def __init__(self, name, genre, rating, duration):
        super().__init__(name, genre, rating)
        self.duration = duration


# Создаем экземпляры классов TVSeries и Movie
one_piece = TVSeries('One Piece', 'Action/Adventure', 8.5, 1000)
naruto = Movie('Naruto', 'Action/Adventure', 8.6, 550)

print(one_piece.get_rating())
print(naruto.get_rating())

one_piece.set_rating(9.0)
naruto.set_rating(9.1)

print(one_piece.get_rating())
print(naruto.get_rating())
