from django.conf import settings

def ecommdetails(request):
    context = {
        'site_name':settings.SITE_NAME,
    }
    return context