import json
import re

from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from learning.models import Bab, Materi, Soal, Jawaban, UserProfileKey
from learning.forms import BabForm, UserForm, RegistrationForm
from django.template import RequestContext
from django.core.mail import send_mail
import hashlib, datetime, random
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


#Register user
def register_user(request):
    args = {}
    args.update(csrf(request))
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        args['form'] = form
        if form.is_valid():
            form.save()  # save user to database if form is valid

            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            salt = hashlib.sha1(str(random.random())).hexdigest()[:5]
            activation_key = hashlib.sha1(salt+email).hexdigest()
            key_expires = datetime.datetime.today() + datetime.timedelta(2)

            #Get user by username
            user=User.objects.get(username=username)

            # Create and save user profile
            new_profile = UserProfileKey(user=user, activation_key=activation_key,
                key_expires=key_expires)
            new_profile.save()
            host=request.META['HTTP_HOST']

            # Send email with activation key
            email_subject = 'Account confirmation'
            email_body = "Hey {}, terima kasih telah mendaftar. Untuk aktivasi akun Anda, harap klik link di bawah ini dalam waktu kurang dari \
            48jam http://{}/confirm/{}".format(username, host, activation_key)

            send_mail(email_subject, email_body, 'be-py@be-py.com',
                [email], fail_silently=False)

            return HttpResponseRedirect('/register_success')
    else:
        args['form'] = RegistrationForm()

    return render_to_response('user_profile/register.html', args, context_instance=RequestContext(request))


#Aktivasi akun baru
def register_confirm(request, activation_key):
    #check if user is already logged in and if he is redirect him to some other url, e.g. home
    if request.user.is_authenticated():
        HttpResponseRedirect('/learning/')

    # check if there is UserProfile which matches the activation key (if not then display 404)
    user_profile = get_object_or_404(UserProfileKey, activation_key=activation_key)

    #check if the activation key has expired, if it hase then render confirm_expired.html
    if user_profile.key_expires < timezone.now():
        return render_to_response('user_profile/confirm_expired.html')
    #if the key hasn't expired save user and set him as active and render some template to confirm activation
    user = user_profile.user
    user.is_active = True
    user.save()
    return render_to_response('user_profile/confirm.html')

#Halaman Sukses Buat Akun
def register_success(request):

    return render_to_response('user_profile/success.html')


#register
def register(request):

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Update our variable to tell the template registration was successful.
            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print user_form.errors, profile_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    # Render the template depending on the context.
    return render(request,
            'learning/register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered} )

#Halaman Log in
def user_login(request):

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
                # We use request.POST.get('<variable>') as opposed to request.POST['<variable>'],
                # because the request.POST.get('<variable>') returns None, if the value does not exist,
                # while the request.POST['<variable>'] will raise key error exception
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('/learning/')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Akun Be-Py yang Anda masukkan belum / tidak aktif")
        else:
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        if request.user.is_authenticated():
            return HttpResponseRedirect('/learning/')
        else:
            return render(request, 'learning/login.html', {})

#some_view
def some_view(request):
    if not request.user.is_authenticated():
        return HttpResponse("Anda sudah masuk")
    else:
        return HttpResponse("Ups, Anda harus masuk dahulu")

@login_required
def restricted(request):
    return HttpResponse("Setelah Anda masuk, Anda bisa melihat halaman ini!")


# Use the login_required() decorator to ensure only those logged in can access the view.
@login_required

#Log out
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/learning/')

#Halaman User (index)
def index(request):
    try:
        all_soal = Soal.objects.all().count()
        user = request.user
        jawaban_user = Jawaban.objects.filter(user=user, sudah_benar=True).count()
        progress = float(jawaban_user)/float(all_soal)*100
    except:
        progress = ''

    context_dict = {'progress': progress}

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.

    return render(request, 'learning/index.html', context_dict)

#Halaman Tentang
def about(request):
    context_dict = {'boldmessage': "I am bold font from the context"}
    return render(request, 'learning/about.html', context_dict)

#Halaman Bantuan
def bantuan(request):
    return render(request, 'learning/bantuan.html')

#Halaman Bab
@login_required(login_url='/accounts/login/')
def bab_view(request):
    bab_list= Bab.objects.all()
    context_dict={"bab":bab_list}

    return render(request, 'learning/bab.html', context_dict)

#Halaman Materi
@login_required(login_url='/accounts/login/')
def list_materi(request, bab_slug):
    bab = Bab.objects.get(slug=bab_slug)
    materi_list = Materi.objects.filter(bab=bab)
    context_dict={"materi":materi_list}

    return render(request, 'learning/materi.html', context_dict)


#Halaman Soal
@login_required(login_url='/accounts/login/')
def soal_view(request, materi_slug, bab_slug, soal_id):
    nav = Materi.objects.get(slug=materi_slug)
    soal = Soal.objects.get(id=soal_id)
    all_soal = Soal.objects.all()
    nomor_soal = list(all_soal.values_list('id', flat=True)).index(soal.id) + 1
    total_soal = all_soal.count()
    try:
        jawaban = Jawaban.objects.get(soal=soal, user=request.user)
	isi_console = jawaban.console_user
	if not isi_console:
		isi_console=""
    except:
        isi_console = soal.isi_console
    context_dict={"soal":soal, "nomor_soal":nomor_soal,"total_soal":total_soal, "nav":nav, "request":request, "isi_console":isi_console}

    return render(request, 'learning/soal.html', context_dict)

#Halaman Profil Saya
@login_required(login_url='/accounts/login/')
def user_dashboard(request):
    user = request.user
    try:
        all_soal = Soal.objects.all().count()
        user = request.user
        jawaban_user = Jawaban.objects.filter(user=user, sudah_benar=True).count()
        progress = float(jawaban_user)/float(all_soal)*100
    except:
        progress = ''

    context_dict={"user":user, "progress":progress}
    return render(request, 'learning/user.html', context_dict)

#ajax cek jawaban
def cek_jawaban(request):
	if request.method == 'POST':
		jawaban_text = request.POST.get('jawaban')
		console_user = request.POST.get('console_user')
		user_id = request.POST.get('user_id')
		soal_id = request.POST.get('soal_id')
		response_data = {}
		user = User.objects.get(id=int(user_id))
		soal = Soal.objects.get(id=int(soal_id))

		try:
			jawaban = Jawaban.objects.get(soal=soal, user=user)
			jawaban.jawaban= jawaban_text
		        jawaban.console_user = console_user
		except:
			jawaban = Jawaban.objects.create(soal=soal, user=user, jawaban=jawaban_text, console_user=console_user)

		jawaban.kali_jawab += 1

		kunci=soal.kunci_jawaban.replace(u'\r',u'')
   		kunci=u'{}\n'.format(kunci)
		if kunci == jawaban.jawaban :
			response_jawaban = "Jawaban Anda benar!"
			jawaban.sudah_benar = True
		else:
			response_jawaban = "Periksa kembali sintaks Anda. Jawaban Anda masih salah."
			jawaban.sudah_benar = False
		print jawaban.jawaban
		print soal.kunci_jawaban

		jawaban.save()
		response_data['response_jawaban'] = response_jawaban
		response_data['jawaban'] = jawaban.jawaban
		response_data['jawaban_html'] = jawaban_text
		response_data['kunci'] = soal.kunci_jawaban

		return HttpResponse(json.dumps(response_data),
							content_type="application/json")
	else:
		return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )
