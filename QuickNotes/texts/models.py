from django.db import models
import uuid
from django.contrib.auth.hashers import make_password, check_password
# Create your models here.
class TextModel(models.Model):
	id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
	title = models.CharField(max_length = 255)
	body = models.TextField()
	password = models.CharField(max_length = 255, default = "")
	
	def __str__(self):
		return self.title

	def set_password(self, raw_password):
		self.password = make_password(raw_password, None, "md5")

	def check_password(self, raw_password):
		return check_password(raw_password, self.password)

