from django.shortcuts import render
import logging
logger = logging.getLogger(__name__)


def handler404(request, exception):
    ''' Custom 404 Error Page '''
    logger.warning(f'404 Error: {exception}')
    return render(request, "errors/404.html", status=404)


def handler500(request):
    ''' Custom 500 Error Page '''
    return render(request, "errors/500.html", status=500)
