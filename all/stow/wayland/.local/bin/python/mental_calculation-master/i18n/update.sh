#!/bin/bash

cd ..
pylupdate5 mentalcalculation.py gui/settings.py gui/main.py -ts mentalcalculation.ts
for l in fr cs it es_ES; do
	pylupdate5 mentalcalculation.py gui/settings.py gui/main.py -ts i18n/$l.ts
done
