from distutils.core import setup

setup(
    name='foo',  # How you named your package folder (MyLib)
    packages=['foo'],  # Chose the same as "name"
    version='0.0.2',  # Start with a small number and increase it with every change you make
    # license='NA',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    description='convert web cookie string to dictionary',  # Give a short description about your library
    author='fenuo',  # Type in your name
    author_email='fenuo@fenuo.com',  # Type in your E-Mail
    url='https://github.com/fenuo/foo',  # Provide either the link to your github or to your website
    download_url='https://github.com/fenuo/foo/foo-master.zip',  # I explain this later on
    keywords=['Cookies', 'Python Dictionary'],  # Keywords that define your package best
    install_requires=[],  # I get to this in a second
    classifiers=[
        'Development Status :: 3 - Alpha',
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Intended Audience :: Developers',  # Define that your audience are developers
        'Topic :: Software Development :: Build Tools',  # Again, pick a license
        'Programming Language :: Python :: 3',  # Specify which pyhton versions that you want to support
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
