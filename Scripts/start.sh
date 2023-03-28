#!/bin/bash

echo "Lancio lo script parser1.py...."
if python3 parser1.py; then
	echo "Fatto!";
	echo "Lancio lo script parser2.py...."
	if python3 parser2.py; then
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
