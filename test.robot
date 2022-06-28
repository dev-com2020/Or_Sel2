
*** Settings ***
Library SeleniumLibrary screenshot_root_directory=\screenshot
Resource Resources/
Resource Resources/

Suite Setup
Valid Login
    [Tags] Valid
    [Documentation] To jest test logowania do portalu
    Given User is in Sklep site and is not search
    And And clicks the Search Input
    When User click the search button
    Then User see the summer collection
    [Teardown] Close Browser

Invalid Login
    [Tags] Invalid
    [Documentation] To jest test niepoprawnego logowania do portalu
    Given
    And
    When
    Then
    [Teardown] Close Browser
