from django.db import models
import uuid
# Create your models here.
class TextModel(models.Model):
	id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
	title = models.CharField(max_length = 255)
	body = models.TextField()

    def __str__(self):
        return self.Title