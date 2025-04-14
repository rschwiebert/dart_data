# Admin developer guide (WORK IN PROGRESS)

## Preliminary setup

1. install `git`
1. checkout the RingApp repository and the dart_data repository
1. install python 3.10+, and arrange for a virtual environment for RingApp (this can be done in many ways)
1. pip install the requirements of RingApp into your venv (right now I'm using pipenv but I plan to change to poetry when possible.)
1. export environment variables as in the localenv.sh.example file in RingApp/dev
1. The website uses two databases, one postgres and one sqlite, 
   but you may be able to alter the settings to use sqlite for both.
   1. when using postgres you'd have to create a postgres user and database matching the connection string in the environment
1. (Using the virtualenv) run `python manage.py migrate` inside RingApp to set up the tables in the databases.
1. Set up a username with `python manage.py createsuperuser` 
1. Ensure that the `EXPORT_ROOT_DIR` environment variable has been set to point at the /db directory of your dart_data checkout
1. From RingApp, run `python manage.py db_to_data import --settings=ringapp.local_settings` to populate your local 
   sqlite database with the information stored in dart_data
1. To test if things are working, you might run `python manage.py runserver --settings=ringapp.local_settings` and 
   browsing to the frontend link it provides.  The default is usually <http://127.0.0.1:8000/> .
   The site should look like the real site (but it is just a local instance.)
1. Additions to the database can be made using the Django admin UI at <http://127.0.0.1:8000/admin>, using
   the superuser credentials you set up earlier.

## Review workflow

### Import and validate format
This step validates whether edited yaml files are parseable into the database.

1. Ensure you have a working setup.
1. Check out the submitted fork of dart_data next to your existing RingApp and dart_data repos.
You might name it dart_data_fork or something.
1. Re-set your EXPORT_ROOT_DIR to point at the db/ directory of the fork.
1. Run `python manage.py db_to_data import --settings=ringapp.local_settings`. An error will occur if there is 
some sort of problem.
   
### Review actual content
1. Review the contents, referring to the associated issue, for correctness. Update the pull request comments accordingly.
   
### Check consistency and completeness
1. The user may or may not have run the `process` routine before submitting the pull request.
You will need to run it to validate the logical consistency with the stored logic.
This can be done with a custom management command (`python manage.py process_ring id --settings=ringapp.local_settings)`
   or by using runserver and pressing the process button in the admin.
   
### Sanity check how it looks
1. If things are still going well at this point, you may want to runserver anyway and view what the new content looks 
like in the browser.
   
### Create patch, if necessary
It's quite possible that `process`ing their submission generated new content they need in their pull request.
We will need to pass that information back to them to update their request.  To do this:
1. run `python manage.py db_to_data export --settings=ringapp.local_settings` to write the database contents back to 
your checkout of their fork.
1. To create the patch, run `git diff --output usefulfilename.patch`.  You can review the differences in that file, and 
attach it to the pull request with instructions to `git apply` the patch to their branch and update their pull request.
   
### Finalize
If everything checks out, then an admin can integrate the fork into the main repo. 
They will need to make an additional step of updating the sqlite database in storage for use in the live website.