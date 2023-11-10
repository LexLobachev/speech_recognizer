# The speech_recognizer bot
  
This program contains Telegram and VK's bots. Bots' phrases that he knows came from [DialogFlow](https://cloud.google.com/dialogflow/docs/).  

The service include the questions and answers from file `questions.json`.  
  

## Environment

### Requirements

Python3(python 3.11 is recommended) should be already installed. Then use pip3 to install dependencies:

```bash
pip3 install -r requirements.txt
```

## Program uses an environment variable

#### Variables:

```  
GOOGLE_APPLICATION_CREDENTIALS: path to Google's application default credentials(to json file)
GOOGLE_PROJECT_ID: project id on Google Cloud 
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
VK_BOT_TOKEN=your_vk_bot_token
TELEGRAM_ADMIN_BOT_TOKEN=your_admin_telegram_bot_token
TELEGRAM_CHAT_ID=your_telegram_chat_id
TG_ADMIN_CHAT_ID=your_admin_telegram_chat_id
QUESTIONS_PATH=path_to_file_with_phrases_dor_dialogflow
```  

## Run

Launch on Linux(Python 3) or Windows:

```bash
$(venv) python tg_bot.py # Telegram-bot
$(venv) python vk_bot.py # VK - bot
```

# Teaching bot 
Script `create_intent.py` upload new answers and questions to service DialogFlow.

```bash
python create_intent.py
```
