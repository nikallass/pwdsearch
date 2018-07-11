# Password search tool
Tool searching for different default passwords in routers, web application management systems, databases, enterprise systems, etc. It uses Levenshtein distance for fuzzy search. It uses over 7500 default passwords.

## Install
    git clone https://github.com/nikallass/pwdsearch.git
    chmod u+x pwdsearch.py

## Usage
    ./pwdsearch.py            ---    print all passwords in csv and GoGrepYourself.
    ./pwdsearch.py tp-link    ---    search for all passwords related to TP-Link devices (or similar word).

## Hint
Use csvlook from csvkit to beautify csv in console.

1) Install csvkit:
    
    sudo apt install csvkit
    or
    sudo pip install csvkit

2) And then: 
    
    pwdsearch.py tp-link | csvlook


## TODO:
* Add tomat, jboss, coldfusion, weblogic, railo, axis2, glassfish
* Add ipmi, HP management systems, RabbitMQ and others

## Author
**nikallass**
<br>E-mail: <nikallass@yandex.ru>
<br>Telegram: [@is_man](https://t.me/is_man)