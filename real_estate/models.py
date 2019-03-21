from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify


def get_image_filename(project_name):
    slug = slugify(project_name)
    return "uploaded_images/{0}/".format(slug)


class RealEstateProject(models.Model):
    name = models.CharField(max_length=200)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    image = models.ImageField(default='default.jpg',
                              upload_to="uploaded_images/%Y/%m/%d/",
                              verbose_name='Image')
    description = models.TextField()

    def __str__(self):
        return self.name


class SectionProject(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    project = models.ForeignKey(RealEstateProject, on_delete=models.CASCADE)

    def __str__(self):
        return "{0} of {1}".format(self.title, self.project)


class Image(models.Model):
    description = models.CharField(max_length=200)
    section_project = models.ForeignKey(SectionProject,
                                        on_delete=models.CASCADE)
    image = models.ImageField(upload_to="uploaded_images/%Y/%m/%d/",
                              verbose_name='Image')

    def __str__(self):
        return "{0} of {1}".format(self.description, self.section_project)
