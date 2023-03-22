## How to Contribute

You'll need to [log into the website](https://ringtheory.herokuapp.com/accounts/login/) or 
[join GitHub](https://www.github.com/join/) to contribute.

### Open an Issue

The easiest way to suggest improvements is to [open an Issue](https://github.com/rschwiebert/dart_data/issues).
Here are a few tips to follow:

- Refer to entities in the site using the urls to their detail page where possible.  This conveys the id for the entities 
  that a developer will need to process your request.  Examples:
  - <https://localhost:8000/rings/ring/1/>
  - <https://localhost:8000/properties/property/1/>
  
  Referring to the type of entity and its id directly is OK too.  Ids are easy to mix up, so it wouldn't
  hurt to write out your propositions in human language, too.

- Include citations in peer-reviewed sources to support assertions when possible.  If none can be found, 
  a short proof may suffice.  If an assertion is unclear, reviewers may decide to defer adoption of the 
  submission until a reference can be found.

- Be mindful of scope when creating an issue. A large multipart issue that is not well-focused will 
  be more difficult to take longer to resolve.  
  You may want to submit separate issues to organize your requests better. Examples of good focus would be
  - for a single example, suggest one (or many) resolution to the example's properties
  - for a single property, suggest one (or many) examples and their statuses for the property
  - suggest a new theorem ("logic") that could be used to make deductions
    
After discussion of your suggestion, any contributor can make a Pull Request (see below) to implement your improvement. 

### Make a Pull Request

To add a pull request implementing any changes to the repository, [fork](https://help.github.com/articles/about-forks/)
this project to your own account, make whatever changes you'd like, then
[open up all pull request for review](https://help.github.com/articles/creating-a-pull-request-from-a-fork/).

Our reviewers will
- check correctness
- evaluate quality of supporting citations
- make suggestions for improvements or corrections
- ensure the sumbission's usage of terminology is consistent with the conventions being used
- (when necessary) run post-processing to maximize the deductions

Once the PR is approved, a developer can go about integrating it into the master branch.

### Submit a webform
This is the least flexible method, but if you really won't use git, then you can 
[log into the website](https://ringtheory.herokuapp.com/accounts/login/) and 
send a message via [the suggestion form](https://ringtheory.herokuapp.com/contribute/).

## References

Ideally, contributions should reference a peer-reviewed publication.  
Sometimes an online resource like the stacks project, mathoverflow or math.stackexchange post 
will also suffice.

Submitting bibtex for references is ideal.  
The [google scholar chrome extension](https://chrome.google.com/webstore/detail/google-scholar-button/ldipcbpaocekfooobnbcddclnhejkcpn?hl=en) 
can produce bibtex entries on demand, although occasionally it messes them up or has incorrect information.

## Mathematical Reviewers

These are our current mathematical reviewers. 

- Ryan Schwiebert, @rschwiebert

Please feel free to contact us with any questions.  If you are interested in becoming a reviewer, please make contact.

## Licensing

Data in this repository - including any merged user contributions - is licensed under
[CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/).
Please see [LICENSE.md](https://github.com/rschwiebert/dart_data/blob/master/LICENSE.md) for details.