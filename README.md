# Password search tool
Tool searching for different default passwords in routers, web application management systems, databases, enterprise systems, etc. It uses Levenshtein distance for fuzzy search. It uses over 7500 default passwords.

## Install
    git clone https://github.com/nikallass/pwdsearch.git

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

## Sources
Routers and others:
    
    DONE!   http://open-sez.me/
    DONE!   http://defaultpasswords.in/
    http://www.defaultpassword.com/
    https://cirt.net/passwords
    http://www.defaultpassword.us/
    https://default-password.info/
    https://www.bestvpn.com/guides/default-router-login-details/
    https://192-168-1-1ip.mobi/default-router-passwords-list/
    http://www.routerpasswords.com/
    http://phenoelit.org/dpl/dpl.html
    https://github.com/jeanphorn/wordlist
    https://datarecovery.com/rd/default-passwords/
    https://www.lifewire.com/netgear-default-password-list-2619154

IP-CAM:
    
    https://ipvm.com/reports/ip-cameras-default-passwords-directory

WEB:
    
    http://securenetworkmanagement.com/default-password-list/

Other:

    http://support.huawei.com/enterprise/en/doc/EDOC1000118783?section=j004

## Author
**nikallass**
<br>Telegram: [@is_man](https://t.me/is_man)
<br>LinkedIn: [Nikita M.](https://linkedin.com/in/mednikand)