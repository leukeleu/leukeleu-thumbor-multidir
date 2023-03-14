#!/usr/bin/python
# -*- coding: utf-8 -*-

from os import fstat
from datetime import datetime
from os.path import join, exists, abspath

from six.moves.urllib.parse import unquote

from thumbor.loaders import LoaderResult
from thumbor.utils import logger

async def load(context, path):
    result = LoaderResult()

    for idx, next_dir in enumerate(context.config.TC_MULTIDIR_PATHS):

        file_path = join(next_dir.rstrip('/'), path.lstrip('/'))
        file_path = abspath(file_path)

        inside_root_path = file_path.startswith(abspath(next_dir))

        if inside_root_path:
            
            # keep backwards compatibility, try the actual path first
            # if not found, unquote it and try again
            found = exists(file_path)
            if not found:
                file_path = unquote(file_path)
                found = exists(file_path)

            if found:
                with open(file_path, 'rb') as f:
                    stats = fstat(f.fileno())

                    result.successful = True
                    result.buffer = f.read()

                    result.metadata.update(
                        size=stats.st_size,
                        updated_at=datetime.utcfromtimestamp(stats.st_mtime))
                return result

        logger.debug('TC_MULTIDIR: File {0} not found in {1}'.format(path, next_dir))
        # else loop and try next directory
    
    if not context.config.TC_MULTIDIR_PATHS:
        logger.error('TC_MULTIDIR: No paths set in configuration TC_MULTIDIR_PATHS')

    # no file found
    result.error = LoaderResult.ERROR_NOT_FOUND
    result.successful = False
    return result
