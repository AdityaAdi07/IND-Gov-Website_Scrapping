# Sracpy Project on Indian Goverment Website
This is a legal, harmless web scrapping project that return the latest and all goverment schemes for the elderly people.

## Table Of Contents
1. [Scrapy spider, for web scrawling](#infospider.py)
2. [Website Flask](#app.py)
3. [Index file](#index.html)
4. [Schemes data, url in JSON format](#clean.json)
5. [Fake agent and Proxies](#middlewares.py)

## Features
- **Robot.txt bypass**: As scrapy is a bot, similar to other commercial and public site indian government website blocks from scraping, so to overcome that, this project inclues Fake Agents, Fake Headers and Proxy sites so the websites treat us like normal user. This can be seen in [middleware file](#middelwares.py).
- **highlights**: Asks for Gender, Age and State input which procesess and pushes the result at top with highlighting.
- **Easy to maintain**:Indian Gov site being dynamically updated, this scrapy project requires regular maintenance, which can be done easily as the html inspection code is commented out.

## Images
![Screenshot 2024-11-19 203313](https://github.com/user-attachments/assets/8d2c1b03-efbc-4670-b3fd-086e2038bdd6)
![Screenshot 2024-11-19 203442](https://github.com/user-attachments/assets/70062b64-9c29-4f74-8917-da900ff272bc)
![Screenshot 2024-11-19 203522](https://github.com/user-attachments/assets/5a2e091c-ef62-4690-a957-c9fd4e52aedd)



## Techstacks
1. Python
2. Scrapy, a python library for extensive web scrapping and retrive data
3. Flask for backend of webpage
4. html & CSS for frontend


