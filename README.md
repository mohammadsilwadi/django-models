# django-models
+ create snack_tracker_project project
+ This will involve some preliminary steps.
+ Review previous class lab for details.
+ create snacks app
+  Add snacks app to project
+ create Snack model
+ make sure it extends from proper base class
+ add name as a CharField with maximum length of 64 characters.
+ add purchaser ForeignKey related to Django’s built in user model with CASCADE delete option.
+ from django.contrib.auth import get_user_model
+ add description TextField

[PR](https://github.com/mohammadsilwadi/django-models/pull/1)