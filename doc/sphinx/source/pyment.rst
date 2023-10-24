Reference documentation
#######################

Pyment: the docstrings manager (creator/converter)

**Discalimer**: This is a non-official fork of the original project. Main changes are:
- Output style by default is numpydoc instead of reST
- The empty sections in original docstring (including parameters) are ignored by default
  To enable them, use `-e` flag (note that the behavior of this flag in the original
  project is the opposite)
- Most sentences are now ended with a dot and start with a capital letter
- Default arguments are automatically specified in the docstring using the `By default, `
  syntax and `, optional` is added next to the type of optional arguments.
- Indentation of indented doctests lines are preserved.
- More sections title are supported (like Note, Example, ...)

.. Contents::

Introduction
============

Pyment is a software allowing to create, update or convert several docstrings formats in existing Python files.
So it should help Python programmers to enhance inside code documentation using docstrings.

It should be useful for code not yet documented, not well documented, or partially documented and also to harmonize files using several docstring formats.

Pyment will then be helpful to harmonize or change a project docstring style format.

How does it work
----------------

Pyment will parse one python file or several (automatically exploring a folder and its sub-folder) and retrieve existing docstrings.
Then, for each found function/method/class, it will generate a formatted docstrings with parameters, default values,...

At the end, depending on options, original files will be overwritten or patches will be generated for each file, in which
case you just have to apply the patches.

What are the supported formats
------------------------------

Currently, the managed styles are javadoc, reST (re-Structured Text, used by Sphinx), numpydoc, google, other groups (like Google).


Customization
-------------

It is planed to provide a large customization properties. However, it is currently limited to some settings.

There are two ways to customize Pyment.

The first is using the command line options (`pyment --help`). The second is providing a configuration file as explained later in that document.


Using Pyment
============

Pyment runs using Python3.6+.

Pyment is usable as is on command line using pyment script. But it can also be used inside a Python program.

How to install
--------------

**Note:** you are going to install a non-official fork of Pyment. To get the original project,
please refer to `Pyment on Github <https://github.com/dadadel/pyment>`_.

- install from Pypi

.. code-block:: sh

        $ pip install pyment

- install from sources:

.. code-block:: sh

        $ pip install git+https://github.com/valentingol/pyment
        or
        $ git clone https://github.com/valentingol/pyment.git
        $ cd pyment
        $ python setup.py install

How to run
----------

- To run Pyment from the command line the easiest way is to provide a Python file or a folder:

.. code-block:: sh

    pyment example.py # will generate a patch
    pyment folder/to/python/progs
    pyment -w myfile.py  # will overwrite the file
    cat myfile.py | pyment -  # will proceed the content from stdin and create a patch written on stdout
    cat myfile.py | pyment -w -  # will proceed the content from stdin and write on stdout the converted content

- To get the available options, run:

.. code-block:: sh

    pyment -h

Will provide the output:

.. code-block:: sh

    usage: pyment [-h] [-i style] [-o style] [-q quotes] [-f status] [-t]
                  [-c config] [-d] [-p status] [-v] [-w]
                  path

    Generates patches after (re)writing docstrings.

    positional arguments:
      path                  python file or folder containing python files to
                            proceed (explore also sub-folders). Use "-" to read
                            from stdin and write to stdout

    optional arguments:
      -h, --help            show this help message and exit
      -i style, --input style
                            Input docstring style in ["javadoc", "reST",
                            "numpydoc", "google", "auto"] (default autodetected)
      -o style, --output style
                            Output docstring style in ["javadoc", "reST",
                            "numpydoc", "google"] (default "reST")
      -q quotes, --quotes quotes
                            Type of docstring delimiter quotes: ''' or """
                            (default """). Note that you may escape the characters
                            using \ like \'\'\', or surround it with the opposite
                            quotes like "'''"
      -f status, --first-line status
                            Does the comment starts on the first line after the
                            quotes (default "True")
      -t, --convert         Existing docstrings will be converted but won't create
                            missing ones
      -c config, --config-file config
                            Get a Pyment configuration from a file. Note that the
                            config values will overload the command line ones.
      -d, --init2class      If no docstring to class, then move the __init__ one
      -p status, --ignore-private status
                            Don't proceed the private methods/functions starting
                            with __ (two underscores) (default "True")
      -v, --version         show program's version number and exit
      -w, --write           Don't write patches. Overwrite files instead. If used
                            with path '-' won't overwrite but write to stdout the
                            new content instead of a patch.
      -e, --enable-empty    Write params, returns, or raises sections even if
                            they are empty.

- To run the unit-tests:

.. code-block:: sh

    python setup.py test

- To run from a Python program:

.. code-block:: python

    import os
    from pyment import PyComment

    filename = 'test.py'

    c = PyComment(filename)
    c.proceed()
    c.diff_to_file(os.path.basename(filename) + ".patch")
    for s in c.get_output_docs():
        print(s)

Note that a documentation will be provided later. Now you can use Python introspection like: *>>> help(PyComment)*


Configuration file
==================

You can provide a configuration file to manage some settings.

Note that if you use command line parameters that are also set in the
configuration file, then the command line ones will be ignored.

The configuration parameters that you can set are:

- **first_line**

    *True or False*

Set to **True** then for each docstring, the description should start on the first
line, just after the quotes. In the other case the description will start on the
second line.

- **quotes**

    *''' or """*

The quotes used for the docstring limits.

- **output_style**

    *javadoc, reST, numpydoc, google, groups*

The output format for the docstring.

- **input_style**

    *auto, javadoc, reST, numpydoc, google, groups*

The input format for the docstring interpretation. Set to **auto** if you want
Pyment to autodetect for each docstring its format.

- **init2class**

    *True or False*

Set to **True** to move the generated docstring for __init__ to the class docstring.
If there was already a docstring for the class, then the __init__ will conserve
its docstring and the class its own.

- **convert_only**

    *True or False*

Set to **True** if you want only to convert existing docstring.
So Pyment won't create missing docstrings.

- **indent**

    *Integer value (default is 2)*

Change the amount of spaces used for indented elements.

**Todo...**

- Add other command line options
- *optional/excluded sections*

Pyment will ignore some sections (like *raises*) or will generate some sections only if there was an existing corresponding section in input docstring.


Examples
========

A full example
--------------

Here is a full example using Pyment to generate a patch and then apply the patch.

Let's consider a file *test.py* with following content:

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

Contact/Contributing
====================

Please refer to the original project on Github: `Pyment on Github <https://github.com/dadadel/pyment>`_