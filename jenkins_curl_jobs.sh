#!/bin/bash

curl -XPOST http://<jenkins_host>:8080/job/<folder>/job/<job_name>/build --user <user>:<token>
curl -XPOST http://<jenkins_host>:8080/job/<folder>/job/<job_name>/buildWithParameters?BUILD_SELECTOR=%3CSpecificBuildSelector%20plugin%3D%22copyartifact%401.46.1%22%3E%3CbuildNumber%3E1%3C%2FbuildNumber%3E%3C%2FSpecificBuildSelector%3E --user <user>:<token>
