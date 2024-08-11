#!/bin/bash

CURRENT_DIR=$(pwd)

if [[ ${CURRENT_DIR} == *bin ]];then
    CURRENT_DIR=$(dirname $CURRENT_DIR)
fi

PYTHON="python3.9"

VENV="${CURRENT_DIR}/venv"
LOG_DIR="${CURRENT_DIR}/logs"
LOG_FILE="${LOG_DIR}/setup.log"
CONFIG_FILE="${CURRENT_DIR}/config/app.setting.json"

PYTHONCACHE="__pycache__"

LOG() 
{
    echo "[`date`] - ${*}" | tee -a ${LOG_FILE}
}

SETUP_PLAYGROUND(){
    
    LOG "Seting up workplace ... Initiated"
    CLEAN_PLAYGROUND
    
    ${PYTHON} -m venv ${VENV}
    [ $? == 0 ] && LOG "Created environment ... Success" || LOG "Created environment ... Failed"

    source ${VENV}/bin/activate
    [ $VIRTUAL_ENV != "" ] && LOG " Inside Virtual environement ... $VIRTUAL_ENV" || exit 1

    pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org --no-cache-dir --upgrade pip
    pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org --no-cache-dir -r requirements.txt

    deactivate

    LOG "Seting up workplace ... Completed"
    return

}

CLEAN_PLAYGROUND(){
    
    LOG "Cleaning workplace ... Initiated"
    [ "x$VIRTUAL_ENV" != "x" ] && LOG "Please come out of virtual environment and try again" && exit 1
    [ -d ${VENV} ] && rm -rf ${VENV}
    [ -d ${LOG_DIR} ] && rm -rf ${LOG_DIR}/*

    find ${CURRENT_DIR} -name ${PYTHONCACHE} |while read fname; do
        [ -d "${fname}" ] && rm -rf "${fname}" && LOG "Deleted $fname ... Completed"
    done

    #[ -d ${PYTHONCACHE} ] && rm -rf ${PYTHONCACHE}
    LOG "Cleaning workplace ... Completed"

    return
}

HELP(){
cat <<EOF

  Usage : $0 Option

  Option :  setup -- Create playground
            clean -- Clean playground

EOF
}

MAIN(){

    case $1 in
	setup)
		SETUP_PLAYGROUND
		;;
	clean)
		CLEAN_PLAYGROUND
		;;
    help)
		HELP
		;;
	*)
		HELP
		;;
    esac
    
}

MAIN $*
