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


# The actual commands we want to execute.


source "/home/user/Final_Project/venv/bin/activate"

read -sp "Entrez le bon mot de passe d'utilisateur $USER: " passvar
gunicorn --bind 0.0.0.0:5000 --chdir /home/user/Final_Project/flaskr wsgi:app & \
echo $passvar | sudo -S /home/user/Final_Project/monitoror/monitoror

# Trap the input and wait for the script to be cancelled.
waitforcancel
return 0
