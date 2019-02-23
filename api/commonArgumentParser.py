import configargparse

def getNew():
    parser = configargparse.ArgParser(default_config_files=["/etc/wacky-tracky/server.cfg", "~/.wacky-tracky/server.cfg"]);
    parser.add_argument("--dbUser", env_var = "WT_DB_USER")
    parser.add_argument("--dbPass", env_var = "WT_DB_PASS")

    return parser;
