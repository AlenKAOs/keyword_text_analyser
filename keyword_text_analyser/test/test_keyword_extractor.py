import os
import textract

from keyword_text_analyser.keyword_extractor import TextRank4Keyword


def test_get_keywords_from_cv():
    """
    Pass the text of a PDF file to the keyword extractor text analyser.
    Expect the keywords to be equal to the expected keywords from the pdf
    """
    dirname = os.path.dirname(__file__)
    path_to_pdf = os.path.join(dirname, 'sample.pdf')

    cvText = textract.process(path_to_pdf).decode("utf-8")

    tr4w = TextRank4Keyword()
    tr4w.analyze(cvText)

    assert tr4w.get_keywords() == 'care client experience arkansas childhood'
