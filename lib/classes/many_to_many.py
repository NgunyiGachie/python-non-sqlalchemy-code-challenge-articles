class Article:
    all = []
    def __init__(self, author, magazine, title):
        self._author = author
        self._magazine = magazine
        self._title = title
        Article.all.append(self)

    @property
    def title(self):
        return self.title
    
    @title.setter
    def title(self,value):
        if not isinstance(value, str):
            raise Exception("Title must be a string.")
        self._title = value
        if len(value) < 5 and len(value) > 50:
            raise Exception("Title must be between 5 and 50 characters.")
        self._title = value
        if hasattr(self, '_title'):
            print(f"title must have the value: {self._title}")

    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, article_author):
        if isinstance(article_author, Author):
            self._author.append(article_author)
        else:
            raise ValueError("Author must be of type Author.")
        if hasattr(self, '_author'):
            print(f"The attribute 'author' is set to: {self._author}")

    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self, magazine_article):
        if isinstance(magazine_article, Magazine):
            self._magazine.append(magazine_article)
        else:
            raise ValueError("Magazine must be of type Magazine.")
        if hasattr(self, '_magazine'):
            print(f"The attribute 'magazine' is set to: {self._magazine}")
            
        
class Author:
    all = []
    AUTHOR_LIST = []

    def __init__(self, name=""):
        self._name = name
        Author.all.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise Exception("Name must be a string.")
        self._name = value
        if len(value) <= 0:
            raise Exception("Name must contain at least one character")
        self._name = value
        if hasattr(self, '_name'):
            print(f"The attribute 'name' is set to: {self._name}")

    def articles(self, article=None):
        if article is not None:
            if not isinstance(article, Article):
                raise ValueError("Article must be of type Article.")
        return [article for article in Article.all if article.author == self]


    def magazines(self, magazine=None):
        if magazine is not None:
            if not isinstance(magazine, Magazine):
                raise ValueError("Magazine must be of type Magazine.")
        return magazine in Magazine.MAGAZINE_LIST

    def add_article(self, magazine, title):
        pass

    def topic_areas(self):
        pass

class Magazine:
    all = []
    MAGAZINE_LIST = []
    
    def __init__(self, name, category):
        self._name = name
        self._category= category
        Magazine.all.append(self)

    @property
    def name(self):
        return self._name 
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise Exception("Name must be a string.")
        self._name = value
        if len(value) < 2 and len(value) > 16:
            raise Exception("Name must contain between 2 and 16 characters.")
        self._name = value
        if hasattr(self, '_name'):
            print(f"Changing name from {self._name} to {value}.")
        self._name = value

    @property
    def category(self):
        return self._category 
    
    @category.setter
    def category(self, value):
        if not isinstance(value, str):
            raise Exception("Category must be a string.")
        self._category = value
        if len(value) < 0:
            raise Exception("Category must be larger than 0 characters.")
        if hasattr(self, '_category'):
            print(f"Changing category from {self._category} to {value}")

    def articles(self, article=None):
        if article is not None:
            if not isinstance(article, Article):
                raise ValueError("Article must be of type Article.")
        return [article for article in Article.all if article.magazine == self]

    def contributors(self, author=None):
        if author is not None:
            if not isinstance(author, Author):
                raise ValueError("Author must be of type Author.")
        return author in Author.AUTHOR_LIST

    def article_titles(self):
        pass

    def contributing_authors(self):
        pass