"""Platform for sensor integration."""
from __future__ import annotations

import logging
import voluptuous as vol
import homeassistant.helpers.config_validation as cv

from pprint import pformat

from homeassistant.components.sensor import SensorEntity

# from homeassistant.const import TEMP_CELSIUS
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType, DiscoveryInfoType
from homeassistant.components.sensor import PLATFORM_SCHEMA
from homeassistant.const import (
    CONF_NAME,
    CONF_PASSWORD,
    CONF_USERNAME,
    CONF_IP_ADDRESS,
    CONF_AUTHENTICATION,
    CONF_ID,
    CONF_UNIT_OF_MEASUREMENT,
    CONF_DEVICE_CLASS,
    CONF_UNIQUE_ID,
    CONF_SCAN_INTERVAL,
)

from . import DOMAIN

import ochsner_web2com.web2com as web2com

_LOGGER = logging.getLogger("web2com")

# Validation of the user's configuration
PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend(
    {
        vol.Required(CONF_NAME): cv.string,
    }
)


def setup_platform(
    hass: HomeAssistant,
    config: ConfigType,
    add_entities: AddEntitiesCallback,
    discovery_info: DiscoveryInfoType | None = None,
) -> None:
    """Set up the sensor platform."""

    # We only want this platform to be set up via discovery.
    if discovery_info is None:
        return

    add_entities([ExampleSensor(discovery_info)])


class ExampleSensor(SensorEntity):
    """Representation of a sensor."""

    def __init__(self, discovery_info) -> None:
        """Initialize the sensor."""
        self._state = None
        self._name = discovery_info[CONF_NAME]
        self._password = discovery_info[CONF_PASSWORD]
        self._username = discovery_info[CONF_USERNAME]
        self._ip_address = discovery_info[CONF_IP_ADDRESS]
        self._id = discovery_info[CONF_ID]
        self._unit_of_measurement = discovery_info[CONF_UNIT_OF_MEASUREMENT]
        self._device_class = discovery_info[CONF_DEVICE_CLASS]
        self._unique_id = discovery_info[CONF_UNIQUE_ID]
        self._scan_interval = discovery_info[CONF_SCAN_INTERVAL]

        self._authentication = web2com.AUTH.DIGEST
        try:
            if discovery_info[CONF_AUTHENTICATION] == "Basic":
                self._authentication = web2com.AUTH.BASIC
        except:
            self._authentication = web2com.AUTH.DIGEST

    @property
    def id(self) -> str:
        """Return the id of the sensor."""
        return self._id

    @property
    def device_class(self) -> str:
        """Return the device class of the sensor."""
        return self._device_class

    @property
    def name(self) -> str:
        """Return the name of the sensor."""
        return self._name

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    @property
    def unique_id(self) -> str:
        """Return the entity_id of the sensor."""
        return self._unique_id

    @property
    def scan_interval(self) -> str:
        """Return the scan_interval of the sensor."""
        return self._scan_interval

    @property
    def unit_of_measurement(self) -> str:
        """Return the unit of measurement."""
        return self._unit_of_measurement

    def update(self) -> None:
        """Fetch new state data for the sensor.

        This is the only method that should fetch new data for Home Assistant.
        """
        w2c = web2com.Service(self._ip_address, self._username, self._password, auth=self._authentication)
        result = w2c.get_value(self._id)
        self._state = result[1]
