mySQLHandler KNOWN BUGS
=======================


Alpha version:
--------------

1. Crash if log table is dropped.

-Context:
if log table is dropped, python using this handler will raise Exception.
This occurs especially during test period (debug mode), when log table became too large and log table is manually dropped :p

-Reproductability:
Always

- Issue #1 in github

- Fixed by commit e8224c7701 (improperly assigned fixing #2, so recommiting


2. Crash with flask server?

-Context:
Flask server serving multi threaded python using this handler will crash improperly.

- Issue #2 in github

