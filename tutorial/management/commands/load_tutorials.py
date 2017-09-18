from django.core.management.base import BaseCommand, CommandError

from tutorial.factories import TopicFactory, CategoryFactory, TutorialFactory


class Command(BaseCommand):
    help = 'Create dummy tutorials for you with topics and without topics ' \
           '- depending upon what option you choose'

    def add_arguments(self, parser):
        parser.add_argument('--topic', dest='topic', default=True,
                            help='Create tutorials with topic and category')
        parser.add_argument('topic', nargs='+', type=bool)

    def handle(self, *args, **options):
        if options['topic'] is False:
            pass
            # Create without topic

        # Otherwise create with topic and category

        # self.stdout.write(self.style.SUCCESS('Successfully closed poll "%s"' % poll_id))