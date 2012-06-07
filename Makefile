test:
	python setup.py test

clean:
	$(RM) -r *.so *.c *.pyc __pycache__ *.egg-info build
