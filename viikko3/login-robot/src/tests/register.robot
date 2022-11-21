*** Settings ***
Resource  resource.robot
Test Setup  Start Application and Input New Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  matti  matti123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  testaccount  password123
    Output Should Contain  New user registered
    Input New Command
    Input Credentials  testaccount  password321
    Output Should Contain  User with username testaccount already exists

Register With Too Short Username And Valid Password
    Input Credentials  aa  password123
    Output Should Contain  Invalid username, username has to be at least 3 characters long

Register With Valid Username And Too Short Password
    Input Credentials  kalle  pass1
    Output Should Contain  Invalid password, password has to be at least 8 characters long and contain numbers or symbols

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  kalle  password
    Output Should Contain  Invalid password, password has to be at least 8 characters long and contain numbers or symbols

*** Keywords ***
Start Application and Input New Command
    Run Application
    Input New Command


