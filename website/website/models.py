from django.db import models
import os, shutil, pdb
from website.settings import MEDIA_ROOT
from django.dispatch import receiver

def upload_path(instance, filename):
        return os.path.join(instance.name, filename)

def upload_path_sub(instance, filename):
        return os.path.join(instance.project.name, filename)

class Project(models.Model):
    name         = models.CharField(max_length=10, primary_key=True, verbose_name='Nombre')
    main_img     = models.ImageField(upload_to=upload_path, verbose_name='Imagen de presentacion')
    description  = models.TextField()
    
    class Meta:
        verbose_name = 'Proyecto'

    def __str__(self):
        return self.name

class Image(models.Model):
    project = models.ForeignKey('Project' , on_delete=models.CASCADE, related_name="images")
    img = models.ImageField(upload_to=upload_path_sub, verbose_name='Imagenes')

@receiver(models.signals.pre_delete, sender=Project)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    shutil.rmtree(os.path.join(MEDIA_ROOT, instance.name))
