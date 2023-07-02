# Manual testing

Here is a list of the manual testing that was carried out to ensure that the Lifesort API works as intended at the time of deployment. These tests are designed to test each created view for functionality.

The intended functionality of Lifesort is that users can only access their own profile and tasks and an error should be returned to the user if they have attempted to access a task or a profile of another user.

All users of the site should be able to create, read, update and delete tasks and create, read, update their own profile.

## Root route view

The root route exists to show a welcome message to a user who visits the API and shows the API is working.

- [x] Test when a user visits the API they are shown a welcome message.