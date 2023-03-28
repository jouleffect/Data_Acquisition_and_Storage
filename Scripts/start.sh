#!/bin/bash

echo "Lancio lo script parser_dati_sulla_procedura.py...."
if python3 parser_dati_sulla_procedura.py; then
	echo "Fatto!";
	echo "Lancio lo script parser_dati_generali_del_lotto.py...."
	if python3 parser_dati_generali_del_lotto.py; then
		echo "Fatto!";
		echo "Lancio lo script geo.py...."
		if python3 geo.py; then
			echo "Fatto!";
			echo "Lancio lo script arricchimento.py...."
			if python3 arricchimento.py; then
				echo "Fatto!";
			else 
				echo "Qualcosa è andata storta...";
			fi
		else 
			echo "Qualcosa è andata storta...";
		fi

	else 
		echo "Qualcosa è andata storta...";
	fi
fi