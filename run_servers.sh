#!/bin/bash



# Triggered when the user interrupts the script to stop it.
trap quitjobs INT
quitjobs() {
    echo ""
    pkill -P $$
    echo "Killed all running jobs".
    scriptCancelled="true"
    trap - INT
    exit
}


# Wait for user input so the jobs can be quit afterwards.
scriptCancelled="false"
waitforcancel() {
    while :
    do
        if [ "$scriptCancelled" == "true" ]; then
            return
        fi

        sleep 1
    done
}


# GET le dossier ou le script se trouve
SCRIPT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" &> /dev/null && pwd)


# The actual commands we want to execute.

read -sp "Entrez le bon mot de passe d'utilisateur $USER: " passvar

# Lancement de serveur flask en utilisent gunicorn
gunicorn --bind 0.0.0.0:5000 --chdir $SCRIPT_DIR/flaskr wsgi:app & \


# Lancement de serveur monitoror 
echo $passvar | sudo -S $SCRIPT_DIR/monitoror/monitoror




# Trap the input and wait for the script to be cancelled.
waitforcancel
return 0
