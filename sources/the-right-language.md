title: The Right Language
date: January 28, 2015
publish: yes
<!-- Post Markdown begins here -->

The Right Language
======================================================================

I admit it.  I have the personality of an _enthusiast_ in the sense it
was used by nineteenth-century writers, a person who believes he is
constantly discovering the next really big thing, like Toad from _The
Wind in the Willows_, who would be one day unable to discuss anything
but the free and easy life of the wanderer in his gypsy cart, and the
next so enamored of the speed of the automobile as to disregard his
own safety and that of others in its pursuit.  I am especially
susceptible to programming languages; I am always getting excited
about the newest programming language, even if it's
[new only to me](http://en.wikipedia.org/wiki/Ada_(programming_language)).
Right now, it's [Nim](http://nim-lang.org); yesterday, it was
[Clojure](http://clojure.org/).  It could be anything tomorrow.

The fascinating part, however, is what happens when I sit down to
actually _make_ something with the new most amazing programming
language of all time: I write about half of it, realize I could have
whipped it up in Python in a third the time already expended and
without
[reimplementing basic functionality that should be baked into any good language](http://www.schemers.org/Documents/Standards/R5RS/HTML/),
and then I go and do that instead.  It could be partly because I know
Python very well and have used it a lot; it could be because a new
language can't hope to match Python's
[insane selection](https://pypi.python.org/pypi?%3Aaction=browse) of
high-quality libraries to do almost anything.  But even in cases where
I wouldn't expect either of those factors to make much difference,
Python still often wins.

Python's pragmatic nature is probably the biggest factor.  It's
opinionated, but it's not the opinion of a fanatic: it doesn't force
you to write pure functions without side-effects (though I'd argue
it's a good idea in general); it
[for the most part](http://lambda-the-ultimate.org/node/587) doesn't
leave features out for ideological reasons; it doesn't strive for
syntactic consistency at the cost of built-in expressiveness — the
design decisions of Python seem driven in general by a desire to see
people get things done and **now**, and it has worked, even though
some of those decisions — e.g. its ridiculously broken "lexical scope"
— are objectively bad.

So, for a surprising number of things, Python is the right language.
I'm still looking for the right language(s) for the others, when you
need fast native code, or ease of packaging and installation, or to
write mobile apps (ugh, Java).  For some of these things, maybe Nim
will be it; it shares Python's pragmatism and adds AOT native
compilation and easy distribution.  But more about that later; right
now, I've got some Python to write.
