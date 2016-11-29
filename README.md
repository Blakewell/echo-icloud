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
2. The Alexa skill calls a Python service running an AWS Lambda function
3. AWS Lambda then calls iCloud using the popular [pyicloud](https://github.com/picklepete/pyicloud) library

## Setup 

Amazon has provided a good walk-through on getting started with [developing an Alexa Skill as a Lambda Function](https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/docs/developing-an-alexa-skill-as-a-lambda-function).  This will be the technique we use for this integration.

### Configure the AWS Lamba Function that will call iCloud

An Alexa skill that relies on an AWS Lambda Function has two parts: the AWS Lambda Function and the Alexa Skill.  The following steps focus on the first part of the equation.

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
* Test the function in the AWS Lambda Function console with the test script [available here](https://github.com/Blakewell/echo-icloud/blob/master/tests/lambda/findPhoneTest.json).  
* Copy your ARN located in the upper-right hand corner.  You'll need it when you configure your Alexa skill.  

### Configure the Alexa Skill

An Alexa skill that relies on an AWS Lambda Function has two parts: the AWS Lambda Function and the Alexa Skill.  The following steps focus on the second part of the equation.

* Go to the Amazon Developer console and select the [Alexa tab](https://developer.amazon.com/edw/home.html).  
* Click on **Get Started** and then **Add a New Skill**.
* Add a name (*echo-icloud*) and an invocation name (*iCloud).  You can use whatever you want here, but the Invocation Name is how you will call your skill (i.e. "Alexa, ask iCloud to find my phone")
* In the **Interaction Model** tab it will ask you for an *intent schema*.  Use the file located [here](https://github.com/Blakewell/echo-icloud/blob/master/echo/intents.json).
* Also in the  **Interaction Model** tab it will ask you for *Sample Utterances*.  Use the file located [here](https://github.com/Blakewell/echo-icloud/blob/master/echo/utterances.txt).  
* In the **Configuration** tab select the *AWS Lambda ARN* radio button and then click your Geographic Region.  Finally, enter the *ARN* you received when setting up your AWS Lambda Function.    
* Test your function my typing an expression like "Find my phone".  
