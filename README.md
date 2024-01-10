# MT30 Alexa
This Project Integrates The Meraki MT30 With VoiceMonkey To Run Alexa Routines for Free!

## Installation

It is recommend to set up your environment as followed, to use this frontend template:

In the CLI:
1.	Choose a folder, then create and activate a virtual environment for the project
    ```python
    #WINDOWS:
    py -3 -m venv [add name of virtual environment here, usually venv] 
    source [add name of virtual environment here]/Scripts/activate
    #MAC:
    python3 -m venv [add name of virtual environment here, usually venv] 
    source [add name of virtual environment here]/bin/activate
    ```

2. Access the created virtual enviroment folder
    ```python
    cd [add name of virtual environment here] 
    ```

3.	Clone this Github repository into the virtual environment folder.
    ```python
    git clone [add github link here]
    ```
    For Github link: 
        In Github, click on the **Clone or download** button in the upper part of the page > click the **copy icon**
    
4. Access the folder 
    ```python
    cd [Folder Name]
    ```

5.	Install dependencies
    ```python
    pip3 install -r requirements.txt
    ```
6. Connect VoiceMonkey to your Amazon Account

7. Enter your API keys in your .env file!

8. Register your webhook onto the Meraki Dashboard as a receiver


## Usage
1.	Run the App!
    ```python
    python3 app.py
    ```

