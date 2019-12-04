
default:
	@echo "default"
	python generate_sage.py testing.ipynb
	jupyter nbconvert testing_sage.ipynb --TagRemovePreprocessor.remove_input_tags="['remove_input']" --to slides
	python generate_sage.py testing_sage.slides.html

%.html: %.ipynb
	@echo $(basename $@)
	python generate_sage.py $(basename $@).ipynb
	jupyter nbconvert $(basename $@)_sage.ipynb --TagRemovePreprocessor.remove_input_tags="['remove_input']" --to slides
	python generate_sage.py $(basename $@)_sage.slides.html

clean:
	@echo "clean"
	git clean . -fx

.PHONY: Makefile
