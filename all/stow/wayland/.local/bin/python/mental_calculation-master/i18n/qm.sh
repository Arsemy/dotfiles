#!/bin/bash
#lrelease='/usr/lib/x86_64-linux-gnu/qt5/bin/lrelease'

ls -1 *.ts|while read ts
do
	lrelease $ts -qm ${ts/.ts}.qm
done
