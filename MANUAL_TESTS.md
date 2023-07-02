# Manual testing

Here is a list of the manual testing that was carried out to ensure that the Lifesort API works as intended at the time of deployment. These tests are designed to test each created view for functionality.

The intended functionality of Lifesort is that users can only access their own profile and tasks and an error should be returned to the user if they have attempted to access a task or a profile of another user.

All users of the site should be able to create, read, update and delete tasks and create, read, update their own profile.

## Django installed correctly

I manually tested early and throughout the process of building the Lifesort API. That started with ensuring Django had installed correctly.

- [x] Test Django had installed correctly

![Django install message](static/images-testing/django-install.png)

## Root route view

The root route exists to show a welcome message to a user who visits the API and shows the API is working.

- [x] Test when a user visits the API they are shown a welcome message.

![Root route welcome message](static/images-testing/api-root-route-page.png)

- [x] Test deployed welcome message screen.

![Root route deployed welcome message](static/images-testing/deployed-api-welcome-screen.png)

## Profile views

I tested the profile views to ensure that users can only see their own profile and edit their own profile as well there is no delete option for the profile view.

- [x] Test a user cannot see a profile if they are not logged in.

![Logged out profile list](static/images-testing/profile/logged-out-profile-list.png)

- [x] Test when a user is logged in they cannot access another profile.

![Logged in accessing another profile](static/images-testing/profile/logged-in-other-profile.png)

- [x] Test a user can access their own profile when logged in.

![Logged in accessing own profile](static/images-testing/profile/logged-in-own-profile.png)

- [x] Test a user can edit their own profile when logged in.

![Editing own profile](static/images-testing/profile/edit-profile.png)
