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

## Quick task views

I tested the quick task views to ensure users can only access their own tasks are have full CRUD control as well.

- [x] Users can create a quick task.

![Creating a quick task](static/images-testing/quick-task/create-quick-task.png)

- [x] Users can access their own quick task.

![Quick task detail view](static/images-testing/quick-task/quick-task-detail-view.png)

- [x] Users can edit a quick task.

![Quick task edit view](static/images-testing/quick-task/edit-quick-task.png)

- [x] Users can delete a quick task.

![Quick task deletion view](static/images-testing/quick-task/delete-quick-task.png)

- [x] Users cannot create a quick task woth a due date more than 1000 days in future.

![Create a quick task with a due date more than 1000 days in future](static/images-testing/quick-task/quick-task-in-1000-days-in-future.png)

- [x] Users cannot create a quick task with a due date in the past.

![Create a quick task with due date in past](static/images-testing/quick-task/quick-task-in-past.png)

- [x] Users cannot access another users quick task.

![User attempting to access another users task](static/images-testing/quick-task/other-users-quick-task.png)

- [x] logged in user can access their own quick task list.

![Logged in user viewing their own quick task list view](static/images-testing/quick-task/quick-task-list-logged-in.png)

- [x] logged out user cannot access quick task list.

![Logged out user trying to access quick task list](static/images-testing/quick-task/quick-task-list-logged-out.png)

