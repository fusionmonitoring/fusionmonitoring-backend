#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Resource information of timeseriesretention
"""


def get_name(friendly=False):
    """Get name of this resource

    :return: name of this resource
    :rtype: str
    """
    if friendly:
        return "TS cache"
    return 'timeseriesretention'


def get_doc():
    """Get documentation of this resource

    :return: rst string
    :rtype: str
    """
    return """
    The ``timeseriesretention`` model is a cache used internally by the backend to store the
    data that could not be sent to Graphite / Influx DB because of a temporarily missing
    connection.
    """


def get_schema():
    """Schema structure of this resource

    :return: schema dictionary
    :rtype: dict
    """
    return {
        'internal_resource': True,
        'schema': {
            'name': {
                "title": "Stored metric name",
                'type': 'string',
                'required': True,
            },
            'realm': {
                "title": "Stored metric host realm",
                'type': 'string',
                'required': True,
            },
            'host': {
                "title": "Stored metric host",
                'type': 'string',
                'required': True,
            },
            'service': {
                "title": "Stored metric service",
                'type': 'string',
                'required': True,
            },
            'value': {
                "title": "Stored metric value",
                'type': 'integer',
                'required': True,
            },
            'timestamp': {
                "title": "Stored metric timestamp",
                'type': 'integer',
                'required': True,
            },
            'graphite': {
                "title": "Graphite relation",
                'type': 'objectid',
                'data_relation': {
                    'resource': 'graphite',
                    'embeddable': True
                },
                'nullable': True,
                'default': None
            },
            'influxdb': {
                "title": "Graphite relation",
                'type': 'objectid',
                'data_relation': {
                    'resource': 'influxdb',
                    'embeddable': True
                },
                'nullable': True,
                'default': None
            },
        }
    }
