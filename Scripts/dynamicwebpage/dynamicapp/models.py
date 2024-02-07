from django.db import models

class mission(models.Model):
    content = models.TextField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    def __str__(self):
        return f"mission #{self.pk}"
    
class vision(models.Model):
    vcontent = models.TextField()
    def __str__(self):
        return f"vision #{self.pk}"

class slogan(models.Model):
    slcontent = models.TextField()
    def __str__(self):
        return f"slogan #{self.pk}"


class pic1(models.Model):
    caption = models.CharField(max_length=255)
    image = models.ImageField(upload_to='templates/dynamic_page.html', null=True, blank=True)
    def __str__(self):
        return f"pic1 #{self.pk} - {self.caption}"

class about(models.Model):
    abtcontent = models.TextField()
    def __str__(self):
        return f"about #{self.pk}"
    
class whatsets(models.Model):
    wscontent = models.TextField()
    def __str__(self):
        return f"whatsets #{self.pk}"
class post1(models.Model):
    p1content = models.TextField()
    def __str__(self):
        return f"post1 #{self.pk}"
    
class post2(models.Model):
    p2content = models.TextField()
    def __str__(self):
        return f"post1 #{self.pk}"

class post3(models.Model):
    p3content = models.TextField()
    def __str__(self):
        return f"post3 #{self.pk}"

class obj1(models.Model):
    obj1content = models.TextField()
    def __str__(self):
        return f"obj1 #{self.pk}"

class obj2(models.Model):
    obj2content = models.TextField()
    def __str__(self):
        return f"obj2 #{self.pk}"

class obj3(models.Model):
    obj3content = models.TextField()
    def __str__(self):
        return f"obj3 #{self.pk}"

class obj4(models.Model):
    obj4content = models.TextField()
    def __str__(self):
        return f"obj4 #{self.pk}"

class obj5(models.Model):
    obj5content = models.TextField()
    def __str__(self):
        return f"obj5 #{self.pk}"

class obj6(models.Model):
    obj6content = models.TextField()
    def __str__(self):
        return f"obj6 #{self.pk}"

class obj7(models.Model):
    obj7content = models.TextField()
    def __str__(self):
        return f"obj7 #{self.pk}"


class Image(models.Model):
    image = models.ImageField(upload_to='images/')

class Signup(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.CharField(max_length=20)
    password = models.CharField(max_length=100)
