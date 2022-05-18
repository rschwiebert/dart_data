# Database of Ring Theory data repo

This package holds the data for the [Database of Ring Theory](https://ringtheory.herokuapp.com/).
The goal is to make contributing more accessible and more transparent, as well as to keep a long-term record of 
the database contents.

## Contents
`db`: human-readable serialization of the contents of the database.  The relevant files are in 
[.yaml format](https://en.wikipedia.org/wiki/YAML). Also, each ring may include an .html file for providing expanded 
details. These are not strictly speaking part of the database, but organised there for convenience of editors.

`dart_data/templates/dart_data`: furnishes Django templates when this package is installed as a Django app 
for the website. The .html files from the /db path wind up there during installation.


## Contributing

There are several ways to help contribute
1. (The old way) You can create an account on 
   [the main site](https://ringtheory.herokuapp.com/) and use the webform there to make a suggestion.
1. You can open a ticket on this repository explaining your suggestion (this requires you to create a github account.)
1. You can create a pull request with your changes for review (this requires a github account too.)  The changes can be 
made by hand, or else you can set up a local development environment with the DaRT Django app and use Django admin to 
   create and modify these objects.

If you choose either of the first two, a developer will need to do the third one for you during the review process.

In any case, your contribution will need to be reviewed for appropriateness, and then correctness before inclusion.  
Please bear in mind that not all suggestions will be accepted.

Once the pull request is integrated into this repository, a developer will need to take one more step to push the new
data to the website where it can be seen. Then your contribution will be live!


## TODO
1. Some sorta web tool to assist in filling .yaml templates?
1. dotfile path and contents