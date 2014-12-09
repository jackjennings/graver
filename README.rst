======
Graver
======

Graver is an experimental implementation of the GLIF spec in Python.

Goals
=====

The primary and sole function of the this library should be: GLIF file data access, validation, and transformation between versions.

In addition, this library attempts to be:

* Low-level. Should be concerned primarily with data read and write with a minimum of functions or properties not written in the GLIF spec
* Naïve. Should be unaware of other libraries implementation
* Explicit and safe. No implicit updating should be done on read, and GLIFs converted to other versions should be initialized as copies so that they must explicitly overwrite the original when saved
* Maintainable. Implementations for additional versions should be easily added
* Tested. Conform to a test suite which corresponds to the GLIF spec
* Documented.

Example
=======

Implementation in progress. Should do something like this:

.. code-block:: python

  import graver

  with graver.open('path/to/f.glif') as glif:
    glif.format
    # => 1
    glif.name
    # => "f"
    glif.advance.width
    # => 268
    glid.advance.width = 300
    # => 300
    glif.outline.contours
    # => [<graver.contour.Contour>]
    glif.lib
    # => {}
    # etc.

  glif1 = graver.read('path/to/b.glif')
  glif2 = glif1.as_version(2)
  glif2.write('path/to/b.glif')
