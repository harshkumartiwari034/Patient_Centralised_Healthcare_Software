class AIEngineError(Exception):
    pass

class OCRFailed(AIEngineError):
    pass

class ParserFailed(AIEngineError):
    pass
