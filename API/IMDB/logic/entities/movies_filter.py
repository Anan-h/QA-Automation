class MoviesFilter:

    def __init__(self, country, genre):
        self.country = country
        self.genre = genre

    @property
    def country(self):
        return self._country

    @country.setter
    def country(self, name):
        self._country = name

    @property
    def genre(self):
        return self._genre

    @genre.setter
    def genre(self, name):
        self._genre = name

    def to_dict(self):
        return {
            "country": {"anyPrimaryCountries": [self.country]},
            "genre": {"allGenreIds": [self.genre]}
        }
