from django.shortcuts import render


def SwaggerView(request):
    return render(request, 'doc.html')