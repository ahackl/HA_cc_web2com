from __future__ import annotations
import logging
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import Platform
from homeassistant.core import HomeAssistant

from pprint import pformat

import ochsner_web2com.web2com as web2com


DOMAIN = "web2com"

_LOGGER = logging.getLogger(DOMAIN)


def setup(hass, config):
    """Set up is called when Home Assistant is loading our component."""

    def handle_NormalSetpointRoomTemperature(call):
        """Handle the service call."""
        temperature = call.data.get("temperature", "0")
        # _LOGGER.info(pformat(temperature))

        username = config[DOMAIN]["username"]
        password = config[DOMAIN]["password"]
        ip_address = config[DOMAIN]["ip_address"]

        w2c = web2com.Service(ip_address, username, password)
        result = w2c.set_value("/1/2/4/99/6", temperature)
        # _LOGGER.info(pformat(result))

    hass.services.register(DOMAIN, "heating", handle_NormalSetpointRoomTemperature)

    sensors = config[DOMAIN]["sensors"]
    for optional in sensors:
        optional["username"] = config[DOMAIN]["username"]
        optional["password"] = config[DOMAIN]["password"]
        optional["ip_address"] = config[DOMAIN]["ip_address"]
        hass.helpers.discovery.load_platform("sensor", DOMAIN, optional, config)

    # Return boolean to indicate that initialization was successful.
    return True
