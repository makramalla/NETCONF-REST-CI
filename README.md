# REST-CI

Curated REST calls CI.
This CI uses a REST API client called [strest] (https://github.com/eykrehbein/strest)
The same procedure could also be created using ansible 



```bash
sudo apt install nodejs npm
curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.11/install.sh | bash
command -v nvm
nvm install node
npm i -g @strest/cli
```

## Usage

1. Set environment variables

    ```bash
    export NUAGE_URL=https://your.server.ip
    export NUAGE_USERNAME=admin
    export NUAGE_PASSWORD=adminpw
    export LOG_STREST=true
    ```

1. Execute tests

    ```bash
    strest alarms/alarms.strest.yml--output curl -s
 
    ```

# NETCONF-CI

Curated NETCONF calls CI.
This CI uses a NETCONF API Client called [netconf-console] (https://pypi.org/project/netconf-console/)

## Dependencies

[netconf-console](https://pypi.org/project/netconf-console/)

```bash
pip install ncclient
pip install netconf-console
```

## Usage

```bash
NETCONF_HOST=<URL>
NETCONF_USER=<USERNAME>
NETCONF_PW=<PASSWORD>
```
### Hello

Quick test to make sure you are connecting

```bash
# Hello
netconf-console --host=$NETCONF_HOST --user=$NETCONF_USER --password=$NETCONF_PW --port=830 --hello
```

### Date and Time  
rpc located: [system](system)
```bash
# Set Date and Time  
netconf-console --host=$NETCONF_HOST --user=$NETCONF_USER --password=$NETCONF_PW --port=830 --rpc=system/date-time_set.xml
# Get Date and Time  
netconf-console --host=$NETCONF_HOST --user=$NETCONF_USER --password=$NETCONF_PW --port=830 --rpc=system/date-time_get.xml
```

### Alarms

Commands print their output to alarms.xml

rpc located: [alarm](alarm)

```bash
# Get Alarms
netconf-console --host=$NETCONF_HOST --user=$NETCONF_USER --password=$NETCONF_PW --port=830 --rpc=netconf-alarm/get-alarms.xml > output/alarms.xml
# Get Alarms Active
netconf-console --host=$NETCONF_HOST --user=$NETCONF_USER --password=$NETCONF_PW --port=830 --rpc=netconf-alarm/get-alarm-active.xml > output/alarms-act.xml
# Get Alarms History
netconf-console --host=$NETCONF_HOST --user=$NETCONF_USER --password=$NETCONF_PW --port=830 --rpc=netconf-alarm/get-alarm-history.xml > output/alarms-his.xml
# Get Alarms Statistics
netconf-console --host=$NETCONF_HOST --user=$NETCONF_USER --password=$NETCONF_PW --port=830 --rpc=netconf-alarm/get-alarm-statistics.xml > output/alarms-st.xml
```