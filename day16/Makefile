
all: test.pdf

%.pdf: %.dot
	dot -Tpdf $< -o $@
	evince $@

%.dot: %.txt txt2dot.py
	./txt2dot.py $< $@
