# This file is part of Tryton.  The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.

try:
    from trytond.modules.product_cost_warehouse.tests.test_product_cost_warehouse import suite  # noqa: E501
except ImportError:
    from .test_product_cost_warehouse import suite

__all__ = ['suite']
