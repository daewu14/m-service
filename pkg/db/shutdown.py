import asyncio
import signal

from pkg.db.alchemy import Alchemy


async def _handle_shutdown_signal(signal_number, frame):
    await Alchemy().close_connection()


# Catch termination signals (SIGTERM, SIGINT)
signal.signal(signal.SIGTERM, lambda sig, frame: asyncio.create_task(_handle_shutdown_signal(sig, frame)))
signal.signal(signal.SIGINT, lambda sig, frame: asyncio.create_task(_handle_shutdown_signal(sig, frame)))
