from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from Mail import sendmail
from Backend.models import member_invites
from django.template import Context
from django.template.loader import get_template
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model


# users page
def users(request):
    user = get_user_model()
    users = user.objects.all()

    super_users = []
    site_users = []

    for user in users:
        if user.is_superuser:
            super_users.append(user)

    for user in users:
        if not user.is_superuser:
            site_users.append(user)
    
    pending_list = []
    email_list = []
    invites = member_invites.objects.all()

    for user in site_users:
        email = user.email

        for member in invites:
            email_list.append(member.email)

        if email in email_list:
            pending_list.append(True)
        else:
            pending_list.append(False)
    
    data = {
        'page': 'settings/Users/users.html',
        'superusers': super_users,
        'siteusers': zip(site_users, pending_list),
    }

    return render(request, 'settings/index.html', data)


def create_user(request):
    data = {
        'page': 'settings/Users/create-user.html',
        'notify': '',
    }

    if request.method == 'POST' and 'create-user' in request.POST:
        member_invite_db = member_invites()
        email = request.POST.get('email').lower()

        try:
            user = User.objects.get(username=email)

            data = {
                'page': 'settings/Users/create-user.html',
                'notify': 'User bestaat al',
                'notifycolor': 'red',
            }

            return render(request, 'settings/index.html', data)

        except User.DoesNotExist:
            user = User.objects.create_user(email, email, "HatikwaMediaManagement")
            user.save()

            try:
                member_invite_db.email = email
                member_invite_db.save()
            except:
                pass

            data = {
                'page': 'settings/Users/create-user.html',
                'notify': 'Uitnodiging is verstuurd!',
                'notifycolor': 'green',
            }

            sendmail.auth_mail(email, 'Uitnodiging deelname Hatikwa-Media', email)

    return render(request, 'settings/index.html', data)


def activate_user(request, mail):
    pending = []

    for person in member_invites.objects.all():
        pending.append(person.email)

    if mail in pending:
        data = {'error': ''}

        if request.method == "POST":
            first_name = request.POST.get('first-name')
            last_name = request.POST.get('last-name')
            pass1 = request.POST.get('pass')
            pass2 = request.POST.get('check')

            if pass1 == pass2:
                user = User.objects.get(username=mail)
                user.set_password(pass1)
                user.first_name = first_name
                user.last_name = last_name
                my_group = Group.objects.get(name='Lid')
                user.groups.add(my_group)
                user.save()

                member_invites.objects.get(email=mail).delete()
                
                return redirect('/login')

            elif pass1 != pass2:
                data = {'error': 'Wachtwoorden komen niet overeen'}
            
        return render(request, 'settings/Users/activate.html', data)
    else:
        raise PermissionDenied()


def reset_user(request, mail):
    try:
        selected_user = User.objects.get(email=mail)
    except:
        selected_user = User.objects.get(username=mail)

    data = {
        'page': 'settings/Users/reset-user.html',
        'email': mail,
        'selected_user': selected_user,
    }
    return render(request, 'settings/index.html', data)


def reset_user_confirmed(request, mail):
    form = member_invites()

    # Try and except for creating new user with reset password
    try:
        try:
            user = User.objects.get(email=mail)
        except:
            user = User.objects.get(username=mail)

        user.delete()
        user = User.objects.create_user(mail, mail, "HatikwaMediaManagement")
        user.save()

    except User.DoesNotExist:
        user = User.objects.create_user(mail, mail, "HatikwaMediaManagement")
        user.save()

        form.email = mail
        form.save()

    # Try and except for resetting the pending system
    try:
        member_invites.objects.get(mail=mail).delete()
        form.email = mail
        form.save()

    except:
        form.email = mail
        form.save()


    # Send password reset mail
    sendmail.reset_email(mail, 'Account & wachtwoord reset', mail)



def delete_user(request, mail):
    try:
        selected_user = User.objects.get(email=mail)
    except:
        selected_user = User.objects.get(username=mail)

    data = {
        'page': 'settings/Users/delete-user.html',
        'email': mail,
        'selected_user': selected_user,
    }
    return render(request, 'settings/index.html', data)


def delete_user_confirmed(request, mail):
    raise PermissionDenied()