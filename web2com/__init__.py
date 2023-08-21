from __future__ import annotations
import logging
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import Platform
from homeassistant.core import HomeAssistant

from pprint import pformat


DOMAIN = "web2com"

ATTR_NAME = "name"
DEFAULT_NAME = "World"

_LOGGER = logging.getLogger("web2com")


def setup(hass, config):
    """Set up is called when Home Assistant is loading our component."""


    def handle_hello(call):
        """Handle the service call."""
        name = call.data.get(ATTR_NAME, DEFAULT_NAME)
        temperature = call.data.get("temperature", "0")


        hass.states.set("web2com.hello", name)

    # hass.services.register(DOMAIN, "hello", handle_hello)

    # hass.data[DOMAIN] = {"temperature": 23}

    sensors = config[DOMAIN]["sensors"]
    for optional in sensors:
        optional["username"] = config[DOMAIN]["username"]
        optional["password"] = config[DOMAIN]["password"]
        optional["ip_address"] = config[DOMAIN]["ip_address"]
        hass.helpers.discovery.load_platform("sensor", DOMAIN, optional, config)

    # Return boolean to indicate that initialization was successful.
    return True
