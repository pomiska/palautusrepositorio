*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  antero
    Set Password  antsa123
    Set Password Confirmation  antsa123
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  mo
    Set Password  morjes123
    Set Password Confirmation  morjes123
    Submit Credentials
    Register Should Fail With Message  Invalid Username, username has to be at least 3 characters long

Register With Valid Username And Too Short Password
    Set Username  roope
    Set Password  roba1
    Set Password Confirmation  roba1
    Submit Credentials
    Register Should Fail With Message  Invalid password, password has to be at least 8 characters and contain numbers or symbols

Register With Nonmatching Password And Password Confirmation
    Set Username  eero
    Set Password  eeroboy69
    Set Password Confirmation  eeropoju69
    Submit Credentials
    Register Should Fail With Message  Nonmatching password and password confirmation

*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password confirmation}
    Input Password  password_confirmation  ${password_confirmation}

Submit Credentials
    Click Button  Register

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}