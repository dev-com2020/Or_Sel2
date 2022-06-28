
*** Settings ***
Library  SeleniumLibrary  screenshot_root_directory=\screenshot
Library  Dialogs
Library  OperatingSystem

*** Keywords ***

Open the browser
    ${new_browser} = Get Selection From User In which browser you want to run the test? chrome firefox edge
    Set Global Variable ${BROWSER} ${new_browser}
User is in Sklep site and is search something
    Open browser    ${SEARCH_URL} ${BROWSER}
    Title Should Be Login - My Store
User clicks the search input
    Input Text ${search}        summer


