#!/bin/bash
VASSAL_PYTHON_HOME="${HOME}/work/vassal-python"
VASSAL_HOME="${HOME}/Documents/VASSAL/VASSAL-3.6.4"
javac -classpath "${VASSAL_HOME}/lib/*" \
    -d ${VASSAL_PYTHON_HOME}/lib/java/ ${VASSAL_PYTHON_HOME}/src/java/Helper.java