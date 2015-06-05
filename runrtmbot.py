from django.core.management.base import BaseCommand, CommandError
#from rtmbot.rtmbot import RtmBot

class Command(BaseCommand):
    def handle(self, *args, **options):
        directory = os.path.dirname(sys.argv[0])
        if not directory.startswith('/'):
            directory = os.path.abspath("{}/{}".format(os.getcwd(),
                                    directory
                                    ))

        config = yaml.load(file('rtmbot/rtmbot.conf', 'r'))
        debug = config["DEBUG"]
        bot = RtmBot(config["SLACK_TOKEN"])
        site_plugins = []
        files_currently_downloading = []
        job_hash = {}

        if config.has_key("DAEMON"):
            if config["DAEMON"]:
                import daemon
                with daemon.DaemonContext():
                    main_loop()
        main_loop()

