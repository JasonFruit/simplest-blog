title: The ABCenatrix
date: November 21, 2017
publish: yes
<!-- Post Markdown begins here -->
The ABCenatrix
======================================================================

The ABCenatrix is a viewer, manager, and editor for tunebooks in
[ABC musical notation](http://abcnotation.com).

Why not use an existing program?
----------------------------------------------------------------------

I wrote the ABCenatrix because there were few simple, usable tools to
handle ABC tunebooks available for Linux.  EasyABC, one of the best,
has not been maintained in some time, and I was unable to make it work
fully.  Besides, its layout mixes functions for editing and viewing
tunes, making it ideal for neither.  Most of the others handle ABC
only as a sideline, or else have disappeared completely or succumbed
to bitrot.

Capabilities:
----------------------------------------------------------------------

 - Opens, creates, manages, and saves tunebooks
 - Displays, prints, transposes, and plays tunes
 - Edits tunes with live preview

Requirements:
----------------------------------------------------------------------

 - Python 2.7 or 3.x with PySide, pygame, and mido
 - abcm2ps and abc2midi
 - Linux (The ABCenatrix mostly works on Windows, too, but it's not
   polished or stable yet, and installation involves a lot of
   _download, unpack, install, repeat_.  It's untested on OS X, but
   should work without modification.)
   
Screenshots:
----------------------------------------------------------------------

Here are a few pictures of the ABCenatrix in action:

### Viewing a tunebook
<a href="viewing-tunebook.png" target="_blank"><img src="viewing-tunebook-thumb.png" alt="Viewing tunebook" /></a>

### Creating a filter
<a href="creating-filter.png" target="_blank"><img src="creating-filter-thumb.png" alt="Creating a filter" /></a>

### Editing a tune
<a href="editing.png" target="_blank"><img src="editing-thumb.png" alt="Editing a tune" /></a>

 
Installation:
----------------------------------------------------------------------

### Linux

I've given the commands for Debian-based distributions, e.g. Ubuntu
and derivatives, Linux Mint, etc.  Other distributions offer similar
packages through their package managers.

#### 1. Install python and other dependencies

This is probably done for you already by your distribution, but it
might be best to use Python 3, which some distributions don't have by
default.  You'll also need PySide, which provides the
GUI[<sup>1</sup>](#fn1).  Then, the ABCenatrix uses `abcm2ps` and
`abcmidi` behind the scenes, as they represent years of refinement and
are as up-to-date as any ABC tooling.  Finally, you'll need pip, which
you will use to install the last couple dependencies.  As root, do:

    apt-get install python3 python3-pyside abcm2ps abcmidi python3-pip
	
#### 2. Install dependencies not available from package manager

The ABCenatrix uses PyGame and Mido to play and read MIDI output, but
you can't get them from the package manager, probably.  Instead,
become root and issue:

    pip3 install pygame mido

#### 3. Finally, install the ABCenatrix

Download the [latest release](abcenatrix.tgz).  As a normal user,
issue:

`tar` `-xvf` _`path/to/abcenatrix.tgz`_

(Obviously, you will need to use the path to your downloaded file, not
the bogus one above.)
	
Change directory into the directory created by that command (usually
`cd abcenatrix`).  Then become root and issue:

    python3 setup.py install
	
If all goes according to plan, the ABCenatrix will be installed.

#### Running

You can run it by issuing `abcenatrix` from the command line or by a
menu entry that should be created for you.

----------------------------------------------------------------------

### Footnotes

<a name="fn1" id="fn1"><sup>1</sup>  </a> Despite what it says on their website,
don't try to install PySide using pip; I've never gotten it to work.
Not even once.
