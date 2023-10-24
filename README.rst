pyment
======

Create, update or convert docstrings in existing Python files, managing several styles.

**Discalimer**: This is a non-official fork of the original project. Main changes are:

- Output style by default is numpydoc instead of reST

- The empty sections in original docstring (including parameters) are ignored by default. To enable them, use `-e` flag (note that the behavior of this flag in the original project is the opposite)

- Most sentences are now ended with a dot and start with a capital letter

- Default arguments are automatically specified in the docstring using the `By default, ` syntax and `, optional` is added next to the type of optional arguments.

- Indentation of indented doctests lines are preserved.

- More sections titles are supported (like Note, Example, ...)

See `output_numpy.py <output_numpy.py>`_ and `output_google.py <output_google.py>`_
for an example of the results from `example.py <example.py>`_.

.. contents:: :local:

Project Status
--------------

**Test Status**

Linux: |travis|

Windows: |appveyor|


.. |travis| image:: https://travis-ci.org/dadadel/pyment.svg?branch=master
    :target: https://travis-ci.org/dadadel/pyment.svg?branch=master
    :alt: Linux tests (TravisCI)

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/f9d4jps5fkf4m42h?svg=true
    :target: https://ci.appveyor.com/api/projects/status/f9d4jps5fkf4m42h?svg=true
    :alt: Windows tests (Appveyor)

|

**Supported Versions**

.. image:: https://img.shields.io/badge/python-3.6-blue.svg
    :target: https://img.shields.io/badge/python-3.6-blue.svg
    :alt: Supports Python36
.. image:: https://img.shields.io/badge/python-3.7-blue.svg
    :target: https://img.shields.io/badge/python-3.7-blue.svg
    :alt: Supports Python37
.. image:: https://img.shields.io/badge/python-3.8-blue.svg
    :target: https://img.shields.io/badge/python-3.8-blue.svg
    :alt: Supports Python38
.. image:: https://img.shields.io/badge/python-3.9-blue.svg
    :target: https://img.shields.io/badge/python-3.9-blue.svg
    :alt: Supports Python39

|

**Code Coverage**

.. image:: https://coveralls.io/repos/github/wagnerpeer/pyment/badge.svg?branch=enhancement%2Fcoveralls
    :target: https://coveralls.io/github/wagnerpeer/pyment?branch=enhancement%2Fcoveralls
    :alt: Test coverage (Coveralls)


Description
-----------

This Python3 program intends to help Python programmers to enhance inside code documentation using docstrings.
It is useful for code not well documented, or code without docstrings, or some not yet or partially documented code, or a mix of all of this :-)
It can be helpful also to harmonize or change a project docstring style format.

It will parse one or several python scripts and retrieve existing docstrings.
Then, for all found functions/methods/classes, it will generate formatted docstrings with parameters, default values,...

At the end, patches can be generated for each file. Then, man can apply the patches to the initial scripts.
It is also possible to update the files directly without generating patches, or to output on *stdout*.
It is also possible to generate the python file with the new docstrings, or to retrieve only the docstrings...

Currently, the managed styles in input/output are javadoc, one variant of reST (re-Structured Text, used by Sphinx), numpydoc, google docstrings, groups (other grouped style).

You can also configure some settings via the command line or a configuration
file.

To get further information please refer to the `documentation <https://github.com/dadadel/pyment/blob/master/doc/sphinx/source/pyment.rst>`_.

The tool, at the time, offer to generate patches or get a list of the new docstrings (created or converted).

You can contact the developer *dadel* by opening a `discussion <https://github.com/dadadel/pyment/discussions/new>`_.

Start quickly
-------------

**Note**: you are going to install and use a non-official fork of Pyment.

- install this fork from sources:

.. code-block:: sh

        $ pip install git+https://github.com/valentingol/pyment
        or
        $ git clone https://github.com/valentingol/pyment.git
        $ cd pyment
        $ python setup.py install

- run from the command line:

.. code-block:: sh

        $ pyment myfile.py    # will generate a patch
        $ pyment -w myfile.py  # will overwrite the file

or

.. code-block:: sh

        $ pyment my/folder/ # patches are generated at root
        $ pyment -w my/folder/ # files are overwritten in place

- get help:

.. code-block:: sh

        $ pyment -h

- run from a script:

.. code-block:: python

        import os
        from pyment import PyComment

        filename = 'test.py'

        c = PyComment(filename)
        c.proceed()
        c.diff_to_file(os.path.basename(filename) + ".patch")
        for s in c.get_output_docs():
            print(s)

Example
-------

Here is a full example using Pyment to generate a patch and then apply the patch.

Let's consider a file *test.py* with following content:

.. code-block:: python

        def addnum_rest(a: int, b: int = 0) -> int:
            """add numbers

            :param a: First number.
            :type a: int
            :param b: Second number. Defaults = 0.
            :type b: int
            :returns: The output sum
            """
            return a + b

Now let's use Pyment:

.. code-block:: sh

        $ pyment test.py

Using Pyment without any argument will autodetect the docstrings formats and generate a patch using the NumpyDoc format.
So the previous command has generated the file *test.py.patch* with following content:

.. code-block:: patch

        # Patch generated by Pyment v0.4.0

        --- a/test.py
        +++ b/test.py
        @@ -1,10 +1,16 @@
         def addnum_rest(a: int, b: int = 0) -> int:
        -    """add numbers
        +    """Add numbers.

        -    :param a: First number.
        -    :type a: int
        -    :param b: Second number. Defaults = 0.
        -    :type b: int
        -    :returns: The output sum
        +    Parameters
        +    ----------
        +    a : int
        +        First number.
        +    b : int, optional
        +        Second number. By default, 0.
        +
        +    Returns
        +    -------
        +    int
        +        The output sum.
            """
            return a + b

Let's finally apply the patch with the following command:

.. code-block:: sh

        $ patch -p1 < test.py.patch

Now the original *test.py* was updated and its content is now:

.. code-block:: python

        def addnum_rest(a: int, b: int = 0) -> int:
            """Add numbers.

            Parameters
            ----------
            a : int
                First number.
            b : int, optional
                Second number. By default, 0.

            Returns
            -------
            int
                The output sum.
            """
            return a + b


For a more complete example using nympydoc or googledoc, see `output_numpy.py <output_numpy.py>`_
and `output_google.py <output_google.py>`_ from `example.py <example.py>`_.