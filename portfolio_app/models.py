from django.db import models



class Project(models.Model):
    class Meta:
        db_table = 'portfolio_app_project'
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')  # Requires media settings
    github_url = models.URLField(max_length=200)

    def __str__(self):
        return self.title



class Message(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
