echo "Installing and configuring CouchDB"

echo "Update the current packages"
sudo apt-get update

echo "Adding PPA Repository"
sudo apt-get install software-properties-common
sudo add-apt-repository ppa:couchdb/stable
sudo apt-get update

echo "Installing CouchDB"
sudo apt-get install couchdb

echo "Configuring ownership"
sudo chown -R couchdb:couchdb /usr/bin/couchdb /etc/couchdb /usr/share/couchdb

echo "Configuring permissions"
sudo chmod -R 0770 /usr/bin/couchdb /etc/couchdb /usr/share/couchdb

echo "Restarting CouchDB"

sudo systemctl restart couchdb

echo "Finished installing and configuring CouchDB"
