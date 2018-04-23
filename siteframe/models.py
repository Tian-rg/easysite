from django.db import models


# Create your models here.
class TopLevelTopic(models.Model):
    tlp_text = models.CharField(max_length=20)
    tlp_description = models.CharField(max_length=250)

    def __str__(self):
        return self.tlp_text

class Tag(models.Model):
    tag_name = models.CharField(max_length=20)

    def __str__(self):
        return self.tag_name

class Author(models.Model):
    first_name = models.CharField(max_length=20)
    second_name = models.CharField(max_length=20)
    birthday = models.DateField()
    nationality = models.CharField(max_length=20)
    email = models.EmailField(default="authorname@example.com")

    def __str__(self):
        return 'Author: %s %s'%(self.first_name, self.second_name)

class Article(models.Model):
    article_title = models.CharField(max_length=50)
    article_authors = models.ManyToManyField(Author)
    article_body = models.CharField(max_length=5000)
    article_pubdate = models.DateTimeField('date published')
    article_tag = models.ManyToManyField(Tag)

    def __str__(self):
        tmpstr = (self.article_title,self.article_author,self.article_pubdate)
        return 'Article: %s %s %s'%tmpstr

# The following models are for practice making query in database
class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):
        return self.name

class BlogAuthor(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Entry(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField()
    authors = models.ManyToManyField(BlogAuthor)
    n_comments = models.IntegerField()
    n_pingbacks = models.IntegerField()
    rating = models.IntegerField()

    def __str__(self):
        return self.headline
