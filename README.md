# echo-icloud

This is a project in its beginning stages to connect the iCloud to Amazon Echo (Alexa)

##Usage

All commands begin with "Alexa, ask *iCloud*...".  *iCloud* is the name that I chose when creating my Alexa skill, but you can name it something to your liking.    

### Find your phone

* Find my iPhone
* Find my phone
* Where is my iPhone?
* Where is my phone?

## How it works

1. When you say the command to Alexa, it triggers the Alexa skill with invocation name iCloud
2. The Alexa skill calls a Python service running on AWS Lambda
3. AWS Lambda then calls iCloud using the popular [pyicloud](https://github.com/picklepete/pyicloud) library

## Setup 

### Configure the AWS Lamba service that will call iCloud

Amazon has provided a good walk-through on getting started with [developing an Alexa Skill as a Lambda Function](https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/docs/developing-an-alexa-skill-as-a-lambda-function).  This will be the technique we use for this integration.

* Download the zip file of the code from this repository (for simplicity I've created a [deployment.zip](https://github.com/Blakewell/echo-icloud/blob/master/install/deployment.zip) file).
* Add a file called config.json that contains your account credentials.  The file should look like this:

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

* Create a Lambda function using the [AWS Lambda Console]("https://console.aws.amazon.com/lambda")
* Select Python 2.7 as the language and pick the Alexa blueprint (we'll be overridding it with our own code)
* Specify a name (I used echo-icloud).  Accept all defaults but be sure to set up an appropriate security role (mine was called lambda_basic_execution)
* Go to the **Code** tab and select *Upload a .ZIP file* in the **Code entry type** dropdown 
* Upload the *deployment.zip* file you modified earlier.  
* Test the function with the test script available here.  


