from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.views.generic import ListView, DetailView

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect

from .models import Post
from .forms import SampleForm



class HomeView(ListView):
    model = Post
    template_name = 'home.html'

class ArticleView(DetailView):
    model = Post
    #if it's got a defined app, template use that. If not, fall back on the default article_details template
    #todo - check for app template filename resolution, fall back to article_details if not found and log an error
    template_name = 'article_details.html'

def index(request):
    posts = Post.objects.all()[:5]
    template = loader.get_template('index.html')
    context = {
        'posts': posts,
    }
    return HttpResponse(template.render(context, request))

@csrf_protect
def upload_file(request):
    if request.method == 'POST':
        form = SampleForm(request.POST,request.FILES)
        if form.is_valid():
            # file is saved
            f = form.save()
            return HttpResponseRedirect(f.attachment.url)
    else:
        form = SampleForm()
    return render(request, 'home.html', {'form': form})


# Create your views here.
