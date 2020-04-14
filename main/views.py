from django.shortcuts import render, HttpResponseRedirect, redirect
from .models import Book, EachLetter

# Create your views here.
def home(request):
    return render(request, 'main/0home.html')

def bookmain(request, id):
    key = Book.objects.get(pk=id)
    # letter = []
    # letter.append(EachLetter.objects.all(whichBook=key))
    letter = EachLetter.objects.filter(whichBook=key)

    return render(request, 'main/0bookmain.html', {'key':key, 'letter':letter})

def letter(request, title, id):
    BookId = Book.objects.get(title=title)  # 입력받은 title에 해당하는 책 가져옴
    thisBook = EachLetter.objects.filter(whichBook=BookId.pk)
    thisLetter = thisBook[id-1]
    
    return render(request, 'main/letter.html', {'thisLetter':thisLetter})