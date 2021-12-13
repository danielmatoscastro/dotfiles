#!/usr/bin/env bash

RIDER_INSTALLATION_HOME=/home/daniel/rider
RIDER_DESKTOP_FILE=$DOTFILES/rider/Rider.desktop

rm -rf $RIDER_INSTALLATION_HOME

mkdir $RIDER_INSTALLATION_HOME

tar -xzf $1 --directory=$RIDER_INSTALLATION_HOME --strip-components=1

sudo desktop-file-install $RIDER_DESKTOP_FILE

