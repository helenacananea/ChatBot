<h1> Chatbot  </h1>

Service for process Telegram chatbot

***
<h2> Running program </h2>

Create a virtual environment to isolate our package dependencies locally
> python3 -m venv env
> source env/bin/activate

On Windows use:
> `env\Scripts\activate`

Create file environment .env and add following configurations:

# TELEGRAM CONFIGURATION
TG_API_BOT_TOKEN=""
TG_API_ID=""
TG_API_HASH=""

### Para saber qual id (TG_API_ID) do chat digit /id depois copie e cole no arquivo de configuração.

### APAGAR ARQUIVO bot.session caso venha mudar o hash

### Obtendo o chat id
 https://api.telegram.org/bot5371162236:AAFHvuLMpx7qUpwW7R7bM-D1di0cv32d0tU/getUpdates

json
''
{"ok":true,"result":
[{"update_id":128543316,
"message":{"message_id":10,"from":{"id":150142865,"is_bot":false,"first_name":"Felipe","last_name":"Vargas","username":"felipevg1"},"chat":{"id":-1001706494313,"title":"ANPD","type":"supergroup"},"date":1651955675,"text":"Ola"}}]}
''

### Instalando dependências:

pip install -r requirements.txt