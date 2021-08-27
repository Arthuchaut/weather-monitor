from django.db import models


class MeasureManager(models.Manager):
    '''The measure management class.'''

    def latest_measure_num(self) -> int:
        '''Returns the latest measure_num.

        Returns:
            int: The latest measure num. None if no measure exists yet.
        '''

        measure: dict[str, int] = self.aggregate(models.Max('measure_num'))
        return measure['measure_num__max']

    def next_measure_num(self) -> int:
        '''Returns the next measure_num.

        Returns:
            int: The next measure num. 1 if no measure is registered yet.
        '''

        measure_num: int = self.latest_measure_num()
        return measure_num + 1 if measure_num else 1
