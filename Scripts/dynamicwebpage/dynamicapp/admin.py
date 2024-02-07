from django.contrib import admin
from .models import mission
from .models import vision, slogan
from .models import pic1, about, whatsets, post1, post3, post2
from .models import obj1, obj2, obj3, obj4, obj5, obj6, obj7, Image


class missionAdmin(admin.ModelAdmin):
    list_display = ('id', 'content')
    search_fields = ('content',)

admin.site.register(mission, missionAdmin)

class visionAdmin(admin.ModelAdmin):
    list_display = ('id', 'vcontent')
    search_fields = ('vcontent',)

admin.site.register(vision, visionAdmin)

class sloganAdmin(admin.ModelAdmin):
    list_display = ('id', 'slcontent')
    search_fields = ('slcontent',)

admin.site.register(slogan, sloganAdmin)

class Pic1Admin(admin.ModelAdmin):
    list_display = ('id', 'caption', 'image')
    search_fields = ('caption',)

admin.site.register(pic1, Pic1Admin)

class aboutAdmin(admin.ModelAdmin):
    list_display = ('id', 'abtcontent')
    search_fields = ('abtcontent',)
admin.site.register(about, aboutAdmin)

class whatsetsAdmin(admin.ModelAdmin):
    list_display = ('id', 'wscontent')
    search_fields = ('wscontent',)
admin.site.register(whatsets, whatsetsAdmin)

class post1Admin(admin.ModelAdmin):
    list_display = ('id', 'p1content')
    search_fields = ('p1content',)
admin.site.register(post1, post1Admin)

class post2Admin(admin.ModelAdmin):
    list_display = ('id', 'p2content')
    search_fields = ('p2content',)
admin.site.register(post2, post2Admin)

class post3Admin(admin.ModelAdmin):
    list_display = ('id', 'p3content')
    search_fields = ('p3content',)
admin.site.register(post3, post3Admin)

class obj1Admin(admin.ModelAdmin):
    list_display = ('id', 'obj1content')
    search_fields = ('obj1content',)
admin.site.register(obj1, obj1Admin)

class obj2Admin(admin.ModelAdmin):
    list_display = ('id', 'obj2content')
    search_fields = ('obj2content',)
admin.site.register(obj2, obj2Admin)

class obj3Admin(admin.ModelAdmin):
    list_display = ('id', 'obj3content')
    search_fields = ('obj3content',)
admin.site.register(obj3, obj3Admin)

class obj4Admin(admin.ModelAdmin):
    list_display = ('id', 'obj4content')
    search_fields = ('obj4content',)
admin.site.register(obj4, obj4Admin)

class obj5Admin(admin.ModelAdmin):
    list_display = ('id', 'obj5content')
    search_fields = ('obj5content',)
admin.site.register(obj5, obj5Admin)

class obj6Admin(admin.ModelAdmin):
    list_display = ('id', 'obj6content')
    search_fields = ('obj6content',)
admin.site.register(obj6, obj6Admin)

class obj7Admin(admin.ModelAdmin):
    list_display = ('id', 'obj7content')
    search_fields = ('obj7content',)
admin.site.register(obj7, obj7Admin)

#class Image(admin.ModelAdmin):
    #list_display = ('id', 'Image')
admin.site.register(Image)

#@admin.register(Image)
#class ImageAdmin(admin.ModelAdmin):
 #   pass







