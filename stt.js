var request = require('request');
var options = {
  'method': 'POST',
  'url': 'https://api.eu-gb.speech-to-text.watson.cloud.ibm.com/instances/4504d974-dd28-4a72-9a17-8d25d5818858/v1/recognize?timestamps=true&max_alternatives=3',
  'headers': {
    'model': 'en-US_NarrowbandModel',
    'Content-Type': 'audio/mp3',
    'Authorization': 'Basic YXBpa2V5OkNfMVR5UmwwdzFyQkhESnV6NFJNYlFaQlpHaEl6S2pnYmVlZ2pMM1JsZVNH'
  },
  body: "audio2.mp3"

};
request(options, function (error, response) {
  if (error) throw new Error(error);
  console.log(response.body);
});

