from textwrap import dedent


def main():
    display_actions_message()


def display_actions_message():

    vars = dict(separator="=" * 79)
    msg = dedent(
        """
        %(separator)s
        This is a scaffolding of a ClimMob plugin. You can use it
        to create complex plugins.
        %(separator)s

        To make ClimMob to run this plugin do:
            
        Activate the ClimMob environment .
            . /path/to/ClimMob/bin/activate
            
        Change directory into your newly created plugin.
            cd {{ cookiecutter.plugin_name }}

        Build the plugin
            python setup.py develop

        Add the plugin to the ClimMob list of plugins by editing the line
            #climmob.plugins = examplePlugin
            climmob.plugins = {{ cookiecutter.plugin_name }}
        

        Run ClimMob again
        """
        % vars
    )
    print(msg)


if __name__ == "__main__":
    main()
