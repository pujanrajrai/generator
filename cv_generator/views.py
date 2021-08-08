from django.shortcuts import render, HttpResponse
# Create your views here.
from docxtpl import DocxTemplate


def cv(request):
    doc = DocxTemplate("first.docx")
    context = {
        'first_name': "fdsaijofasdjoi",
        'middle_name': 'fdasijofasd',
        'last_name': 'fdas',
        'address': 'pepsicola',
        'phone_number': '9808282207',
        'linkedin_profile ': 'www.linkedin.com',

    }
    doc.render(context)
    doc.save("generated_doc.docx")
    return HttpResponse('cv')
