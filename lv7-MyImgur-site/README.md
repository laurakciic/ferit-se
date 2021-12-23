# Lab 7

Notes:
- Django prefers classes for forms and then html for forms to be dinamically generated 
  - difference in comparison to other frameworks where forms are tipically manually written 
- in Django we can control forms really good from the code itself
  - which then allows validations which in Django are performed at the level of forms

Tutorial: 

- Enable user login/signup
  - [Django authentication views](https://docs.djangoproject.com/en/3.1/topics/auth/default/#django.contrib.auth.forms.AuthenticationForm)
- Configure signup/login forms to use bootstrap (make 'em pretty)
  - [Extending Django UserCreationForm](https://dev.to/yahaya_hk/usercreation-form-with-multiple-fields-in-django-ek9)
  - [Looping over form fields](https://docs.djangoproject.com/en/3.1/topics/forms/#looping-over-the-form-s-fields)
  - [What are Django Widget Tweaks and how to use them](https://simpleisbetterthancomplex.com/2015/12/04/package-of-the-week-django-widget-tweaks.html)
  - [How Django forms work internally and how to render them manually](https://simpleisbetterthancomplex.com/article/2017/08/19/how-to-render-django-form-manually.html)
- Create image submission using forms
  - [Creating forms from models](https://docs.djangoproject.com/en/3.1/topics/forms/modelforms/)
- Add pretty datetime picker for django
  - [Bootstrap django datetime picker](https://github.com/monim67/django-bootstrap-datepicker-plus)
    - [Bootstrap-datepicker-plus tutorial based on Django Polls app tutorial part 4](https://django-bootstrap-datepicker-plus.readthedocs.io/en/latest/Walkthrough.html)
    - [Stackoverflow link](https://stackoverflow.com/a/49065034/347891)
    - [Setup bootstrap-datepicker-plus](https://monim67.github.io/django-bootstrap-datepicker-plus/configure/)
- Configure Comment submission to use forms
- Prevent commenting for unauthorized users
- Set basic CRUD for images
- Make sure user can vote only once
  - Create a Vote model with FKs on Image and User
  - Create upvote and downvote
  - Create pretty UI for voting
- Connect comments to users
  - Remove author field in model and CommentForm
  - Add user foreign key relationship
  - When submitting the comment make sure the user field is set in the view



Resources: 

- [Classy Class-Based Views cheatsheet](https://ccbv.co.uk/)
- [Sign up view in django with bootstrap](https://stackoverflow.com/questions/39294499/sign-up-view-in-django-with-bootsrap)

Tasks: 
1. Make sure unauthorized users cannot vote
2. Add comment moderation:
  - Add `approved` boolean field on Comment
  - Logged in admin (check `if request.user.is_superuser`) can see all comments
    on the detail view
  - Logged in users can see only approved comments
  - Logged out users can see only approved comments
  - Logged in admin has a button `Approve` next to each unapproved comment
  - Clicking the `Approve` button sets the `approved` field in Comment model to
    True 
3. Add Image-User relationship
  - Foreign key to User in the Image model
  - Only logged in users can submit images
  - Image is tied to the user
  - User can edit or delete only images that belong to them
  - Admins can edit or delete all images
  - Add a `posted_by` text to all templates where the image is shown. This text
    shows the username of a user that posted a comment. 
4. Enable liking comments
  - Create a new model `Like` with FK on Comment and User, similar to `Vote`
  - Create view `like` with route `path('like_comment/<int:comment_id>', ...`  

    This machanic does not have dislike, calling like for the first time
    likes a comment, calling it for the second time removes a like, similar
    to removing an upvote
  - Add form with like button next to every comment
  - Only logged in users can like
5. Add user profile page
  - Now that both images and comments are tied to the user create a new view in
    `accounts` app with url `localhost:8000/accounts/<user_id>`
  - All visitors (both logged in and logged out) can see a user's profile
  - User profile should show a list of all images a user posted with scores
  - User profile should show a list of all comments user posted with a number
    of likes
  - Change `posted_by` texts from task 2 to a link to user's profile





