# Plan of Project Twinkle


# Twinkle

## What is this?

A small paper/book reading (sharing) system, in which we could comment conveniently on each paper/book, even on some specific points, with some user-friendly technique support, such as @-user-support, math-support, paper-title-link-support, etc.

Besides, we also offer a feeds module to show what your friends are foucusing on, where you could easily make a discussion directly.

## How to implement?

Boostrap + Python + Flask + MongoDB

## Usage

### Database
1. Install MongoDB (add its 'bin' path to \$PATH\$ enviroment variable)
2. Create a folder for storing your database

### Python Package
1. ``pip install flask``
2. ``pip install PyMongo``
3. ``pip install Flask-PyMongo``

### Run
1. Run the database at the default port (replace 'YourDBPath' with your database path)
``mongod --dbpath YourDBPath``
2. run command ``python run.py`` at the root folder

## Modules

### Login Module

- [x] 1. Login, Logout
- [x] 2. Database
- [ ] 3. Register 
- [ ] 4. Secure Login (Flask-WTF)

### Upload Module

- [ ] 1. Upload function & UI
- [ ] 2. Database (MongoDB save & load)
- [ ] 3. Matching text real-time when typing name/author/etc.

### Comments Module

- [ ] 1. pdf.js(?) -- To be determined
- [ ] 2. the way of the Collection and Orgnization of all the comments (Database)
- [ ] 3. Some additive features, such as @-support, title-link-support, math-support, etc.

### Feeds Module
 
- [ ] 1. Feeds (UI & Database of action recording)
- [ ] 2. Follow & Unfollow (UI & Database)

## Technique TODO

- [ ] Flask-WTF (Secure Login)
- [ ] MongoDB自设Key的方法，不用ObjectID
- [ ] TODO
