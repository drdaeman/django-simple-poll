from __future__ import absolute_import

# This module provides three important variables to support custom user models with migrations.
# See http://kevindias.com/writing/django-custom-user-models-south-and-reusable-apps/ for details.

# Safe User import for Django < 1.5
try:
    from django.contrib.auth import get_user_model
except ImportError:
    from django.contrib.auth.models import User
else:
    User = get_user_model()

# With the default User model these will be 'auth.User' and 'auth.user'
# so instead of using orm['auth.User'] we can use orm[user_orm_label]
user_orm_label = '%s.%s' % (User._meta.app_label, User._meta.object_name)
user_model_label = '%s.%s' % (User._meta.app_label, User._meta.model_name)
user_model_data = {
    'Meta': {
        'object_name': User.__name__,
        'db_table': "'%s'" % User._meta.db_table
    },
    User._meta.pk.attname: (
        'django.db.models.fields.AutoField', [],
        {'primary_key': 'True',
         'db_column': "'%s'" % User._meta.pk.column}
    ),
}
