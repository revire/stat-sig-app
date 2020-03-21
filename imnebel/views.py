from django.shortcuts import render

# Create your views here.



from .models import Blog, Category
from django.shortcuts import render_to_response, get_object_or_404, render

from django.views.generic import TemplateView


def index(request):
   context = {'categories':Category.objects.all(), 'posts': Blog.objects.all()[:5]}
   return render(request, 'imnebel/index.html', context)
#
# class IndexView(TemplateView):
#    template_name = 'polls/home.html'
#
#    def get(self, request):
#       words = list(Category.objects.all())[-5:]
#       words.reverse()
#       return render(request, self.template_name, {'words': words})

   # def post(self, request):
   #    form = NameForm(request.POST)
   #    words = list(Data.objects.all())[-5:]
   #    words.reverse()
   #    if form.is_valid():
   #       post = form.save(commit=False)
   #       post.save()
   #
   #       text = form.cleaned_data['post']
   #       l = len(text)
   #       form = NameForm()
   #
   #    context = {'form': form, 'text': text, 'len': l, 'words': words}
   #    return render(request, self.template_name, context)



def view_post(request, slug):
   context = {'post': get_object_or_404(Blog, slug=slug)}
   return render(request, 'imnebel/view_post.html', context)


def view_category(request, slug):
   category = get_object_or_404(Category, slug=slug)
   context = {'category': category, 'posts': Blog.objects.filter(category=category)[:5]}
   return render(request, 'imnebel/view_category.html', context)