title: The ABCenatrix
date: November 21, 2017
publish: yes
<!-- Post Markdown begins here -->
The ABCenatrix
======================================================================

The ABCenatrix is a viewer, manager, and editor for tunebooks in
[ABC musical notation](http://abcnotation.com).

----------------------------------------------------------------------

(Jump straight to [Installation](#installation))

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
 - Linux, or, if you're adventurous, Windows
   
Screenshots:
----------------------------------------------------------------------

Here are a few pictures of the ABCenatrix in action:

### Viewing a tunebook
<a href="viewing-tunebook.png" target="_blank"><img src="viewing-tunebook-thumb.png" alt="Viewing tunebook" /></a>

### Creating a filter
<a href="creating-filter.png" target="_blank"><img src="creating-filter-thumb.png" alt="Creating a filter" /></a>

### Editing a tune
<a href="editing.png" target="_blank"><img src="editing-thumb.png" alt="Editing a tune" /></a>

 
<a id="installation" name="installation" />Installation:
----------------------------------------------------------------------

Jump to:

 - [Linux](#linux)
 - [Windows](#windows)
 
### <a id="linux" name="linux" />Linux

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

Download a tarball of the [latest release](abcenatrix.tgz).  As a
normal user, issue:

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

### <a id="windows" name="windows" />Windows

The ABCenatrix works on Windows, except for scaling the tune display.
(Give me a moment on that.)  I wouldn't call the process installation,
exactly, but here's how you acquire working prerequisites and get the
program running.  (I'm working on a clean installation on Windows, but
at least this way you can help shake out any bugs.)

#### 1. Install python

Install the latest release in the Python 2.7.x branch from
[the Python website](https://www.python.org/downloads/windows/); it's
2.7.14 at the time of writing.  When you get to what features will be
installed, tell it to add Python to your PATH.

#### 2. Install pip

Download the
[get-pip.py script](https://bootstrap.pypa.io/get-pip.py).  Open a
`cmd` window, `cd` to where you have it saved, and run it:

    python get-pip.py
	
#### 3. Install other dependencies

Once you have pip, use it to install the Python dependencies for the
ABCenatrix:

    pip install pyside pygame mido
	
#### 4. Get git

Download git (a source control tool) from
[here](https://git-scm.com/download/win).  Run the installer.

#### 5. Get the latest version of The ABCenatrix

Open a `cmd` window and issue:

    git clone https://github.com/JasonFruit/abcenatrix
	
Then, `cd` into the resulting `abcenatrix` directory, and issue:

    mkdir tools
	
Keep this `cmd` window open.
	
#### 6. Get abcm2ps and abcmidi

Download the .zip file of abctools for Windows from
[here](http://abcplus.sourceforge.net/#abctools); at the time of
writing, the version is abctools-win-20171121.zip.  Extract the zip
file to the `tools` directory you just created.

#### 7. Running

In the `cmd` window from step 5, type `python abcenatrix`.  It should
start up and run normally.  Please report bugs at
[the ABCenatrix's Github page](https://github.com/JasonFruit/abcenatrix)
so I can do better at supporting it on Windows.

Source
----------------------------------------------------------------------

The best way to get the source is to download a tarball of the
[latest release](abcenatrix.tgz).  It should always be fairly clean
and reasonably up-to-date.

The source code for the latest development version can be got from
[https://github.com/JasonFruit/abcenatrix](https://github.com/JasonFruit/abcenatrix).
I try not to commit code that's actually _broken_, but new features
may be in rudimentary form and not quite fit for public consumption;
please be cautious about using code newer than the release tarball
above.

----------------------------------------------------------------------

### Footnotes

<a name="fn1" id="fn1"><sup>1</sup> </a> Despite what it says on their
website, don't try to install PySide on Linux using pip; I've never
gotten it to work.  Not even once.
