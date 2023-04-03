from django.http import HttpResponse

HTML_STRING = """
<h1>Hello World</h1>
"""
def home_view(request):

    print(100 * 1000)
    return HttpResponse(HTML_STRING)