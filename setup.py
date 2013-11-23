from distutils.core import setup

setup(
    name='biblib',
    version='0.1.0',
    description='Simple, correct BibTeX parser and algorithms',
    url='https://github.com/aclements/biblib',
    author='Austin Clements',
    author_email='aclements@csail.mit.edu',
    packages=['biblib'],
    keywords=['bibtex', 'tex'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Database',
        'Topic :: Text Processing',
    ],
    long_description=open('README.md').read(),
)
