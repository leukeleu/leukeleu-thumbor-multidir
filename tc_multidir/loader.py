#!/usr/bin/python
from thumbor.config import Config
from thumbor.context import Context
from thumbor.loaders import LoaderResult, file_loader
from thumbor.utils import logger

async def load(context, path):
    result = LoaderResult()

    for idx, next_dir in enumerate(context.config.TC_MULTIDIR_PATHS):
        result = await file_loader.load(Context(config=Config(FILE_LOADER_ROOT_PATH=next_dir)), path)

        if result.successful:
            return result

        logger.debug('TC_MULTIDIR: File {0} not found in {1}'.format(path, next_dir))
        # else loop and try next directory
    
    if not context.config.TC_MULTIDIR_PATHS:
        logger.error('TC_MULTIDIR: No paths set in configuration TC_MULTIDIR_PATHS')

    # no file found
    result.error = LoaderResult.ERROR_NOT_FOUND
    result.successful = False
    return result
