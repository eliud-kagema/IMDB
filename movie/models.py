from django.db import models

CATEGORY_CHOICES = (
    ('A', 'ACTION'),
    ('D', 'DRAMA'),
    ('C', 'COMEDY'),
    ('R', 'ROMANCE'),
)
LANGUAGE_CHOICES = (
    ('EN', 'ENGLISH'),
    ('GR', 'GERMAN'),
)

STATUS_CHOICES = (
    ('RA', 'RECENTLY ADDED'),
    ('MW', 'MOST WATCHED'),
    ('TR', 'TOP RATED'),
)

RATINGS = (
    ('NR', 'Not Rated'),
    ('G', 'General Audiences'),
    ('PG', 'Parental Audiences'),
    ('R', 'Restricted'),
)
    
class Movie(models.Model):
    title = models.CharField(max_length=140)
    description = models.TextField(max_length=10000)
    image = models.ImageField(upload_to='movies')
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=1)
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=2)
    status = models.CharField(choices=STATUS_CHOICES, max_length=2)
    director = models.CharField(max_length=140)
    cast = models.CharField(max_length=100)
    rating = models.CharField(choices=RATINGS, max_length=2)
    year_of_prodcution = models.DateField()
    views_count = models.IntegerField(default=0)
    

    def __str__(self):
        return self.title



LINK_CHOICES = (
    ('D', 'Download'),
    ('W', 'Watch'),
)
class MovieLinks(models.Model):
    movie = models.ForeignKey(Movie, related_name='movie_watch_link', on_delete=models.CASCADE)
    type = models.CharField(choices=LINK_CHOICES, max_length=1)
    link = models.URLField()

    def __str(self):
        return str(self.movie)

    class Meta:
        verbose_name = 'Movie Links'
        verbose_name_plural = 'Movie Links'
