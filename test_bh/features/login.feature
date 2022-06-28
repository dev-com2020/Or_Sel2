Feature: sign in to e-mail account
  As a user I want to log in
  and check my emails

  Scenario Outline: Perform searches using few words
    Given user is on automationpractice website
    When user fills in the Search form <search> and submits it
    Then User can see search result, and take a screenshot with <num> number

    Examples: question
      | search | num |
      | drees  | 1   |
      | tshirt | 2   |
      | blouse | 3   |
      | summer | 4   |

