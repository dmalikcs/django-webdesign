#webdesign

Webdesign is simple socail link & address available application


Detailed documentation is in the "docs" directory.

## Quick start


1. Add "**Webdesign**" to your INSTALLED_APPS setting like this::

    ```

      INSTALLED_APPS = (
          ...
          'webdesign',
      )

    ```
2. Include the polls URLconf in your project urls.py like this::

      url(r'^webdesign/', include('webdesign.urls')),

3. Run `python manage.py syncdb` to create the polls models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a poll (you will need the Admin app enabled).

5. Visit http://127.0.0.1:8000/webdesign/ to participate in the poll.


   ~~ mistaken ~~
