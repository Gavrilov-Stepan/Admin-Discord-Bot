import bot
import pytest
import unittest.mock

#тест для функции multiply
@pytest.mark.asyncio
async def testmulty():
    ctx = unittest.mock.Mock()
    ctx.send = unittest.mock.AsyncMock()
    a = 9
    b = 10
    await bot.multiply(ctx,a,b)
    ctx.send.assert_called_with("9 * 10 = 90")