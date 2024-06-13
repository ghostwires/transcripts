#!/bin/zsh

eval `ssh-agent -s` && ssh-add ~/.ssh/id_ed25519_creeperfromdiscord && ssh-add -l
REPO_PATH="/Users/home/projects/transcripts/"
git -C "$REPO_PATH" add -A
git -C "$REPO_PATH" commit --allow-empty -m "[the weekly auto-save]"
git -C "$REPO_PATH" push
# pmset disablesleep 0