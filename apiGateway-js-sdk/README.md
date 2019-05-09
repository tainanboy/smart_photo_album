speech-input
============

Simple speech input for `<input>` and `<textarea>` elements — replaces the now defunct `x-webkit-speech` attribute

## Use:

1. Include **speech-input.css** and **speech-input.js**
2. Add a `speech-input` class to your `<input>` or `<textarea>`

And you're done! Here's a demo:

[![speech-input demo][1]][2]

## Extra options

### Other languages
It uses the value of the `lang` attribute on the `<html>` element by default. But you can override this by specifying a `lang` attribute on the input fields themselves. You may then also want to customize the "Speak now" text for that language with a `data-ready` attribute on that field:

```html
<input type="text" class="speech-input" lang="es" data-ready="Habla ahora">
```

### Button size
If, for any reason, you want to change the button size, you can use the `data-buttonsize` attribute:

```html
<input type="text" class="speech-input" data-buttonsize="20">
```

### Speech time limit
By default, it will wait a full 6 seconds after you finish speaking until it stops listening. You can change this time with the `data-patience` attribute:

```html
<input type="text" class="speech-input" data-patience="2">
```

### Submit when done
If you add the `data-instant-submit` attribute, the form that the input is in will automatically be submitted after listening stops:

```html
<input type="text" class="speech-input" data-instant-submit>
```


## FAQ

### Why does it keep asking me to allow the microphone?
To have the microphone permissions persist, use https: http://stackoverflow.com/a/15999940/552067

### I clicked the mic button but it didn't do anything.
Make sure you're using it on an actual server — it won't work on a `file://` URL. Try [starting up a simple static HTTP server](https://gist.github.com/willurd/5720255).

### [Can I use](http://caniuse.com/#feat=web-speech) this in non-webkit browsers?
Not yet.

## [License (MIT)](http://hug.mit-license.org/)


[1]: http://f.cl.ly/items/3m0n2Q0y0h1a0N2P2s0Y/screenshot-by-nimbus.png
[2]: http://daniel-hug.github.io/speech-input/


# Prerequisites
For the JavaScript SDK to work your APIs need to support CORS. The Amazon API Gateway developer guide explains how to [setup CORS for an endpoint]().
The generated SDK depends on third-party libraries. Include all of the scripts in your webpage

    <script type="text/javascript" src="lib/axios/dist/axios.standalone.js"></script>
    <script type="text/javascript" src="lib/CryptoJS/rollups/hmac-sha256.js"></script>
    <script type="text/javascript" src="lib/CryptoJS/rollups/sha256.js"></script>
    <script type="text/javascript" src="lib/CryptoJS/components/hmac.js"></script>
    <script type="text/javascript" src="lib/CryptoJS/components/enc-base64.js"></script>
    <script type="text/javascript" src="lib/url-template/url-template.js"></script>
    <script type="text/javascript" src="lib/apiGatewayCore/sigV4Client.js"></script>
    <script type="text/javascript" src="lib/apiGatewayCore/apiGatewayClient.js"></script>
    <script type="text/javascript" src="lib/apiGatewayCore/simpleHttpClient.js"></script>
    <script type="text/javascript" src="lib/apiGatewayCore/utils.js"></script>
    <script type="text/javascript" src="apigClient.js"></script>

# Use the SDK in your project

To initialize the most basic form of the SDK:

```
var apigClient = apigClientFactory.newClient();
```

Calls to an API take the form outlined below. Each API call returns a promise, that invokes either a success and failure callback

```
var params = {
    //This is where any header, path, or querystring request params go. The key is the parameter named as defined in the API
    param0: '',
    param1: ''
};
var body = {
    //This is where you define the body of the request
};
var additionalParams = {
    //If there are any unmodeled query parameters or headers that need to be sent with the request you can add them here
    headers: {
        param0: '',
        param1: ''
    },
    queryParams: {
        param0: '',
        param1: ''
    }
};

apigClient.methodName(params, body, additionalParams)
    .then(function(result){
        //This is where you would put a success callback
    }).catch( function(result){
        //This is where you would put an error callback
    });
```

#Using AWS IAM for authorization
To initialize the SDK with AWS Credentials use the code below. Note, if you use credentials all requests to the API will be signed. This means you will have to set the appropiate CORS accept-* headers for each request.

```
var apigClient = apigClientFactory.newClient({
    accessKey: 'ACCESS_KEY',
    secretKey: 'SECRET_KEY',
    sessionToken: 'SESSION_TOKEN', //OPTIONAL: If you are using temporary credentials you must include the session token
    region: 'eu-west-1' // OPTIONAL: The region where the API is deployed, by default this parameter is set to us-east-1
});
```

#Using API Keys
To use an API Key with the client SDK you can pass the key as a parameter to the Factory object. Note, if you use an apiKey it will be attached as the header 'x-api-key' to all requests to the API will be signed. This means you will have to set the appropiate CORS accept-* headers for each request.

```
var apigClient = apigClientFactory.newClient({
    apiKey: 'API_KEY'
});
```



