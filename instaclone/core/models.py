from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    caption = models.TextField()
    image = models.ImageField(upload_to='posts/')
    likes = models.ManyToManyField(User, related_name='liked_posts', blank=True)  # Changed this line
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Post by {self.user.username}"

    def total_likes(self):
        return self.likes.count()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='profiles/', default='profiles/default.png')

    @property
    def profile_image_url(self):
        return self.profile_image.url


class Image(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # <-- Add this line
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

def some_view(request):
    from core.models import Image
    # Example view logic for querying Image objects
    images = Image.objects.all()  # Query all Image objects
    return render(request, 'some_template.html', {'images': images})