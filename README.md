# LEETSOLVER
A Chrome extension that solves Leet Code Problems for you. </br>
 You can check how it works in this link ->

# Built with:
<img src="https://github.com/RaedNefzi98/LEETSOLVER/assets/74836098/0fb1c5b4-b0ca-4633-9d95-6985ca6a74f8" alt="Flask-Dark" width="70"> <img src="https://github.com/RaedNefzi98/LEETSOLVER/assets/74836098/25bad7e8-9751-4782-8127-92f5cd702c3e" alt="React-Dark" width="70"> <img src="https://github.com/RaedNefzi98/LEETSOLVER/assets/74836098/be6e66b1-9f51-4ef9-8dc4-4e727b85aa03" alt="Python-Dark" width="70">  <img src="https://github.com/RaedNefzi98/LEETSOLVER/assets/74836098/155d57ac-c48f-446f-9fff-ffb7e8e81fdb" alt="Webpack-Dark" width="70">


# How to use
### 1) Install the packages 
*(you need the lastest version of node)*

Run npm install (or yarn)
```
$ npm install
```
Build the frontend
```
$ npm install react-switch --save
$ npm run build
```

### 3) Load the extension
See [Chrome's developer tutorial](https://developer.chrome.com/docs/extensions/mv3/getstarted/development-basics/) on how to start a chrome extension project. You can select this repository as the unpacked extension to run (should work out of the box)

### 3) Run the Backend locally or in a google Colab:

The bot runs off of an API that's running flask/ngrok. The API is in front of Code LLama Instruct.*Remember you have to copy the ngrok url to the `popup/components/SolverForm.js` file*

Update this url with the new ngrok url from flask
```
	const apiUrl = "http://fcc9-34-28-212-176.ngrok.io"; // change this line
```

Install these the Dependecies:
```
!pip install transformers
!pip install accelerate
!pip install -i https://test.pypi.org/simple/ bitsandbytes
!pip install flask-ngrok
```
Login with you huggingFace account and add your Token:
```
!huggingface-cli login
```
