w#!/bin/zsh

REPO_PATH="~/projects/transcripts"
git -C "$REPO_PATH" add -A
git -C "$REPO_PATH" commit -m "[the weekly auto-save]"
git -C "$REPO_PATH" push