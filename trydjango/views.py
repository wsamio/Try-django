from django.http import HttpResponse


def home_view(request):

    name = "Galia"
    HTML_STRING = f"""
    <h1>Hello {name}</h1>
    """
    return HttpResponse(HTML_STRING)