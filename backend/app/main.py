import os
from process_url import ProcessUrl
import asyncio



async def main() -> None:
    process_url = ProcessUrl(url='https://stackoverflow.com/questions/626754/how-to-find-out-the-summarized-text-of-a-given-url-in-python-django')
    # print(await process_url.get_screenshot(file_name='test'))
    # print(process_url.get_title())
    # print(process_url.find_p())
    with open('./note.txt', 'w') as f:
        for i in process_url.get_some_data():
            f.write(i)


if __name__ == '__main__':
    asyncio.run(main())
