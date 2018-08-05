pywin32-displaypilot
====================

.. image:: https://img.shields.io/pypi/v/pywin32-displaypilot.svg
    :target: https://pypi.python.org/pypi/pywin32-displaypilot
    :alt: Latest PyPI version

A python script sets monitor display orientation with PyWin32

Usage
-----
::

  pywin32-displaypilot [-h] [-d] [-l] [-s SCREEN] [orientation]

Examples:
^^^^^^^^^

1. List all connected monitors and their indexes::

    pywin32-displaypilot -l

2. Set primary monitor (primary monitor is the default target) to portrait mode (90 degree)::

    pywin32-displaypilot 90

  or (index of the primary monitor is guaranteed to be zero)::

    pywin32-displaypilot -s 0 90

3. Set the second monitor (index 1, use ``-l`` to consult all monitors' indexes) to landscape (0 degree)::

    pywin32-displaypilot -s 1 0

4. Enable debug output: use the ``-d`` option;

5. Read full help message::

    pywin32-displaypilot -h

Installation
------------

Requirements
^^^^^^^^^^^^

`PyWin32>=220 <https://sourceforge.net/projects/pywin32/>`_ is required.

Install with pip
^^^^^^^^^^^^^^^^

``pip install pywin32-displaypilot``

Install from source
^^^^^^^^^^^^^^^^^^^

::

    git clone https://github.com/genzj/pywin32-displaypilot.git
    python setup.py install


Compatibility
-------------

Windows 7, 8 and 10


Licence
-------

MIT


Authors
-------

`pywin32-displaypilot` was written by `genzj <zj0512@gmail.com>`_.
