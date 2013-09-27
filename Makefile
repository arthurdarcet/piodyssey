# Shamelessly copied from http://git.polytechnique.org/?p=xnet;a=blob_plain;f=Makefile;hb=HEAD

MANAGE_PY = python manage.py


define help
Makefile command help

Available targets are:

Running:
  run:	      Start a development server on http://127.0.0.1:8000/
  shell:      Open a development Python shell using the current database

Database:
  resetdb:    Reinitialize the database schema

Testing:
  test:	      Run the test suite

Misc:
  clean:      Cleanup all temporary files (*.pyc, ...)
  help:       Display this help message
endef

default: all


all:


help:
	@echo -n ""  # Don't display extra lines.
	$(info $(help))


.PHONY: all default help


# Running
# =======

run:
	@$(MANAGE_PY) runserver

shell:
	@$(MANAGE_PY) shell

scrap:
	@$(MANAGE_PY) scrap --all

.PHONY: run shell


# Development
# ===========

test:
	@$(MANAGE_PY) test

resetdb:
	@rm -f local.db
	@$(MANAGE_PY) syncdb --noinput

.PHONY: resetdb test


# Misc
# ====

clean:
	@find . "(" -name "*.pyc" -or -name "*.pyo" -or -name "*.mo" ")" -delete
	@find . -type d -empty -delete

.PHONY: clean
