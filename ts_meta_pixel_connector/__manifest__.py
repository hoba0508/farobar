# -*- coding: utf-8 -*-
#############################################################################
#
#    Techvaria Solutions Pvt. Ltd.
#
#    Copyright (C) 2025-Techvaria Solutions(<https://techvaria.com>)
#    Author: Techvaria Solutions Pvt. Ltd.(info@techvaria.com)
#
#    You can modify it under the terms of the GNU AFFERO
#    GENERAL PUBLIC LICENSE (AGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU AFFERO GENERAL PUBLIC LICENSE (AGPL v3) for more details.
#
#    You should have received a copy of the GNU AFFERO GENERAL PUBLIC LICENSE
#    (AGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
#############################################################################

{
    'name': 'Meta Pixel Connector | Facebook Meta Pixel PageView Tracking',
    'version': '19.0.1.0.0',
    'summary': 'Facebook Meta Pixel PageView Tracking.',
    'description': 'Easily integrate Meta Pixel with your Odoo website to automatically track PageView events. Supports multi-website setups, allowing different Pixel Code per website for accurate and independent tracking.',
    'category': 'Website/Website',
    'author': 'Techvaria',
    'company': 'Techvaria',
    'maintainer': 'Techvaria',
    'website': "https://techvaria.com",
    "depends": ['website_sale'],
    "data": [
        'views/website_views.xml',
        'views/website_templates.xml',
    ],
    'images': [
        'static/description/screen.jpg',
    ],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
}
