{
    'name': "Inventory Dashboard",
    'version': '15.0.1.0.2',
    'summary': """Create Configurable Dashboards Easily""",
    'description': """making dashboards easier""",
    'author': 'IT PMR TEAM',
    'depends': ['base', 'web'],
    'data': [
        'views/dashboard_view.xml',
        'views/inventory_block_view.xml',
        'views/dashboard_menu_view.xml',
        'security/ir.model.access.csv',
    ],
    'assets': {
        'web.assets_backend': [
            'inventory_dashboard/static/src/js/inventory_dashboard.js',
            'inventory_dashboard/static/src/scss/style.scss',
            'https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.8.0/Chart.bundle.js',
            'https://fonts.googleapis.com/css?family=Source+Sans+Pro:300,400,400i,700',
        ],
        'web.assets_qweb': [
            'inventory_dashboard/static/src/xml/dynamic_dashboard_template.xml',
        ],
    },
    # 'images': ['static/description/inventory_dashboard.png'],
    'demo': [],
    'qweb': [],
    'license': "AGPL-3",
    'installable': True,
    'application': True,
    'auto_install': False,
}
