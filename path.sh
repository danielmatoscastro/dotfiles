#!/usr/bin/env bash

# My variables
export REPOS_HOME=$HOME/meus-repositorios
export DOTFILES=$REPOS_HOME/dotfiles
export SCRIPTS=$DOTFILES/scripts

# Android studio variables
export ANDROID_HOME=$HOME/Android/Sdk

# Add android studio directories to PATH
export PATH=$PATH:$ANDROID_HOME/emulator
export PATH=$PATH:$ANDROID_HOME/platform-tools

# Add scripts to PATH
export PATH=$PATH:$SCRIPTS