from django.db import models

# Create A Blog model
class Blog(models.Model):
	title = models.CharField(null=True, max_length=255)
	pub_date = models.DateTimeField(null=True)
	body = models.TextField(default="ABC")
	image = models.ImageField(upload_to='images/')

	

#Add the Blog app to the settings

#Create migration

#Migrate

#Add to the admin


