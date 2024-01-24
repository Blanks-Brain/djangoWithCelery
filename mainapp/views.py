from django.shortcuts import render
from .tasks import test_func
from django.http import HttpResponse
# Create your views here.
from sendMailApp.tasks import sent_mail_func
def test(request):
    test_func.delay()
    return HttpResponse("Done")

def send_mail_to_all(request):
    sent_mail_func.delay()
    return HttpResponse("Sent")