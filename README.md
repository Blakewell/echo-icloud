# echo-icloud

This is a project in its beginning stages to connect the iCloud to Amazon Echo (Alexa)

##Configuration

A config.json file needs to be placed inside of the zip file before uploading to the AWS Lambda function.  The configuration file should look something like:

```javascript
{
    "devices": [
        {
		"name": "YourName",
		"userName": "YourITunesEmailAddress",
		"password": "YourITunesPassword",
		"deviceIdx": "0"
        }
    ]
}
```

This provides the crucial information needed to log into the iCloud service to find your phone.  

##Usage

All commands begin with "Alexa, ask *iCloud*...".  *iCloud* is the name that I chose when creating my Alexa skill, but you can name it something to your liking.    

### Find your phone

* Find my iPhone
* Find my phone
* Where is my iPhone?
* Where is my phone?
