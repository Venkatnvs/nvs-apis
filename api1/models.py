from django.db import models

class EndPoints(models.Model):
    title = models.CharField(max_length=255,unique=True,null=True)
    slug = models.CharField(max_length=255,unique=True,null=True)
    request = models.CharField(max_length=255,null=True)
    request_type = models.CharField(max_length=255,null=True)
    description = models.TextField(null=True)
    request_input = models.TextField(null=True)
    request_output = models.TextField(null=True)
    is_active = models.BooleanField(default=True)
    is_free = models.BooleanField(default=True)
    meta_keywords = models.CharField(max_length=255, help_text="Comma seperated set of SEO Keywords for meta tag",null=True,blank=True)
    meta_description = models.TextField(max_length=255, help_text="Content for description of meta tag",null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title} --- {self.request_type}'
    
class CodeSnippets(models.Model):
    api = models.ForeignKey(EndPoints,on_delete=models.CASCADE)
    title = models.CharField(max_length=255,null=True,blank=True)
    language = models.CharField(max_length=255,null=True)
    code = models.TextField(null=True)
    is_active = models.BooleanField(default=True)
    is_free = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ['api', 'language']

    def __str__(self):
        return f'{self.api.title} --- {self.language}'
