Feature: Eating Cucumbers
  Feature: Update password
  Scenario: Admin user can update the user password
Given I am in the HR system with an Admin account
When I update password of another user
Then I receive a message for updating password successfully
And user password is updated to the new password