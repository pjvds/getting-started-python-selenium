Getting started python selenium
===============================

Simple pyhton project that contains a selenium test that gets executed on wercker.


## Wercker.yml

Here is the [wercker.yml](http://devcenter.wercker.com/articles/werckeryml/) for a python
project that has selenium tests.

``` yaml
# Makes the build and deployment pipeline run the python box
box: wercker/python
# Here is the start of the build pipeline
build:
  # The build pipeline consists of steps
  steps:
    # This is a script step that executes the code in the `code` option.
    # The | (pipe) character is YAML's way to start a multiline string.
    - script:
        name: Install selenium
        code: |
          sudo pip install selenium
          sudo pip install pyvirtualdisplay
    - script:
        name: Start Firefox in virtual frame buffer
        code: xvfb-run firefox
    # This is a script step that actually executes the python code that
    # contains the selenium tests.
    - script:
        name: Test with selenium
        code: python test_google.py
```
