""" apps/main/models.py """

from django.db import models


class Day(models.Model):
    """ Abstract day model. """
    name = models.CharField(
        null=True,
        max_length=255,
    )
    header = models.TextField(
        null=True,
    )
    body = models.TextField(
        null=True,
    )
    force = models.PositiveIntegerField(
        null=True,
    )

    class Meta:
        abstract = True

    def __str__(self):
        return self.header


class DayTempo(Day):
    """ Day tempo model. """
    baseline = models.CharField(
        max_length=25,
        choices=[
            ('Start', 'Start'),
            ('Easter', 'Easter'),
            ('End', 'End'),
        ],
    )
    add = models.IntegerField()


class DaySancto(Day):
    """ Day sancto model. """
    month = models.IntegerField(
        choices=[
            (1, 'January'),
            (2, 'February'),
            (3, 'March'),
            (4, 'April'),
            (5, 'May'),
            (6, 'June'),
            (7, 'July'),
            (8, 'August'),
            (9, 'September'),
            (10, 'October'),
            (11, 'November'),
            (12, 'December'),
        ],
    )
    day = models.IntegerField(
        choices=[(i + 1, i + 1) for i in range(31)],
    )
