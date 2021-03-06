from distutils.core import setup

setup(name='chunks',
      version='2.0',
      description='Keyed blocks of content for use in your Django templates',
      author='Clint Ecker',
      author_email='me@clintecker.com',
      url='https://github.com/code-on/django-chunks',
      packages=['chunks', 'chunks.templatetags'],
      classifiers=['Development Status :: 4 - Beta',
                   'Environment :: Web Environment',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Utilities'],
      )
