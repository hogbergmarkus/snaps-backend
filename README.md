# Snaps - API

## Introduction

![Welcome message](documentation/images/welcome_message.png)

This is my RESTful API, developed for my frontend React project, Snaps.

It contains all the logic that allows users on the frontend to perform CRUD operations.

Snaps is a photo-sharing website that allows users to upload photos to share with others.

Any photos uploaded to the website is also free to download for other users, thereby creating a sharing community.

Users can sign up to take part in interactions such as, up- and downloading images, like, comment and save images to albums in their profile.

## Table of Contents

- [Introduction](#introduction)
- [Design](#design)
  - [Entity Relational Diagram](#entity-relational-diagram)
  - [API-endpoints](#api-endpoints)
- [Testing](#testing)
  - [Unit Tests](#unit-tests)
  - [Validation](#validation)
  - [Manual Testing](#manual-testing)
    - [root_route](#root_route)
    - [albums](#albums)
    - [comments](#comments)
    - [likes](#likes)
    - [posts](#posts)
    - [profiles](#profiles)
- [Deployment](#deployment)

## Design

### Entity Relational Diagram

As a part of my design process, I charted my models on a spreadsheet.

This project was based on the [Moments](https://github.com/Code-Institute-Solutions/moments/tree/304244f540308ff4dd3c961352f55a633a4b3bed) walkthrough project,
and it will therefore exist code that is the same or similar

However I have made my own customizations to fit the plan for my project.

The [backend](https://github.com/Code-Institute-Solutions/drf-api/tree/ed54af9450e64d71bc4ecf16af0c35d00829a106) is for this reason inevitably similar to the one in the Moments project but I will point out som key differences here that make it my own.

- **My Like model:**

Unlike the one for Moments, my model allow users to like both posts and comments.

Also, posts and comments can be liked individually, not dependent on eachother.

- **My Post model:**

Unlike the one for moments, my model utilizes [django-taggit](https://django-taggit.readthedocs.io/en/latest/) to let users add tags to this posts.

This adds a level of searchability that the Moments project lacks.

I am also going to allow users to download images, and then keep track of how many times

the image of a post has been downloaded which my model accommodates.

- **My Album model**

The Moments project does not carry this feature at all.

It will allow users to save posts to albums that they can create on their profile page.

The result can be seen here:

![Entity Relational Diagram](documentation/entity_relational_diagram/erd.png)

### API Endpoints

These are the endpoints used by my API:

![API-endpoints](documentation/images/api_endpoints.png)

## Testing

### Unit Tests

I have created some 50 automated tests for my views, all passing.

- Tests for my Album views can be found here: [Album view tests](https://github.com/hogbergmarkus/snaps-backend/blob/main/albums/tests.py)

- Tests for my Comment views can be found here: [Comments view tests](https://github.com/hogbergmarkus/snaps-backend/blob/main/comments/tests.py)

- Tests for my Like views can be found here: [Likes view tests](https://github.com/hogbergmarkus/snaps-backend/blob/main/likes/tests.py)

- Tests for my Post views can be found here: [Posts view tests](https://github.com/hogbergmarkus/snaps-backend/blob/main/posts/tests.py)

- Tests for my Profile views can be found here: [Profile view tests](https://github.com/hogbergmarkus/snaps-backend/blob/main/profiles/tests.py)

### Validation

All files I created/altered were run through the [PEP8 CI python linter](https://pep8ci.herokuapp.com/), with no errors or warnings to show.

### Manual Testing

Each title under "Works" was tested manually and marked with an X for yes if it works, and no if it does not.

#### root_route

|Works                                              |YES |NO |
|---------------------------------------------------|:---:|---|
|The root_route url loads                           |X  |   |
|Welcome message is displayed on landing page       |X  |   |

#### albums

|Works                                                   |YES |NO |
|--------------------------------------------------------|:---:|---|
|`albums/` is not accessible if not logged in            |X  |   |
|`albums/<int:pk>/` is not accessible if not logged in   |X  |   |
|`albums/` is accessible to user if logged in            |X  |   |
|`albums/<int:pk>/` is accessible to user if logged in   |X  |   |
|Logged in user can create an album and add posts to it  |X  |   |
|Logged in user can view their albums                    |X  |   |
|Logged in user can update an album                      |X  |   |
|Logged in user can delete an album                      |X  |   |

#### comments

|Works                                                                |YES |NO |
|---------------------------------------------------------------------|:---:|---|
|`comments/` is accessible if not logged in as read only              |X  |   |
|`comments/<int:pk>/` is accessible if not logged in as read only     |X  |   |
|Can read, but not create comments if not logged in                   |X  |   |
|If I am signed in, I can create a comment                            |X  |   |
|Comments can not be edited if not logged in                          |X  |   |
|Comments can not be deleted if not logged in                         |X  |   |
|Comments can be edited by its owner                                  |X  |   |
|Comments can be deleted by its owner                                 |X  |   |

#### likes

|Works                                                                |YES |NO |
|---------------------------------------------------------------------|:---:|---|
|`likes/` is accessible if not logged in as read only                 |X  |   |
|`likes/<int:pk>/` is accessible if not logged in as read only        |X  |   |
|I can see but not add likes if not logged in                         |X  |   |
|If I am signed in, I can add a like to a post                        |X  |   |
|If I am signed in, I can add a like to a comment                     |X  |   |
|Likes can not be deleted if not logged in as the owner               |X  |   |
|Likes can be deleted if logged in as its owner                       |X  |   |
|I can not like the same thing twice                                  |X  |   |

#### posts

|Works                                                                    |YES |NO |
|-------------------------------------------------------------------------|:---:|---|
|`posts/` is accessible if not logged in as read only                     |X  |   |
|`posts/<int:pk>/` is accessible if not logged in as read only            |X  |   |
|`posts/<int:pk>/download/` is not accessible if not logged in            |X  |   |
|I can see but not add posts if not logged in                             |X  |   |
|If I am signed in, I can add a post                                      |X  |   |
|Posts can not be edited if not logged in as the owner                    |X  |   |
|Posts can not be deleted if not logged in as its owner                   |X  |   |
|Posts can be edited by its owner                                         |X  |   |
|Posts can be deleted by its owner                                        |X  |   |
|I can increment download count by posting to `posts/<int:pk>/download/`  |X  |   |
|comments_count increments by one when I add a comment to a post          |X  |   |
|likes_count increments by one when I add a like to a post                |X  |   |
|I can upload an image to a post                                          |X  |   |

#### profiles

|Works                                                                |YES |NO |
|---------------------------------------------------------------------|:---:|---|
|`profiles/` is accessible if not logged in as read only              |X  |   |
|`profiles/<int:pk>/` is accessible if not logged in as read only     |X  |   |
|`profiles/<int:pk>/` is accessible if not logged in as read only     |X  |   |
|Upon registering, a new profile is created for the user              |X  |   |
|As the owner of a profile, I can update it                           |X  |   |
|I can add a profile image                                            |X  |   |
|If I don't own the profile, I can only view it                       |X  |   |

## Deployment

I started by setting up a database at [Elephant SQL](https://www.elephantsql.com/).

On [Heroku](https://www.heroku.com/) I created my app, then on the settings page for the app, I added the following config vars:

- DATABASE_URL with the value of my postgreSQL server url.
- SECRET_KEY with a value I got from [Djecrety](https://djecrety.ir/).
- DISABLE_COLLECTSTATIC with the value of 1.
- CLOUDINARY_URL with a value of my cloudinary API environment variable.

Back in my IDE, I installed dj_database_url and psycopg2, using the command:

- pip3 install dj_database_url==0.5.0 psycopg2

Then import dj_database_url into the setting.py file.

In settings.py I updated the Database section to use my local db.sqlite3 server when I'm in development,

and to use my postgreSQL server when in production.

This is the code snipped to achieve that:

```
if 'DEV' in os.environ:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
else:
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
    }
```

I then added ```os.environ['DATABASE_URL'] = 'my-ElephantSQL-database-url'``` to my env.py file.

In my env.py file I also have ```os.environ['DEV'] = '1'```, to be able to set conditional logic in my settings.py,

so I can dynamically switch between development and production.

Temporarily comment out the DEV variable in the env.py file, to let the IDE connect
to the external database.

In settings.py add a print statement here:

```
else:
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
    }
    print(connected to external database)
```

In the terminal, run:

- python3 manage.py makemigrations --dry-run

You should see: "connected to external database" in the terminal.

Remove the print statement, and migrate the database:

- python3 manage.py migrate

Create a superuser:

- python3 manage.py createsuperuser

Head back over to [Elephant SQL](https://www.elephantsql.com/), and go to the database you just created.

On the left side navigation, click "Browser", then select "Table queries", and from the list, click "auth_user".
