from django.db import models

class PersonManager(models.Manager):
    def all_with_prefetch_movies(self):
        qs = self.get_queryset()
        return qs.prefetch_related('directed', 'writing_credits', 'role_set_movie')

class Person(models.Model):
    fname = models.CharField(max_length=140)
    lname = models.CharField(max_length=140)

    objects = PersonManager()

    class Meta:
        ordering = ('fname', 'lname')
        verbose_name = 'Person'
        verbose_name_plural = 'Person'

    def _str__(self):
        return '{} , {}'.format(self.fname, self.lname)

class MovieManager(models.Manager):
    def all_with_related_persons(self):
        qs = self.get_queryset()
        qs = qs.select_related('director')
        qs = qs.prefetch_related('writers', 'actors')
        return qs

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
    director = models.ForeignKey(to='Person', on_delete=models.SET_NULL, related_name='directed', blank=True, null=True)
    writers = models.ManyToManyField(to='Person',  related_name='writing_credits', blank=True)
    actors = models.ManyToManyField(to='Person', through='Role',  related_name='acting_credits', blank=True)
    cast = models.CharField(max_length=100)
    rating = models.CharField(choices=RATINGS, max_length=2)
    year_of_prodcution = models.DateField()
    views_count = models.IntegerField(default=0)

    objects = MovieManager()
    
    class Meta:
        ordering = ('-year_of_prodcution', 'title')

    def __str__(self):
        return self.title

class Role(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.DO_NOTHING)
    person = models.ForeignKey(Person, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=140)

    class Meta:
        unique_together = ('movie','person', 'name')

    def __str__(self):
        return "{} {} {}".format(self.movie_id, self.person_id, self.name)






LINK_CHOICES = (
    ('D', 'Download'),
    ('W', 'Watch'),
)
class MovieLinks(models.Model):
    movie = models.ForeignKey(Movie, related_name='movie_watch_link', on_delete=models.CASCADE)
    type = models.CharField(choices=LINK_CHOICES, max_length=1)
    link = models.URLField()

    def __str__(self):
        return str(self.movie)

    class Meta:
        verbose_name = 'Movie Links'
        verbose_name_plural = 'Movie Links'
