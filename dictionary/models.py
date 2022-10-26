from email.policy import default
from django.db import models

from django.contrib.auth.models import User
from django.urls import reverse

class Author(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(unique=True, blank=True, null=True)
    first_name = models.CharField(max_length=100, null=True, blank=True, verbose_name='First Name')
    last_name = models.CharField(max_length=100, null=True, blank=True,verbose_name='Last Name')
    designation = models.CharField(max_length=10, null=True)
    author_image = models.ImageField(upload_to='author/',verbose_name='Author Profile Image',blank=True, null=True)
    auth_status = models.CharField(max_length=100, null=True)

    class Meta:
        verbose_name_plural = 'Author'
    

    def __str__(self):
        return self.author.username

# category model
class Category(models.Model):
    name = models.CharField(max_length=200, null=True)
    slug = models.SlugField(null=True)
    image = models.CharField(max_length=300, blank=True, null=True)
    description = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self) -> str:
        return self.name


# tags model
class Tag(models.Model):
    name = models.CharField(max_length=100, null=True)

    def __str__(self) -> str:
        return self.name


# model for words and meaning
class Jargon(models.Model):
    STATUS = (
        ('active', 'active'),
        ('pending', 'pending')
    )

    word = models.CharField(max_length=100, null=True, help_text="A word related to tech.")
    meaning = models.TextField(max_length=500, null=True, help_text="The meaning of the word")
    image = models.ImageField(upload_to="images/media", null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, null=True)
    tags = models.ManyToManyField(Tag, blank=True)
    status = models.CharField(max_length=20, choices=STATUS, default='pending')
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    featured = models.BooleanField(default=False)
    visit_count = models.IntegerField(default=0)
    visible = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Jargons"

    def excerpt(self):
        short = self.meaning[:150]
        return f"{short}..."


    def get_username(self):
        return self.author.author.username

    def get_absolute_url(self):
        return reverse("definition", kwargs={"id": self.id})


    def get_category(self):
        return self.category.name
    

    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url


    @property
    def get_user_image_url(self):
        if self.author.author_image and hasattr(self.author.author_image, 'url'):
            return self.author.author_image.url


    def __str__(self) -> str:
        return f"{self.word} by {self.author.author.username}"


# Comment Class
class Comment(models.Model):
    post = models.ForeignKey(Jargon, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100, null=True, blank=False)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.post.title} | {self.name } "

# Reply Class
class Reply(models.Model):
    comment = models.ForeignKey(Comment,on_delete=models.CASCADE, related_name='reply')
    name = models.CharField(max_length=200, null=True, blank=False)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.comment} | { self.name } |{ self.created_at }"


# email marketing system 
class EmailSignUp(models.Model):
    email  = models.EmailField(blank=True)

    class Meta:
        verbose_name_plural = " User Emails"

    def __str__(self):
        return self.email

class Contact(models.Model):
    name = models.CharField(max_length=100, null=True, verbose_name='Name')
    email = models.EmailField(null=True)
    messages = models.TextField()
    subject = models.CharField(max_length=200, null=True, verbose_name='Subjects' )

    def __str__(self):
        return f"{ self.name } | { self.subject}"



