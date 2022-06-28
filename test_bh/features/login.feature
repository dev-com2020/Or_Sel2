Feature: sign in to e-mail account
  As a user I want to log in
  and check my emails

  Scenario Outline: Log in with valid data
    Given user is on Poczta Onet website
    When user fills in the Sign In form <login> and <pass> and submits it
    Then User can see email list

    Examples: login
      | login    | pass  |
      | Mobile   | 1@230 |
      | Computer | 36#00 |
      | Notebook | 799$9 |