botw-tracker
============

The Legend of Zelda: Breath of the Wild<sup>TM</sup> Progress Tracker

Author: Evan Moritz

Description
-----------

This Django-based web application is a simple progress tracker for various aspects of the video game
The Legend of Zelda: Breath of the Wild<sup>TM</sup>.

License
-------

Copyright (c) 2017, Evan Moritz.

botw-tracker is an open source software project released under the MIT License.  
See the accompanying LICENSE file for terms.

Installation
------------

  1. Make sure the following software is installed on the target machine:

    - Python 3
    - Django
    - (optional) sqlite3

  2. Download the project from GitHub.

  3. (optional) Create a database instance of your choice and update database settings in `src/botwtracker/settings.py`.

     By default, the project will use a `sqlite3` instance in `data/sqlite3.db`.

  4. After cloning the project, run the configuration command:

        $ cd src
        $ python configure.py

     The configuration script will generate localized settings, prompting when necessary.

  5. (optional) Run the server locally for testing:

        $ python manage.py runserver

  6. Deploy application on development server

     Django applications can be deployed on any server with Python/WSGI support.

References
----------

  - Django is a registered trademark of the Django Software Foundation.
  - The Legend of Zelda: Breath of the Wild<sup>TM</sup> is copyright (c) 2017, Nintendo.
  - The Legend of Zelda, Wii U, and Nintendo Switch are trademarks of Nintendo.
  - Python and PyCon are trademarks or registered trademarks of the Python Software Foundation.
