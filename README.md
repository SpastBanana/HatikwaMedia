## HatikwaMedia

---

### Content
This site is created to manage all sorts of media for the music choir Hatikwa. On this site, the members of the choire
will find their music sheets, midi songs, pre recorded videos of the rehearsal's, and more. The site is builded in 
Python with help of the Django framework to provide a secure way for publishing all sorts of media in a secure way. This
way the members of Hatikwa can all securely access their media.

---

### Checklist
_
**Main site functions**
- [x] View music sheets, midi's, video's and more (media)
- [ ] Upload music "media"
- [ ] Edit music "media"
- [ ] Delete music "media"
- [x] Admin can create user's with email function
- [x] Admin can reset user's password with email function
- [ ] Admin can change user's email
- [ ] See all users and manage them from one page
- [x] User role system
- [ ] Admin can manage user's role
- [x] Guests can view songfiles for song that is guest activated


_
**Bugs fixed**
- [x] Guest can view every song they enter in the url
- [x] Create user checks if the e-mail address is allready a outgoing_invite
- [x] Username needs to be not case sensitive
- [x] Songfiles are listed in upload order, needs to be alphabetic
- [ ] Songname is everywhere in the file names, needs to be only what type of file it is
- [ ] If song opened, order of head files needs to be "Bladmuziek, Audio opname, Choreo"


_
**High priority**
- [x] Entire site needs to be locked down and more hacker proof for non_authenticated_users
- [x] E-mail system uses raw password, this and other authentication types need to be more secure


_
**Extra's / todo**
- [x] Uploading all songs for main launch
- [ ] Correct the names of files in the frontend (for example remove ".mp3" and make it a play button icon)
- [ ] Add search function to the song list
- [ ] Better styling
- [ ] More compatible with phone
- [ ] More compatible with pc
- [ ] Upload all archived songs from hatikwa.aikebah.net to this site
- [ ] User now get's same email of entering the site when password is reset, this needs to be a "password reset" email
- [x] User first and last name are saved upon registration.