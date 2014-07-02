from django.template import Context, loader
from datetime import datetime
from django.http import HttpResponse

def index(request):
    return HttpResponse('<html><body>Hello, World!</body></html>')

def about(request):
    return HttpResponse('''Here is the About Page. Neat? No.  It is not.
                        But whatever.  Anyways there isn't much to say.
                        Have a really nice day.
                        <a href="/">Home</a>''')

def better_hello(request):
    t = loader.get_template('betterhello.html')
    c = Context({'current_time': datetime.now(),})
    return HttpResponse(t.render(c))
