# Makefile to make easier running scripts

serve:
	uvicorn src.main:app --reload --host 192.168.0.53