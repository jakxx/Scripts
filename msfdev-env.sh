#/bin/bash
#
#Description: 	This script automates the commands given here: https://github.com/rapid7/metasploit-framework/wiki/Setting-Up-a-Metasploit-Development-Environment
#			  	to setup a MSF development environment on a linux machine.
#
#Author:		jakx
#
#Notes:			this has only been tested on Backtrack5 r3 

sudo apt-get -y install \
  build-essential zlib1g zlib1g-dev \
  libxml2 libxml2-dev libxslt-dev locate \
  libreadline6-dev libcurl4-openssl-dev git-core \
  libssl-dev libyaml-dev openssl autoconf libtool \
  ncurses-dev bison curl wget postgresql \
  postgresql-contrib libpq-dev \
  libapr1 libaprutil1 libsvn1 \
  libpcap-dev

\curl -L https://get.rvm.io | bash -s stable --autolibs=enabled --ruby=1.9.3

source /usr/local/rvm/scripts/rvm

rvm install 1.9.3-p125

git clone https://github.com/rapid7/metasploit-framework.git

gem install bundle && bundle install

echo "Script has finished, now you should be able to run ./msfconsole from your new metasploit directory"
