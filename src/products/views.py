from django.shortcuts import render
from django.conf import settings
from .models import Product
from .forms import ProductForm, ContactForm
import urllib.request
import json
# Create your views here.

# def form_valid(self, form):
#     # get the token submitted in the form
#     recaptcha_response = self.request.POST.get('g-recaptcha-response')
#     url = 'https://www.google.com/recaptcha/api/siteverify'
#     payload = {
#         'secret': settings.RECAPTCHA_SECRET_KEY,
#         'response': recaptcha_response
#     }
#     data = urllib.parse.urlencode(payload).encode()
#     req = urllib.request.Request(url, data=data)
#
#     # verify the token submitted with the form is valid
#     response = urllib.request.urlopen(req)
#     result = json.loads(response.read().decode())
#
#     # result will be a dict containing 'contact' and 'action'.
#     # it is important to verify both
#
#     if (not result['product_create_view']) or (not result['action'] == ''):  # make sure action matches the one from your template
#         messages.error(self.request, 'Invalid reCAPTCHA. Please try again.')
#         return super().form_invalid(form)



def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()



    # context = {
    #     'form': form,
    #     'site_key': settings.RECAPTCHA_SITE_KEY,
    #     'secret_key': settings.RECAPTCHA_SECRET_KEY,
    # }
    #
    # recaptcha_response = request.POST.get('g-recaptcha-response')
    #
    # url = 'https://www.google.com/recaptcha/api/siteverify'
    # payload = {
    #     'secret': settings.RECAPTCHA_SECRET_KEY,
    #     'response': recaptcha_response
    # }
    # data = urllib.parse.urlencode(payload).encode()
    # req = urllib.request.Request(url, data=data)
    #
    # # verify the token submitted with the form is valid
    # response = urllib.request.urlopen(req)
    # print(response)
    #
    # result = json.loads(response.read().decode())
    # print(result)


def product_detail_view(request):
    obj = Product.objects.get(id=1)
    # context = {
    #     'title': obj.title,
    #     'description': obj.description,
    # }
    context = {
        'object': obj,
    }
    return render(request, "products/product_detail.html", context)

# def form_valid(self, form):
#     # get the token submitted in the form
#     recaptcha_response = self.request.POST.get('g-recaptcha-response')
#     url = 'https://www.google.com/recaptcha/api/siteverify'
#     payload = {
#         'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
#         'response': recaptcha_response
#     }
#     data = urllib.parse.urlencode(payload).encode()
#     req = urllib.request.Request(url, data=data)
#
#     # verify the token submitted with the form is valid
#     response = urllib.request.urlopen(req)
#     result = json.loads(response.read().decode())
#
#     # result will be a dict containing 'contact' and 'action'.
#     # it is important to verify both
#
#     if (not result['contact']) or (not result['action'] == ''):  # make sure action matches the one from your template
#         messages.error(self.request, 'Invalid reCAPTCHA. Please try again.')
#         return super().form_invalid(form)

# def form_valid(self, form):
#     # get the token submitted in the form
#     recaptcha_response = self.request.POST.get('g-recaptcha-response')
#     url = 'https://www.google.com/recaptcha/api/siteverify'
#     payload = {
#         'secret': settings.RECAPTCHA_SECRET_KEY,
#         'response': recaptcha_response
#     }
#     data = urllib.parse.urlencode(payload).encode()
#     req = urllib.request.Request(url, data=data)
#
#     # verify the token submitted with the form is valid
#     response = urllib.request.urlopen(req)
#     result = json.loads(response.read().decode())
#
#     # result will be a dict containing 'contact' and 'action'.
#     # it is important to verify both
#
#     if (not result['contact']) or (not result['action'] == ''):  # make sure action matches the one from your template
#         messages.error(self.request, 'Invalid reCAPTCHA. Please try again.')
#         return super().form_invalid(form)


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Website Inquiry"
            body = {
            'first_name': form.cleaned_data['first_name'],
            'last_name': form.cleaned_data['last_name'],
            'email': form.cleaned_data['email_address'],
            'message': form.cleaned_data['message'],


            }
            message = "\n".join(body.values())
            print(message)
            # try:
            #     send_mail(subject, message, 'admin@example.com', ['admin@example.com'])
            # except BadHeaderError:
            #     return HttpResponse('Invalid Header found.')
            # return redirect("about.html")
    form= ContactForm()
    return render(request, "contact.html", {'form':form})
