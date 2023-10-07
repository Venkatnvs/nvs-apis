from django.conf import settings

def SiteDetails(request):
    context = {
        'site_name':settings.SITE_NAME,
    }
    return context