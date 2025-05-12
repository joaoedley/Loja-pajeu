from .models import SiteConfig

def site_logo(request):
    config = SiteConfig.objects.first()
    return {
        'site_logo': config.logo.url if config and config.logo else None
    } 