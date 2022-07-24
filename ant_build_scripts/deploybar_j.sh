@echo off
CALL "/var/mqsi/iib-10.0.0.19/server/bin/mqsiprofile"
CALL "/var/mqsi/iib-10.0.0.19/server/bin/mqsideploy" -e %1 -a %2 -w 600  -i %3