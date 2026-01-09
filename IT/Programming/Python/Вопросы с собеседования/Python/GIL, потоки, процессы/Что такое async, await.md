### Что такое async/await, для чего они нужны и как их использовать

Ключевое слово `async` идет до `def`, чтобы показать, что метод является асинхронным. Ключевое слово `await` показывает, что вы ожидаете завершения сопрограммы.

```python
import asyncio
import aiohttp

urls = ['http://www.google.com', 'http://www.yandex.ru', 'http://www.python.org']

async def call_url(url):
    async with aiohttp.ClientSession() as session:
        print('Starting {}'.format(url))
        async with session.get(url) as response:
            data = await response.text()
            print('{}: {} bytes: {}'.format(url, len(data), data))
            return data

futures = [call_url(url) for url in urls]

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.gather(*futures))
```

Программа состоит из метода async. Во время выполнения он возвращает сопрограмму, которая затем находится в ожидании.

`async/await` нужен для того, чтобы не блокировать поток выполнения на время ожидания какого-нибудь асинхронного события. Конструкция `async/await` превращает по сути процедуру в корутину (сопрограмму): она прекращает своё выполнение на время `await`, дожидается асинхронного события, и возобновляет работу.

В не-async-варианте ожидание получается блокирующим, или нужно вручную делать трюки: запускать операцию и подписываться на её окончание. Async делает код более простым, линейным.