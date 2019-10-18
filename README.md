# CEC-MCP-Curated_stREST

Curated REST calls for MCP.

## Pre-Requirements:

[stREST](https://github.com/eykrehbein/strest/blob/master/README.md)

```bash
sudo apt install nodejs npm
curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.11/install.sh | bash
command -v nvm
nvm install node
npm i -g @strest/cli
```

## Usage

The Dynamic FRE creation tests are designed to create services on any MCP server.  Assumptions:

* Available CCMD's

1. Make your reservation on [CEC](https://developer.ciena.com/) or use your own server.

    * Recommended CEC environment: BP-MCP L0 + L2 + Waveserver

1. Set environment variables

    ```bash
    export MCP_SERVER=https://your.server.ip
    export MCP_USERNAME=admin
    export MCP_PASSWORD=adminpw
    export LOG_STREST=true
    ```

1. Execute tests

    ```bash
    strest FRE/L0-6500_dynamic/ --output curl -s
    strest FRE/fre.strest.yml --output curl -s
    strest TPE/ --output curl -s
    strest PM/ --output curl -s
    strest Alarms/ --output curl -s
    ```
