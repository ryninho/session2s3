# TODO

* put it on PyPI (FIX IT)
* don't upload pickle files
* delete the pickle files? (maybe make that an option)
* Make a script for recovering the file
  * do we need `awscli`?
  * on the other hand we don't know what the file is called- could take the latest automatically
* add note to README- might need to import the same libraries used by the script before loading the session
* how to use this with imports and picklings that happen within a function?
  * another tool for collecting pickles in all subdirectories? (might collect too much)
  * or something that goes inside of functions? or need to have functions return all the objects? (big process change)
* use isinstance to remove modules before saving (and have that be the default)
