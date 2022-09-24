#!/bin/bash
VASSAL_PYTHON_HOME="${HOME}/work/vassal-python"
javac -classpath ${VASSAL_PYTHON_HOME}/lib/java/Vengine.jar \
    -d ${VASSAL_PYTHON_HOME}/classlib/ ${VASSAL_PYTHON_HOME}/src/java/Helper.java