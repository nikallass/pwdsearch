# Password search tool
Tool searching for different default passwords in routers, web application management systems, databases, enterprise systems, etc. It uses Levenshtein distance for fuzzy search. It uses over 11000 default passwords.

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
* Fix excel text -> num autocorrection. 0000 became 0, 000001 became 1, "1234" bacame "1,234".
* Fix CaSiNg of key fields.
* Fix small (2 word) search falses.
* Add multiword search
* csvlook by default
* Add coldfusion, railo, axis2, terradata

### Add source:

#### Routers and others:

https://www.urtech.ca/2011/12/default-passwords/  
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

#### SCADA:

[SCADA Default Password (SDPD)](http://www.critifence.com/default-password-database/)  
[Default Passwords for Nearly Every SCADA System](https://www.hackers-arise.com/single-post/2016/09/21/Scada-Hacking-Default-Passwords-for-Nearly-Every-SCADA-System)  

#### Other:    

[default accounts wordlist](https://github.com/milo2012/pentest_scripts/tree/master/default_accounts_wordlist)  
[netbiosX/Default-Credentials](https://github.com/netbiosX/Default-Credentials)  
[tenable: plugins: Default unix accounts](https://www.tenable.com/plugins/index.php?view=all&family=Default+Unix+Accounts)  
[default password list (2007-07-03)](http://www.phenoelit.org/dpl/dpl.html)  


## Password Sources
https://github.com/ztgrace/changeme  
https://github.com/danielmiessler/SecLists/blob/master/Miscellaneous/wordlist-common-snmp-community-strings.txt  
https://github.com/breenmachine/VulnCheckFramework/tree/master/credentialDatabase  
http://securenetworkmanagement.com/default-password-list/  
http://open-sez.me/  
http://defaultpasswords.in/  
https://github.com/danielmiessler/SecLists/blob/master/Passwords/Default-Credentials/  
https://github.com/danielmiessler/SecLists/blob/master/Passwords/Default-Credentials/scada-pass.csv  
https://ipvm.com/reports/ip-cameras-default-passwords-directory  
https://github.com/govolution/betterdefaultpasslist/blob/master/mssql.txt  
https://github.com/rapid7/metasploit-framework/blob/master/data/wordlists/snmp_default_pass.txt  
https://github.com/netbiosX/Default-Credentials  
https://github.com/jarmouz/default_credentials/blob/master/Camera_DC.csv  
https://gist.github.com/todb-r7/5d86ecc8118f9eeecc15  
http://docs.antsle.com/defaultpw/  
http://documentation.microfocus.com/help/index.jsp?topic=%2Fcom.microfocus.sctm.doc%2FSCTM-CBA0F2AF-DATABASESETTINGSPAGE-REF.html  
http://geonetwork-opensource.org/manuals/2.10.4/eng/users/quickstartguide/installing/index.html  
http://kb.lenel.com/cd/12/articlesImport/1098.PDF  
http://opengts.sourceforge.net/OpenGTS_Config.pdf  
http://packetstormsecurity.com/files/125754/Loadbalancer.org-Enterprise-VA-7.5.2-Static-SSH-Key.html  
http://platforma.astor.com.pl/files/getfile/id/3781  
http://protechsecurity.us/wp-content/uploads/2013/12/IR-Schlage-Security-Management-System-V5.3.pdf  
http://resource.boschsecurity.com/documents/RPS_InGuide_Installation_Manual_enUS_2596022155.pdf  
https://community.rapid7.com/community/infosec/blog/2016/04/07/r7-2016-04-exagrid-backdoor-ssh-keys-and-hardcoded-credentials  
https://confluence.atlassian.com/hipchatkb/how-to-change-the-username-and-the-ssh-password-for-the-admin-user-875608217.html  
https://discuss.pivotal.io/hc/en-us/articles/217649658-How-to-connect-to-Ambari-s-PostgreSQL-database-  
http://seclists.org/fulldisclosure/2015/Jan/76  
http://sentinelldk.safenet-inc.com/LDKdocs/Install/Installation%20Guide/Troubleshooting/Troubleshooting.htm  
https://packetstormsecurity.com/files/125755/quantum-root.txt  
https://packetstormsecurity.com/files/125761/Array-Networks-vxAG-xAPV-Privilege-Escalation.html  
https://raw.githubusercontent.com/mitchellh/vagrant/master/keys/vagrant  
https://support.cch.com/kb/solution.aspx/sw29540  
https://twitter.com/0rbz_/status/914171719652401152  
https://wiki.netxms.org/wiki/Server_Installation_Guide  
https://www-01.ibm.com/support/docview.wss?uid=swg21645570  
https://www.ariscommunity.com/system/files/ARIS%20Server%20Installation%20and%20Administration%20Guide_0_0.pdf  
https://www.cisco.com/c/en/us/td/docs/wireless/access_point/1300/quick/guide/br13qsg.html  
https://www.cisco.com/en/US/products/ps5888/prod_release_note09186a0080237333.html  
https://www.cultofmac.com/20871/how-to-change-your-iphones-default-ssh-password/  
https://www.i2b2.org/software/projects/hivecore/Data_Installation_Guide_13.pdf  
https://www.ibm.com/support/knowledgecenter/en/SSLKT6_7.5.0/com.ibm.mam.doc/install_was/t_ccmdb_manconfigfoundinst.html  
https://www.ibm.com/support/knowledgecenter/en/SSQP76_8.7.0/com.ibm.odm.distrib.config.was/config_ds_res_was/tsk_was_before_res_config.html  
https://www.ibm.com/support/knowledgecenter/ST5Q4U_1.6.2/com.ibm.storwize.v7000.unified.162.doc/ifs_132_changedefaultpasswords11142011.html  
https://www.kb.cert.org/vuls/id/662676  
https://www.mytimeforce.com/images/videos/support/training/kb/docs/internal/support/time/TIMEFORCE1Migration.pdf  
https://www.nomotion.net/blog/sharknatto/  
https://www.team-mediaportal.com/wiki/display/MediaPortal1/SQL+Server+2008  
https://www.telestream.net/pdfs/app-notes/app_Vantage_DatabaseSetup.pdf  
https://www.trustedsec.com/june-2012/remote-root-authentication-bypass-for-f5-big-ip/  
https://www.trustmatta.com/advisories/MATTA-2012-002.txt  
https://www.tunnelsup.com/default-password-cisco-firewall/  
https://www.welchallyn.com/content/dam/welchallyn/documents/sap-documents/LIT/80013/80013928LITPDF.pdf  
http://us.allegion.com/content/dam/allegion-us-2/web-documents-2/UserGuide/Schlage_Campus_Lock_Keycard_Center_User_Guide_108225.pdf  
http://www.auftragsbearbeitung-warenwirtschaft-pps.de/p/Handbuch/Installation/Installationsanleitung/  
http://www.bernationalcontrols.com/support_docs/Access/Lenel/Facility%20Commander%20Wnx%207.7%20User%20Manual.pdf  
http://www.emerson.com/documents/automation/39924.pdf  
http://www.lasa.org.uk/uploads/aims/Installation_Guides/SQL_Server_Installation_Guide.pdf  
http://www.medocheck.com/site/assets/files/1440/kurzanleitung_mysql-server_fuer_medo_check.pdf  
http://www.napcosecurity.com/download/tg04L2RevB.pdf  
http://www.securityfocus.com/archive/1/354230  
http://www.seismicmicro.com/productreleasedocumentation/kingdom/installationguide.pdf  
http://www.skf.com/binary/79-267781/AA_2013_323124d0_IM-EN.pdf  
http://www.splendidcrm.com/Documentation/tabid/233/rvdwktid/deployment-guide-528/Default.aspx  
http://www.video-insight.com/kb/pdf.php?cat=15&id=111&artlang=en  


## Author
**nikallass**
<br>Telegram: [@is_man](https://t.me/is_man)
<br>LinkedIn: [Nikita M.](https://linkedin.com/in/mednikand)
