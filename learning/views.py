from django.shortcuts import render
from django.http import HttpResponse
from learning.models import Bab, Materi, Soal
from learning.forms import BabForm


def index(request):

    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    context_dict = {'boldmessage': "I am bold font from the context"}

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.

    return render(request, 'learning/index.html', context_dict)

def bab_view(request):
    bab_list= Bab.objects.all()
    context_dict={"bab":bab_list}

    return render(request, 'learning/bab.html', context_dict)

def list_materi(request, bab_slug):
    bab = Bab.objects.get(slug=bab_slug)
    materi_list = Materi.objects.filter(bab=bab)
    context_dict={"materi":materi_list}

    return render(request, 'learning/materi.html', context_dict)

def tambah_bab(request):
    # A HTTP POST?
    if request.method == 'POST':
        form = BabForm(request.POST)

        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database.
            form.save(commit=True)

            # Now call the index() view.
            # The user will be shown the homepage.
            return index(request)
        else:
            # The supplied form contained errors - just print them to the terminal.
            print form.errors
    else:
        # If the request was not a POST, display the form to enter details.
        form = BabForm()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render(request, 'learning/tambah_bab.html', {'form': form})

def soal_view(request, materi_slug):
    materi = Materi.objects.get(slug=materi_slug)
    soal = Soal.objects.filter(materi=materi)

    context_dict={"soal":soal}

    return render(request, 'learning/soal.html', context_dict)


