from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.text import slugify

class Ads(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField()
    date = models.DateField(auto_now_add=True, null=True, blank=True)
    slug = models.SlugField(unique=True)

    lar = 'Laravel'
    dja = 'Django'
    aspNet = 'ASP.NET'
    node = 'Node.js'
    spring = 'Spring'
    flask = 'Flask'

    urgent = 'Urgent'
    normal = 'Normal'

    urgency = (
        (urgent, 'Urgent'),
        (normal, 'Normal')
    )

    frameworks = (
        (lar, 'Laravel'),
        (dja, 'Django'),
        (aspNet, 'ASP.NET'),
        (node, 'Node.js'),
        (spring, 'spring'),
        (flask, 'Flask')
    )

    framework = models.CharField(
        max_length=50,
        choices=frameworks,
    )

    priority = models.CharField(
        max_length=50,
        choices=urgency,
        null=True
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('ad-detail', args=[str(self.slug)])

    def _get_unique_slug(self):
        slug = slugify(self.title)
        unique_slug = slug
        num = 1
        while Ads.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save(*args, **kwargs)
