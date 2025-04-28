.PHONY: all run test clean doc pack stddev help

all: run

run:
	python3 src/calculator.py

test:
	pytest tests/

clean:
	find . -type f -name '*.pyc' -delete
	rm -rf pycache build dist

doc:
	doxygen Doxyfile

pack:
	zip -r xgulasa00_xfackas00_xhorstd00_xjakubm00.zip src/ tests/ README.md Makefile Doxyfile requirements.txt

stddev:
	python3 src/stddev.py

help:
	@echo "Makefile commands:"
	@echo "  make all    - Run the program"
	@echo "  make run    - Run the program"
	@echo "  make test   - Run tests"
	@echo "  make clean  - Delete temporary and generated files"
	@echo "  make doc    - Generate documentation"
	@echo "  make pack   - Package the project for submission"
	@echo "  make stddev - Run the standard deviation program"