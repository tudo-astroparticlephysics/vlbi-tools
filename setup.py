from setuptools import setup, find_packages

setup(
    name='vlbi_tools',
    version='0.0.1',
    description='Tools for analyzing and presenting VLBI data',
    url='https://github.com/tudo-astroparticlephysics/vlbi-tools',
    author='Kevin Schmidt',
    author_email='kevin3.schmidt@tu-dortmund.de',
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
        'astropy',
    ],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'vlbi_convert_difmap2csv = vlbi_tools.scripts.convert_difmap2csv:main'
        ]
    },
    classifiers=[
         'Development Status :: 2 - Pre-Alpha',
         'Intended Audience :: Science/Research',
         'License :: OSI Approved :: MIT License',
         'Natural Language :: English',
         'Operating System :: OS Independent',
         'Programming Language :: Python',
         'Programming Language :: Python :: 3.6',
         'Programming Language :: Python :: 3 :: Only',
         'Topic :: Scientific/Engineering :: Astronomy',
         'Topic :: Scientific/Engineering :: Physics',
    ],
)
