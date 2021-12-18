import bot
import pytest
import unittest.mock

@pytest.mark.asyncio
async def testroll2():
    ctx = unittest.mock.Mock()
    ctx.send = unittest.mock.AsyncMock()
    message = '1'
    await bot.roll(ctx, message)
    ctx.send.assert_called_with("Roll: 1")
