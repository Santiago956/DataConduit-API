Feature: Allow creation of a quality rule for a specific table and column

  Scenario: Request to create a quality rule with all attributes provided: rule type, table name, column, and rule-specific parameters
    Given the creation of a new uniqueness rule with all attributes: rule type (uniqueness), table and column
    When the create method is called passing these attributes
    Then it checks for the existence of the table
    And whether the rule in question already exists
    And creates the quality rule
