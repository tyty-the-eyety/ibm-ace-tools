@echo off
CALL "/opt/mqsi/10.0.0.19/server/bin/mqsiprofile"
CALL "/opt/mqsi/10.0.0.19/server/bin/mqsiapplybaroverride" -b %1 -p %2 -r 