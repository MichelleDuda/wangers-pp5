from django.shortcuts import render
import logging
logger = logging.getLogger(__name__)


def handler404(request, exception):
    logger.warning(f'404 Error: {exception}')
    return render(request, "errors/404.html", status=404)


def handler500(request):
    return render(request, "errors/500.html", status=500)
