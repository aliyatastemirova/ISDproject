# Changelog

### 2020-05-14
#### [#58mpt5](https://app.clickup.com/t/#58mpt5) - Add partner registration
- Added Partners group, is_student and is_partner boolean fields in User model
- Added a custom filter for Users in Django admin panel to filter by students or by partners
- Added a better view for User and Profile models on Django admin panel
- Added a possibility to view all Users that belong to a Group, easily remove or add users from the group

### 2020-05-09
#### [#54nb2t](https://app.clickup.com/t/54nb2t) - Create a user dashboard
- Added user dashboard view
- Added decorators to handle authenticated users
#### [#6rb527](https://app.clickup.com/t/6rb527) - Make auth user and Student user separate
- Changed user auth model, which required database changes
- Added Student user group, which can be later have specific permissions

### 2020-04-26
#### [#689cmp](https://app.clickup.com/t/689cmp) - Add profile picture upload feature for students
- Created a field for a profile picture in Profile model
- Updated signals to clean up models file and create a profile automatically from signals.py
#### [#6eaxu7](https://app.clickup.com/t/6eaxu7) - Add a form for updating a user profile
- Created a form for updating user's profile details
- Created a form for changing user's password

### 2020-04-19
#### [#60b05j](https://app.clickup.com/t/60b05j) - Create class Student in models.py
- Created a Student class for authorization and Profile class for more information and creating a profile page
- Added signals for custom user creation and creating a profile automatically
#### [#60b05r](https://app.clickup.com/t/60b05r) - Create account creation feature
- Created a form, views and urls for registration and login