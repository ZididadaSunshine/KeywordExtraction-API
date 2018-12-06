from KeywordExtraction.keyword_graph import TKGExtractor


class KWEServiceResponse:
    Success = 200
    Error = 400


def extract_keywords(corpus):
    extractor = TKGExtractor(corpus)
    return dict(keywords=extractor.extract_n_keywords(n=15)), 200
