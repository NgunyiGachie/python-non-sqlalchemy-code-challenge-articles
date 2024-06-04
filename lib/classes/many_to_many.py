class Author:
    all = []

    def __init__(self, name):
        if not isinstance(name, str) or len(name) <= 0:
            raise ValueError("Name must be a non-empty string.")
        self._name = name
        self._articles = []
        Author.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        raise AttributeError("Cannot modify the name attribute.")

    def add_article(self, magazine, title):
        if not isinstance(magazine, Magazine):
            raise ValueError("Magazine must be of type Magazine.")
        return Article(self, magazine, title)

    def articles(self):
        return self._articles

    def magazines(self):
        return list(set(article.magazine for article in self._articles))

    def topic_areas(self):
        if not self._articles:
            return None
        return list(set(article.magazine.category for article in self._articles))


class Magazine:
    all = []

    def __init__(self, name, category):
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise ValueError("Name must be a string between 2 and 16 characters.")
        if not isinstance(category, str) or len(category) <= 0:
            raise ValueError("Category must be a non-empty string.")
        self._name = name
        self._category = category
        self._articles = []
        Magazine.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not (2 <= len(value) <= 16):
            raise ValueError("Name must be a string between 2 and 16 characters.")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str) or len(value) <= 0:
            raise ValueError("Category must be a non-empty string.")
        self._category = value

    def articles(self):
        return self._articles

    def contributors(self):
        return list(set(article.author for article in self._articles))

    def article_titles(self):
        if not self._articles:
            return None
        return [article.title for article in self._articles]
    
    def contributing_authors(self):
        if not self._articles:
            return None
        author_count = {}
        for article in self._articles:
            author = article.author
            if author not in author_count:
                author_count[author] = 0
            author_count[author] += 1
        contributing_authors = [author for author, count in author_count.items() if count > 2]
        return contributing_authors if contributing_authors else None

    @classmethod
    def top_publisher(cls):
        if not Article.all:
            return None
        return max(cls.all, key=lambda magazine: len(magazine.articles()), default=None)

class Article:
    all = []

    def __init__(self, author, magazine, title):
        if not isinstance(author, Author):
            raise ValueError("Author must be of type Author.")
        if not isinstance(magazine, Magazine):
            raise ValueError("Magazine must be of type Magazine.")
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise ValueError("Title must be a string between 5 and 50 characters.")
        self._author = author
        self._magazine = magazine
        self._title = title
        Article.all.append(self)
        author._articles.append(self)
        magazine._articles.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        raise AttributeError("Cannot modify the title attribute")

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise ValueError("Author must be of type Author.")
        self._author = value

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        if not isinstance(value, Magazine):
            raise ValueError("Magazine must be of type Magazine.")
        self._magazine = value
