Feature: calculating vat
  Scenario Outline: create product
    Given I created product called <name> with the price <price> and VAT <vat_rate>
    Then the vat value will be <vat_value>

    Examples: Products with 23%
    | name      | price | vat_rate | vat_value |
    |Mobile     |1230   | 23       | 230.00    |
    |Computer   |3600   | 23       | 630.00    |
    |Notebook   |7999   | 23       | 1499.00   |

    Examples: Products with 5%
    | name      | price | vat_rate | vat_value |
    |Mobile     |1230   | 5        | 230.00    |
    |Computer   |3600   | 5        | 630.00    |
    |Notebook   |7999   | 5        | 1499.00   |

