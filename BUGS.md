mySQLHandler KNOWN BUGS
=======================


Alpha version:
--------------

1. Crash with flask server?

-Context:
Flask server serving multi threaded python using this handler will crash improperly.

- Issue #1 in github

2. Crash if log table is dropped.

-Context:
if log table is dropped, python using this handler will raise Exception.
This occurs especially during test period (debug mode), when log table became too large and log table is manually dropped :p

-Reproductability:
Always