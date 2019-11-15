NAME=report
all:
	pdflatex $(NAME).tex
	bibtex $(NAME)
	pdflatex $(NAME)
	pdflatex $(NAME)

dvi:
	latex $(NAME).tex
	#bibtex $(NAME)
	latex $(NAME).tex
	dvips $(NAME).dvi


clean:	
	#rm -rf $(NAME).bbl
	rm -rf $(NAME).ps $(NAME).dvi $(NAME).log
	rm -rf $(NAME).toc $(NAME).blg $(NAME).bbl
	rm -rf $(NAME).aux $(NAME).out 
	rm -rf *~ *.aux *.log *.xml *.bcf

