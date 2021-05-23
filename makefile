# Signifies our desired python version
# Makefile macros (or variables) are defined a little bit differently than traditional bash, keep in mind that in the Makefile there's top-level Makefile-only syntax, and everything else is bash script syntax.
PYTHON = python3

# .PHONY defines parts of the makefile that are not dependant on any specific file
# This is most often used to store functions
.PHONY = help run fetch process model clean


# Defines the default target that `make` will to try to make, or in the case of a phony target, execute the specified commands
# This target is executed whenever we just type `make`
.DEFAULT_GOAL = help

# The @ makes sure that the command itself isn't echoed in the terminal
help:
	@echo "---------------HELP-----------------"
	@echo "To run the whole project type make run"
	@echo "To fetch raw data type make fetch"
	@echo "To process data type make process"
	@echo "To run the model type make model"
	@echo "------------------------------------"

run:
	${PYTHON} scripts/getData.py
	${PYTHON} scripts/models.py

fetch:
	${PYTHON} scripts/fetch.py

process:
	${PYTHON} scripts/process.py

model:
	${PYTHON} scripts/models.py

# In this context, the *.project pattern means "anything that has the .project extension"
clean:
	rm -r *.json *.csv
