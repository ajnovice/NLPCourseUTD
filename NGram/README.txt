# Python 3 to execute the NGRAMS.py
# corpus.txt and NGRAMS.py should be in the same folder
# 'python NGRAMS.py -N <N> -b <b>' command(without quotes) is used to execute the python.
	where <N> = (2 is used for BIGRAM and 3 is used for TRIGRAM)
		  <b> = (0 is used for WITHOUT ADD-ONE SMOOTHING and 1 is used for WITH ADD-ONE SMOOTHING)

Example :
	 python NGRAMS.py -N 2 -b 0 
	 Above command is used for BIGRAM WITHOUT SMOOTHING

	 python NGRAMS.py -N 3 -b 1
	 Above command is used for TRIGRAM WITH SMOOTHING
