slides = introduksjon.html

default: $(slides)

%.html: %.ipynb
	python generate.py $(basename $@).ipynb
	jupyter nbconvert __$(basename $@).ipynb --TagRemovePreprocessor.remove_input_tags="['remove_input']" --SlidesExporter.reveal_theme=serif --to slides --template slides_reveal_custom.tpl --output=$(basename $@)
	python generate.py $(basename $@).slides.html
	@rm __$(basename $@).ipynb
	@mv $(basename $@).slides.html ../html/

clean:
	@echo "clean"
	git clean . -fx

.PHONY: Makefile
