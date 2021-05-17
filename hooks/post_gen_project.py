from textwrap import dedent


def main():
    display_actions_message()


def display_actions_message():

    vars = dict(separator="=" * 79)
    msg = dedent(
        """
        %(separator)s
        This is a scaffolding of a FormShare plugin. You can use it
        to create complex plugins.
        %(separator)s

        To make FormShare to run this plugin do:
            
        Activate the FormShare environment .
            . /path/to/FormShare/bin/activate
            
        Change directory into your newly created plugin.
            cd {{ cookiecutter.plugin_name }}

        Build the plugin
            python setup.py develop

        Add the plugin to the FormShare list of plugins by editing the line
            #formshare.plugins = examplePlugin
            formshare.plugins = {{ cookiecutter.plugin_name }}
        

        Run FormShare again
        """
        % vars
    )
    print(msg)


if __name__ == "__main__":
    main()
