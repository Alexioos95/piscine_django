#!/bin/sh
curl -s --head $1 | grep Location | cut -b 11-
