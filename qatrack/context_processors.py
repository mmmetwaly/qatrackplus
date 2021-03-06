from django.conf import settings
from django.contrib.sites.models import Site
from qatrack.qa.models import Frequency, TestListInstance


def site(request):
    site = Site.objects.get_current()
    root = getattr(settings, "FORCE_SCRIPT_NAME")

    return {
        'SITE_NAME': site.name,
        'SITE_URL': site.domain,
        'QATRACK_ROOT': root if root else "",
        'VERSION': settings.VERSION,
        'BUG_REPORT_URL': settings.BUG_REPORT_URL,
        'FEATURE_REQUEST_URL': settings.FEATURE_REQUEST_URL,

        # forcing list cuts down number of queries on some pages
        'QA_FREQUENCIES': list(Frequency.objects.frequency_choices()),
        'UNREVIEWED': TestListInstance.objects.unreviewed().count(),
    }
