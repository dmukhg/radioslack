from django.core.management.base import BaseCommand, CommandError
from rtmbot.rtmbot import *

class Command(BaseCommand):
    def handle(self, *args, **options):
        def main_loop():
            if "LOGFILE" in config:
                logging.basicConfig(filename=config["LOGFILE"], level=logging.INFO, format='%(asctime)s %(message)s')
            logging.info(directory)
            try:
                bot.start()
            except KeyboardInterrupt:
                sys.exit(0)
            except:
                logging.exception('OOPS')

        directory = os.path.dirname(sys.argv[0])
        if not directory.startswith('/'):
            directory = os.path.abspath("{}/{}".format(os.getcwd(),
                                    directory
                                    ))

        config = yaml.load(file('rtmbot/rtmbot.conf', 'r'))
        debug = config["DEBUG"]
        bot = RtmBot(config["SLACK_TOKEN"], directory + '/rtmbot', config)
        site_plugins = []
        files_currently_downloading = []
        job_hash = {}


        if config.has_key("DAEMON"):
            if config["DAEMON"]:
                import daemon
                with daemon.DaemonContext():
                    main_loop()
        main_loop()
