import asyncio
from PIL import Image

from config.log_config import Logger as Log


async def resize(photo_path: str) -> bool:
    pic = Image.open(photo_path)
    try:
        pic.save(photo_path, optimize=True, quality=20)
        Log.logger.info('[UTILS] [Optimizer] Photo optimized')
        return True
    except Exception as e:
        Log.logger.error('[UTILS] [Optimizer] Could not optimize photo %r, Reason: %r', photo_path, e)
        return False


