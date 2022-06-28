Feature: computing real income and taxes
  Scenario: create company and sell something
    Given I own company called 'ALKTOM' with income tax rate 19
    When I sell something for 12300 with vat rate 23
    Then my real income will be 8100.00

  Scenario: create company and sell/buy something
    Given I own company called 'ALKTOM' with income tax rate 19
    When I sell something for 25000 with vat rate 23
    And I buy Commputer for 11500 with vat rate 23
    And I buy Notebook for 2900 with vat rate 23
    Then my real income will be 213802.49
