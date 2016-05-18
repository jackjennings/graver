======
Graver
======

Graver is an experimental implementation in Python of the GLIF spec (http://unifiedfontobject.org/versions/ufo3/glyphs/glif/).

Goals
=====

The primary and sole function of the this library should be: GLIF file data access, validation, and transformation between versions.

In addition, this library attempts to be:

* Low-level. Should be concerned primarily with data read and write with a minimum of functions or properties not written in the GLIF spec
* Naïve. Should be unaware of other libraries implementation
* Explicit and safe. No implicit updating should be done on read, and GLIFs converted to other versions should be initialized as copies so that they must explicitly overwrite the original when saved
* Maintainable. Implementations for additional versions should be easily added
* Tested. Conform to a test suite with 100% coverage of the GLIF spec
* Correct. Correspond directly to each version of GLIF spec
* Documented.

Maintainability and correctness are the primary priorities of the project. This library should be useful for creating a series of tests that can be run against other GLIF libraries to check correctness.

At this point, speed is a secondary concern to those listed above.

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
