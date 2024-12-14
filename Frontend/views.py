from django.shortcuts import render, redirect, get_object_or_404
from Songs.models import song_list, song_files
from django.db.models.functions import Lower
from django.core.exceptions import PermissionDenied
from django.http import Http404


def request_perm(request, groups):
    for group in groups:
        if request.user.groups.filter(name=group).exists():
            return True

    return False


# def all_groups(request):
#     for group in ['Admin', 'Bestuur', 'Dirigent']:
#         if request.user.groups.filter(name=group).exists():
#             return True

#     return False



def repetoireview(request):

    # Permission groups
    settings_perm = request_perm(request, ['Admin', 'Bestuur', 'Dirigent'])
    media_perm = request_perm(request, [''])

    # get dictionary's from the database in order to fill out the webpage
    active = song_list.objects.filter(page_topic='active').order_by(Lower('song_name'))
    inactive = song_list.objects.filter(page_topic='inactive').order_by(Lower('song_name'))
    folders = song_list.objects.filter(page_topic='folder').order_by(Lower('song_name'))
    
    # Template data dictionary
    data = {
        'page': 'repetoire.html',
        'active': active,
        'inactive': inactive,
        'folders': folders,
        'settings_perm': settings_perm,
        'media_perm': media_perm,
    }

    return render(request, 'index.html', data)


def songview(request, url_song_name):

    # Get all songs registered in a list
    all_songs = []
    for song in song_list.objects.all():
        all_songs.append(song.song_name)

    # Return 403 if requested song not in database
    if url_song_name not in all_songs:
        raise Http404()
    
    # Redirect user to archive if song not active
    song_item = get_object_or_404(song_list, song_name=url_song_name)
    if song_item.page_topic == 'archive':
        return redirect('/songs/archive')

    # Permission groups
    settings_perm = request_perm(request, ['Admin', 'Bestuur', 'Dirigent'])
    media_perm = request_perm(request, [''])

    # Create a list with all song files
    files_list = []
    for item in song_files.objects.all():
        if item.song_name == url_song_name:
            files_list.append(item)

    file_names_clean = []
    for item in song_files.objects.all():
        if item.song_name == url_song_name:
            file_names_clean.append(str(item.song_file).split('/')[-1].split('.')[0].replace('_', ' '))
    
    file_names = []
    for item in song_files.objects.all():
        if item.song_name == url_song_name:
            file_names.append(str(item.song_file).split('/')[-1].replace('_', ' '))

    data = {
        'page': 'render-song.html',
        'settings_perm': settings_perm,
        'media_perm': media_perm,
        'main_sheets': zip(files_list, file_names_clean),
        'main_choreos': zip(files_list, file_names_clean),
        'main_audios': zip(files_list, file_names_clean),
        'midi_files': zip(files_list, file_names),
        'all_files': zip(files_list, file_names),
    }

    return render(request, 'index.html', data)


def gastview(request):
    guest_activated = []
    for item in song_list.objects.all():
        if item.guest_active:
            guest_activated.append(item.song_name)

    if len(guest_activated) < 1:
        all_guest_items = None
    else:
        all_guest_items = []
        for song in song_files.objects.all():
            if song.item_type == 'main_sheet' and song.song_name in guest_activated:
                all_guest_items.append(song.song_name)


    data = {
        'items': all_guest_items,
    }

    return render(request, 'gast.html', data) 