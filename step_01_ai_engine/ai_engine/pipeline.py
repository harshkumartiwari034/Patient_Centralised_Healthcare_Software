from .logger import get_logger

class AIPipeline:
    def __init__(self):
        self.logger=get_logger("AI_PIPELINE")

    def process(self,image_path:str)->dict:
        self.logger.info("Pipeline started")
        # Future modules will be connected here.
        return {
            "success":True,
            "stage":"foundation",
            "image":image_path
        }
