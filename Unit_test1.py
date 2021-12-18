import bot
import pytest
import unittest.mock

#тест для рандомной функции, иногда работает, иногда нет.
@pytest.mark.asyncio
async def testroll():
    ctx = unittest.mock.Mock()
    ctx.send = unittest.mock.AsyncMock()
    words = ['Dima', 'Ru']
    await bot.choose(ctx, *words)
    ctx.send.assert_called_with("How about this - Dima? From this List('Dima', 'Ru')")
