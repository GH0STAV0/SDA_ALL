#!/bin/bash


# telegram_tokens_van="5842682178:AAHhcZ41vh4XpIXvVhZ0-RuN0KkCClVgg4g"
# chat_id_alerts_van_google = "-1001633899177"
# TELEGRAM_BOT_TOKEN="5842682178:AAHhcZ41vh4XpIXvVhZ0-RuN0KkCClVgg4g"
TELEGRAM_BOT_TOKEN="2137513961:AAGENlwIUQnfvbKZX64-fZ72R_oStto8oFo"
# Chatid_alerts_van_google = "-857300964"





function maFonction()
{
  curl -X POST \
       -H 'Content-Type: application/json' \
       -d '{"chat_id": "-857300964", "text": "testContainer  exist", "disable_notification": true}' \
       https://api.telegram.org/bot$TELEGRAM_BOT_TOKEN/sendMessage
  
}
function testContainer2()
{
  curl -X POST \
       -H 'Content-Type: application/json' \
       -d '{"chat_id": "-857300964", "text": "👽Container does not exist", "disable_notification": true}' \
       https://api.telegram.org/bot$TELEGRAM_BOT_TOKEN/sendMessage
  
}

if [ $( docker ps -a | grep testContainer | wc -l ) -gt 0 ]; then
  echo "testContainer exists"
  maFonction1
else
  echo "testContainer does not exist"
  testContainer2
  bash -c "supervisorctl restart vncd"
fi


echo $TELEGRAM_BOT_TOKEN