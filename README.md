# Readme

Home Assistant custom component for the web2com interface from ochsner.
Use the python module [ochnser-web2com](https://pypi.org/project/ochsner-web2com/)

This component is in an experimental stage.

## Installation

Create a folder "web2com" in "custom_components".
Copy all files to this folder.

```text
custom_components/web2com/__init__.py
custom_components/web2com/manifest.json
custom_components/web2com/sensor.py
custom_components/web2com/service.yaml
```

Copy "ochsner_web2com.yaml" to your configuration folder.
Copy "ochsner_web2com_template.yaml" to your configuration folder.

Add a link in you configuration.yaml file

```yaml
web2com: !include ochsner_web2com.yaml
template: !include ochsner_web2com_template.yaml
```
Set the user name and the ip number of the web2com server
in the file ochsner_web2com.yaml

```yaml
ip_address: 192.168.188.50
username: OEM
```

Optional:
In the file ochsner_web2com.yaml the authentication method can be set.
If the value is not set then Digest authentication will be used.

```yaml
authentication: Digest
```
or

```yaml
authentication: Basic
```

Set a password in the secrets.yaml file

```yaml
web2com_password: your_password
```

With the [climate_template](https://github.com/jcwillox/hass-template-climate/)
it is possible to combine a sensor and a service to a climate integration.
```yaml
climate:
  - platform: climate_template
    name: RaumtemperaturSollwert
    modes:
      - "auto"
    min_temp: 15
    max_temp: 30
    temp_step: 0.5
    current_temperature_template: "{{states('sensor.Normal_Raumtemperatur_Heizbetrieb') }}"
    set_temperature:
      - service: web2com.heating
        data:
          temperature:  "{{ temperature }}"
```


## Configuration

A sensor can be set via the ochsner_web2com.yaml file.

```yaml
sensors:
  - name: Heizenergie Teil 1 MWh
    scan_interval: 30
    unique_id: web2com_HeizenergieTeil1MWh
    id: /1/2/1/125/10
    unit_of_measurement: MWh
    device_class: "energy"
```

One service is set up:
    NormalSetpointRoomTemperature

## Paramter List:

| Description                                                | ID chain      |
| ---------------------------------------------------------- | ------------- |
| heat pump: State heat generator control                    | /1/2/1/125/0  |
| heat pump: Flow temperature heat generator                 | /1/2/1/125/1  |
| heat pump: Return flow temperature heat generator          | /1/2/1/125/2  |
| heat pump: Heat source outlet temperature                  | /1/2/1/125/3  |
| heat pump: Heat source inlet temperature                   | /1/2/1/125/4  |
| heat pump: Operation cycles                                | /1/2/1/125/5  |
| heat pump: Operation hours                                 | /1/2/1/125/6  |
| heat pump: Volume flow heat energy                         | /1/2/1/125/7  |
| heat pump: Flow rate heat source                           | /1/2/1/125/8  |
| heat pump: Thermal energy kWh                              | /1/2/1/125/9  |
| heat pump: Thermal energy MWh                              | /1/2/1/125/10 |
| heat pump: Energy DHW kWh                                  | /1/2/1/125/11 |
| heat pump: Energy DHW MWh                                  | /1/2/1/125/12 |
| auxiliary: State heat generator control                    | /1/2/2/126/0  |
| auxiliary: Flow temperature heat generator                 | /1/2/2/126/1  |
| auxiliary: Operation cycles                                | /1/2/2/126/2  |
| auxiliary: Operation hours                                 | /1/2/2/126/3  |
| auxiliary: Thermal energy kWh                              | /1/2/2/126/4  |
| auxiliary: Thermal energy MWh                              | /1/2/2/126/5  |
| heating circuit: State heating circuit control             | /1/2/4/119/0  |
| heating circuit: Outdoor temperature                       | /1/2/4/119/1  |
| heating circuit: Outdoor temperature average value         | /1/2/4/119/2  |
| heating circuit: Setpoint room temperature                 | /1/2/4/119/3  |
| heating circuit: Actual heating circuit flow temperature   | /1/2/4/119/4  |
| heating circuit: Setpoint heating circuit flow temperature | /1/2/4/119/5  |
| DHW: State DHW control                                     | /1/2/7/121/0  |
| DHW: Actual DHW temperature                                | /1/2/7/121/1  |
| DHW: DHW setpoint                                          | /1/2/7/121/2  |
| Manager: Storage tank temperature top                      | /1/2/8/122/0  |
| Manager: Storage tank temperature center                   | /1/2/8/122/1  |
| Manager: Plant flow temperature                            | /1/2/8/122/2  |
| Manager: Plant CH setpoint flow temperature                | /1/2/8/122/3  |
| Manager: Heating power in heating mode                     | /1/2/8/122/4  |
| Manager: Heating power in DHW mode                         | /1/2/8/122/5  |
| Manager: State heating manager                             | /1/2/8/122/6  |

Default paramter:

| Description | ID  |
| ----------- | --- |
| eBus        | 1   |
| device      | 2   |
