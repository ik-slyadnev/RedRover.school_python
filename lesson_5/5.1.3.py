

class Anime:
    def __init__(self, name, episodes):
        self.name = name
        self.episodes = episodes

    def get_episodes(self):
        return self.episodes

    def set_episodes(self, episodes):
        self.episodes = episodes


class Season(Anime):
    def __init__(self, name, episodes, season):
        super().__init__(name, episodes)
        self.season = season

    def get_season(self):
        return self.season

    def set_season(self, season):
        self.season = season

bleach = Season('Bleach', 365, 1)
naruto = Season('Naruto', 500, 2)

# print(bleach.get_episodes())
# print(bleach.get_season())
# print(naruto.get_season())

print(f'Аниме: {bleach.name}, количество серий {bleach.episodes}, всего сезонов {bleach.season}')
print(f'Аниме: {naruto.name}, количество серий {naruto.episodes}, всего сезонов {naruto.season}')