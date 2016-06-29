from setuptools import setup

requires = [
	'pyramid',
	'pyramid_chameleon',
	'pytest',
	'webtest',
]

setup(name='tutu',
	install_requires=requires,
	entry_points="""\
	[paste.app_factory]
	main = tutu:main
	""",
);
