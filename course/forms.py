from django.forms import ModelForm
from course.models import teacher, resources, assignment, announcement, course, textbook


class TeacherForm(ModelForm):
    """
        teacher' form.

    """
    class Meta:
        model = teacher


class courseForm(ModelForm):
    """
        course's Form
        name
        info require false
        prerequisites require false
        time require false
        location require false
        description require false
        teacher 
        timestamp
        >>> from datetime import datetime
        >>> from forms import courseForm
        >>> data = {
            'name' : 'hello',
            'info' : '',
            'prerequisites' : '',
            'time' : '',
            'location' : '',
            'description' : '',
            'teacher' : '',
            'timestamp' : datetime.now()
        }
        >>> f = courseForm(data)
        >>> f.is_valid()
        True
        >>> data['name'] = ''
        False
    """

class assignmentForm(ModelForm):
    """
        course's Form
        name
        info require false
        prerequisites require false
        time require false
        location require false
        description require false
        teacher 
        timestamp
        >>> from datetime import datetime
        >>> from forms import courseForm
        >>> data = {
            'name' : 'hello',
            'info' : '',
            'prerequisites' : '',
            'time' : '',
            'location' : '',
            'description' : '',
            'teacher' : '',
            'timestamp' : datetime.now()
        }
        >>> f = courseForm(data)
        >>> f.is_valid()
        True
        >>> data['name'] = ''
        False
    """

class announcementForm(ModelForm):
    """
        course's Form
        name
        info require false
        prerequisites require false
        time require false
        location require false
        description require false
        teacher 
        timestamp
        >>> from datetime import datetime
        >>> from forms import courseForm
        >>> data = {
            'name' : 'hello',
            'info' : '',
            'prerequisites' : '',
            'time' : '',
            'location' : '',
            'description' : '',
            'teacher' : '',
            'timestamp' : datetime.now()
        }
        >>> f = courseForm(data)
        >>> f.is_valid()
        True
        >>> data['name'] = ''
        False
    """

class resourcesForm(ModelForm):
    """
        course's Form
        name
        info require false
        prerequisites require false
        time require false
        location require false
        description require false
        teacher 
        timestamp
        >>> from datetime import datetime
        >>> from forms import courseForm
        >>> data = {
            'name' : 'hello',
            'info' : '',
            'prerequisites' : '',
            'time' : '',
            'location' : '',
            'description' : '',
            'teacher' : '',
            'timestamp' : datetime.now()
        }
        >>> f = courseForm(data)
        >>> f.is_valid()
        True
        >>> data['name'] = ''
        False
    """

class textbookForm(ModelForm):
    """
        course's Form
        name
        info require false
        prerequisites require false
        time require false
        location require false
        description require false
        teacher 
        timestamp
        >>> from datetime import datetime
        >>> from forms import courseForm
        >>> data = {
            'name' : 'hello',
            'info' : '',
            'prerequisites' : '',
            'time' : '',
            'location' : '',
            'description' : '',
            'teacher' : '',
            'timestamp' : datetime.now()
        }
        >>> f = courseForm(data)
        >>> f.is_valid()
        True
        >>> data['name'] = ''
        False
    """