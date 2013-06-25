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
    # This is a script step that actually executes the python code that
    # contains the selenium tests.
    - script:
        name: Test with selenium
        code: python test_google.py
```

### Running the selenium tests in xvfb

The selenium tests spin up a new firefox process. This process must be executed
in a context that has a virtual display. To do so, just start a display before
the tests are executed.

``` python
if __name__ == '__main__':
    # Run the code this process inside a virtual framebuffer
    display = Display(visible=0, size=(800, 600))
    display.start()
    unittest.main(verbosity=2)
    display.stop()
```
