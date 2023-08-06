from django.http import HttpResponse

def home(request):
   return HttpResponse("""
    <html>
      <head>
        <title>Bienvenue sur mon site</title>
      </head>
      <body>
        <h1>Bienvenue sur mon site !</h1>
        <p>Page d'accueil en construction.</p>
      </body>
    </html>
  """)