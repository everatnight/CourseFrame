from django.db import models


class teacher(models.Model):
    """the model for teacher"""
    name = models.CharField(max_length=10)
    researcharea = models.CharField(max_length=50)
    biography = models.TextField(null=True, blank=True)
    contact = models.CharField(max_length=50, null=True, blank=True)
    officehour = models.CharField(max_length=30, null=True, blank=True)
    picture = models.ImageField(upload_to='image')
    project = models.TextField(null=True, blank=True)


class course(models.Model):
    """
        #todo google map api
        #todo auto get course description
        the course model location can use the google map api.
    """
    name = models.CharField(max_length=30)
    info = models.TextField(null=True, blank=True)
    prerequisites = models.ForeignKey('self', null=True, blank=True)
    time = models.CharField(max_length=20, null=True, blank=True)
    location = models.CharField(max_length=60, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    teacher = models.ForeignKey(teacher)
    timestamp = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u'%s %s' % (self.name, self.time)


class assignment(models.Model):
    """
        the assignment for the student.
        assignment type can be:
            lab
            homework
    """
    name = models.CharField(max_length=20)
    duetime = models.DateTimeField()
    description = models.TextField()
    atype = models.CharField(max_length=10)
    course = models.ForeignKey(course)
    timestamp = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u'%s %s' % (self.name, self.description)


class announcement(models.Model):
    """
        #todo how to implement for course and assignment,
        one of them should be not null?
        announcement model.announcement is for the assignment
        and the course.
    """
    course = models.ForeignKey(course, null=True, blank=True)
    assignment = models.ForeignKey(assignment, null=True, blank=True)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now=True)


class resources(models.Model):
    """
        the resources model.
        rtype canbe:
            slides
            code
            zip
    """
    name = models.CharField(max_length=30)
    rtype = models.CharField(max_length=10)
    filename = models.FileField(upload_to='resource', null=True, blank=True)
    assignment = models.ForeignKey(assignment, null=True, blank=True)
    course = models.ForeignKey(course, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name


class textbook(models.Model):
    """
        #todo public api to find text book
        the textbook model, may be not need to store in
        our database, just need to use some public api.
    """
    name = models.CharField(max_length=20)
    ISBN = models.CharField(max_length=20)
    course = models.ForeignKey(course)
    description = models.TextField()

    def __unicode__(self):
        return self.name
