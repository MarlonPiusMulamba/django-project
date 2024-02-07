from django.shortcuts import get_object_or_404, render, redirect
from .models import mission
from .models import vision
from .models import slogan
from .models import pic1
from .models import about, post1, post2, post3, obj1, Image
from django.contrib.admin.views.decorators import staff_member_required
from .forms import Image


def dynamic_page(request):
    contents = mission.objects.all()
    vcontents = vision.objects.all()
    slcontents = slogan.objects.all()
    pic1_instance = pic1.objects.first()
    abtcontents = about.objects.all()
    p1contents = post1.objects.all()
    p2contents = post2.objects.all()
    p3contents = post3.objects.all()
    obj1contents = obj1.objects.all()
    image = Image.objects.all()


    return render(request, 'dynamicapp/dynamic_page.html', {'contents': 
    contents, 'vcontents': vcontents, 'slcontents': slcontents,
    'pic1_instance' :pic1_instance, 'abtcontents': abtcontents,
    'p1contents' : p1contents, 'p2contents': p2contents, 'p3contents': p3contents,
   'obj1contents': obj1contents, 'image':image})

#ef display_pic1(request, pic1_id):
  #  pic1_instance = get_object_or_404(pic1, pk=pic1_id)
   # return render(request, 'display_pic1.html', {'pic1_instance': pic1_instance})

#def display_image(request):
    #image = Image.objects.last()  # Assuming you're retrieving the last uploaded image
    #return render(request, 'display_image.html', {'image': image})

