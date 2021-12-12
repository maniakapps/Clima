from datetime import date

from .forecast_type import ForecastType
from dataclasses import dataclass


@dataclass
class Forecast:
    _current_temp: float
    _humidity: float
    _wind: float
    _high_temp: object = None
    _low_temp: object = None
    _description: str = ""
    forecast_date: object = None
    _forecast_type: object = ForecastType.TODAY

    if forecast_date is None:
        forecast_date = date.today()
    else:
        _forecast_date = forecast_date

    @property
    def forecast_date(self):
        return self._forecast_date

    @forecast_date.setter
    def forecast_date(self, forecast_date):
        self._forecast_date = forecast_date.strftime("%a %b %d")

    @property
    def current_temp(self):
        return self._current_temp

    @property
    def humidity(self):
        return self._humidity

    @property
    def wind(self):
        return self._wind

    @property
    def description(self):
        return self._description

    def __str__(self):
        offset = ' ' * 4

        if self._forecast_type == ForecastType.TODAY:
            temperature = (f'{offset}{self._current_temp}\xb0\n'
                           f'{offset}High {self._high_temp}\xb0 / '
                           f'Low {self._low_temp}\xb0 ')
        else:
            temperature = (f'{offset}High {self._high_temp}\xb0 / '
                           f'Low {self._low_temp}\xb0 ')

        return (f'>> {self.forecast_date}\n'
                f'{temperature}'
                f'({self._description})\n'
                f'{offset}Wind: '
                f'{self._wind} / Humidity: {self._humidity}\n')
